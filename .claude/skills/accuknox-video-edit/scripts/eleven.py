"""ElevenLabs text to speech. The key is resolved at run time and never printed or written.

Key order:
  1. ELEVENLABS_API_KEY in the environment
  2. ELEVENLABS_API_KEY_1 .. _6 in D:\\Atharva\\NOTES\\.env, burned in order. A slot that answers
     quota_exceeded is skipped for the rest of the run and the same line is retried on the next.

    python eleven.py sample "<neutral sentence>"   write voice samples for the shortlist below
"""
import json
import os
import re
import ssl
import sys
import urllib.error
import urllib.request

ENV_FILE = r"D:\Atharva\NOTES\.env"

# This machine's Python has an expired CA root, so verification is off for this one host.
CTX = ssl.create_default_context()
CTX.check_hostname = False
CTX.verify_mode = ssl.CERT_NONE

# The default model and voice for every AccuKnox video. eleven_v4 accepts audio tags such as
# [excited] or [whispers] at the start of a line, and voice_settings including style and speed.
MODEL = "eleven_v4"
DEFAULT_VOICE = "Xb7hH8MSUJpSbSDYk0k2"   # Alice, British female, the house voice
DEFAULT_SETTINGS = {"stability": 0.45, "similarity_boost": 0.8, "style": 0.35, "speed": 1.0}

# Premade voices every account can use. The keys lack voices_read, so they cannot be listed.
VOICES = {
    "alice": "Xb7hH8MSUJpSbSDYk0k2",    # crisp British female, the default
    "lily": "pFZP5JQG7iQjIQuC4Bku",     # warm British female, slower
    "brian": "nPczCjzI2devNBz1zQrb",    # calm, mid-low male
    "daniel": "onwK4e9ZLuTAKqWW03F9",   # British male, slower
}

_slots = None
_dead = set()


def slots():
    """Every candidate key, in burn order. The environment key comes first when set."""
    global _slots
    if _slots is None:
        _slots = []
        k = os.environ.get("ELEVENLABS_API_KEY", "").strip()
        if len(k) >= 20:
            _slots.append(k)
        if os.path.exists(ENV_FILE):
            env = open(ENV_FILE, encoding="utf-8").read()
            for i in range(1, 7):
                m = re.search(rf"^ELEVENLABS_API_KEY_{i}\s*=\s*['\"]?([^'\"\r\n]+)", env, re.M)
                if m and len(m.group(1).strip()) >= 20 and m.group(1).strip() not in _slots:
                    _slots.append(m.group(1).strip())
    return _slots


def key():
    for k in slots():
        if k not in _dead:
            return k
    sys.exit("No ElevenLabs slot has credits left. Fill another ELEVENLABS_API_KEY_n in "
             rf"{ENV_FILE}. Do not switch to another voice service.")


def _post(path, body):
    rq = urllib.request.Request("https://api.elevenlabs.io" + path, data=json.dumps(body).encode(),
                                headers={"xi-api-key": key(), "Content-Type": "application/json"})
    return urllib.request.urlopen(rq, timeout=180, context=CTX)


def tts(text, voice_id=DEFAULT_VOICE, out="line.mp3", model=MODEL, settings=None):
    """Write one line to `out` (mp3). Falls back to 128 kbps when the plan blocks 192."""
    body = {"text": text, "model_id": model, "voice_settings": settings or DEFAULT_SETTINGS}
    fmts = ["mp3_44100_192", "mp3_44100_128"]
    while fmts:
        fmt = fmts[0]
        try:
            with _post(f"/v1/text-to-speech/{voice_id}?output_format={fmt}", body) as r:
                data = r.read()
            with open(out, "wb") as f:
                f.write(data)
            return
        except urllib.error.HTTPError as e:
            msg = e.read().decode("utf-8", "replace")
            if "output_format_not_allowed" in msg:
                fmts.pop(0)
                continue
            if "quota_exceeded" in msg:
                _dead.add(key())   # exits when no slot is left
                print(f"  slot out of credits, moving to slot {len(_dead) + 1}", flush=True)
                key()
                continue
            sys.exit(f"ElevenLabs HTTP {e.code}: {msg[:200]}")
    sys.exit("ElevenLabs refused every output format.")


if __name__ == "__main__":
    if len(sys.argv) >= 3 and sys.argv[1] == "sample":
        os.makedirs("voice_samples", exist_ok=True)
        for name, vid in VOICES.items():
            tts(sys.argv[2], vid, os.path.join("voice_samples", f"{name}.mp3"))
            print("voice_samples/" + name + ".mp3")
    else:
        sys.exit(__doc__)
