"""ElevenLabs text to speech. The key is resolved at run time and never printed or written.

Key order:
  1. ELEVENLABS_API_KEY in the environment
  2. D:\\Atharva\\NOTES\\SCRIPTS\\keys\\keys.py elevenlabs  (first slot that still has credits)

    python eleven.py sample "<neutral sentence>"   write voice samples for the shortlist below
"""
import json
import os
import ssl
import subprocess
import sys
import urllib.error
import urllib.request

KEYS_PY = r"D:\Atharva\NOTES\SCRIPTS\keys\keys.py"

# This machine's Python has an expired CA root, so verification is off for this one host.
CTX = ssl.create_default_context()
CTX.check_hostname = False
CTX.verify_mode = ssl.CERT_NONE

# Premade voices every account can use. The keys lack voices_read, so they cannot be listed.
VOICES = {
    "brian": "nPczCjzI2devNBz1zQrb",    # calm, mid-low male, the tested default
    "daniel": "onwK4e9ZLuTAKqWW03F9",   # British, slower
    "sarah": "EXAVITQu4vr4xnSDxMaL",    # warm female
    "alice": "Xb7hH8MSUJpSbSDYk0k2",    # crisp British female
    "will": "bIHbv24MWmeRgasZH58o",     # friendly, lighter male
}

_key = None


def key():
    global _key
    if _key:
        return _key
    k = os.environ.get("ELEVENLABS_API_KEY", "").strip()
    if not k and os.path.exists(KEYS_PY):
        r = subprocess.run([sys.executable, KEYS_PY, "elevenlabs"], capture_output=True, text=True)
        out = r.stdout.strip().splitlines()
        k = out[-1].strip() if out else ""
    if len(k) < 20:
        sys.exit("No ElevenLabs key. Set ELEVENLABS_API_KEY, or fill ELEVENLABS_API_KEY_1.._6 in "
                 r"D:\Atharva\NOTES\.env so keys.py can pick a slot. Do not switch to another voice service.")
    _key = k
    return k


def _post(path, body):
    rq = urllib.request.Request("https://api.elevenlabs.io" + path, data=json.dumps(body).encode(),
                                headers={"xi-api-key": key(), "Content-Type": "application/json"})
    return urllib.request.urlopen(rq, timeout=180, context=CTX)


def tts(text, voice_id, out, model="eleven_v3", settings=None):
    """Write one line to `out` (mp3). Falls back to 128 kbps when the plan blocks 192."""
    body = {"text": text, "model_id": model}
    if settings:
        body["voice_settings"] = settings
    for fmt in ("mp3_44100_192", "mp3_44100_128"):
        try:
            with _post(f"/v1/text-to-speech/{voice_id}?output_format={fmt}", body) as r:
                data = r.read()
            with open(out, "wb") as f:
                f.write(data)
            return
        except urllib.error.HTTPError as e:
            msg = e.read().decode("utf-8", "replace")
            if "output_format_not_allowed" in msg:
                continue
            if "quota_exceeded" in msg:
                global _key
                _key = None
                sys.exit("ElevenLabs slot is out of credits. keys.py moves to the next slot on the next run; rerun tts.")
            sys.exit(f"ElevenLabs HTTP {e.code}: {msg[:200]}")


if __name__ == "__main__":
    if len(sys.argv) >= 3 and sys.argv[1] == "sample":
        os.makedirs("voice_samples", exist_ok=True)
        for name, vid in VOICES.items():
            tts(sys.argv[2], vid, os.path.join("voice_samples", f"{name}.mp3"))
            print("voice_samples/" + name + ".mp3")
    else:
        sys.exit(__doc__)
