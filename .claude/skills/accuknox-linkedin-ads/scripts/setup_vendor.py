"""Clone the LinkedIn Ads Manager plugin into vendor/ for reference.

    python setup_vendor.py

The plugin has no license, so vendor/ is gitignored and nothing in this skill
copies its text or imports its code. Every script in it needs the LinkedIn
Marketing API, which needs a developer app with Advertising API approval.
"""
import subprocess
from pathlib import Path

URL = "https://github.com/twentworth12/linkedin-ads-manager-plugin"
DEST = Path(__file__).resolve().parent.parent / "vendor" / "linkedin-ads-manager-plugin"

if DEST.exists():
    subprocess.run(["git", "-C", str(DEST), "pull", "--ff-only"], check=True)
else:
    DEST.parent.mkdir(parents=True, exist_ok=True)
    subprocess.run(["git", "clone", "--depth", "1", URL, str(DEST)], check=True)
print("vendor ready at", DEST)
