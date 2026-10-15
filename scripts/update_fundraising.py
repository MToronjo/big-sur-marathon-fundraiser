"""Read Macy's live total from her Haku page and write fundraising-data.json.

The Haku page is server-rendered, so plain HTTP is enough (no browser needed).
Fails loudly and writes nothing if the numbers can't be found.
"""
import html
import json
import re
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

URL = "https://fundraisers.hakuapp.com/fundraisers/7e737b754f559c246316"
OUTPUT = Path(__file__).resolve().parent.parent / "fundraising-data.json"

req = urllib.request.Request(URL, headers={"User-Agent": "Mozilla/5.0 (fundraiser-site updater)"})
with urllib.request.urlopen(req, timeout=30) as resp:
    raw = resp.read().decode("utf-8", "replace")

text = re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", raw)))

def amount(label: str) -> float:
    m = re.search(r"\$\s*([\d,]+(?:\.\d{1,2})?)\s*" + label, text, re.IGNORECASE)
    if not m:
        raise SystemExit(f"Could not find '{label}' amount on the Haku page. Nothing written.")
    return float(m.group(1).replace(",", ""))

payload = {
    "raised": amount("raised"),
    "goal": amount("goal"),
    "updated": datetime.now(timezone.utc).isoformat(),
    "source": URL,
}
OUTPUT.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
print(f"Raised ${payload['raised']:,.2f} of ${payload['goal']:,.2f}")
