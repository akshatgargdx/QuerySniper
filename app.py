
from flask import Flask, request, jsonify
from flask_cors import CORS  
from urllib.parse import urlparse, parse_qs, urljoin
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)
CORS(app)  


ERROR_PAYLOADS = ["'", "\"", "'--", "\"--", "' OR '1'='1", "\" OR \"1\"=\"1"]
BOOLEAN_PAYLOADS = [
    ("1 AND 1=1", "1 AND 1=2"),
    ("1' AND '1'='1", "1' AND '1'='2"),
]

ERROR_SIGNATURES = [
    "you have an error in your sql syntax",
    "unclosed quotation mark",
    "mysql_fetch",
    "sqlstate",
    "pg_query",
    "syntax error"
]

def is_vulnerable(response_text):
    return any(error.lower() in response_text.lower() for error in ERROR_SIGNATURES)

def inject_payload(url, payload):
    parsed = urlparse(url)
    query = parse_qs(parsed.query)
    new_query = {k: [v[0] + payload] for k, v in query.items()}
    new_query_str = "&".join([f"{k}={v[0]}" for k, v in new_query.items()])
    return f"{parsed.scheme}://{parsed.netloc}{parsed.path}?{new_query_str}"

def scan_url(url):
    findings = []
    try:
        if "?" in url:
            for payload in ERROR_PAYLOADS:
                test_url = inject_payload(url, payload)
                res = requests.get(test_url, timeout=10)
                if is_vulnerable(res.text):
                    findings.append({
                        "url": test_url,
                        "payload": payload,
                        "type": "Error-Based SQLi"
                    })

            for true_payload, false_payload in BOOLEAN_PAYLOADS:
                url_true = inject_payload(url, true_payload)
                url_false = inject_payload(url, false_payload)
                res_true = requests.get(url_true, timeout=10)
                res_false = requests.get(url_false, timeout=10)
                if len(res_true.text) != len(res_false.text):
                    findings.append({
                        "url": url_true,
                        "payload": f"{true_payload} / {false_payload}",
                        "type": "Boolean-Based SQLi"
                    })
    except:
        pass
    return findings

def crawl(base_url):
    found_links = []
    try:
        response = requests.get(base_url, timeout=10)
        soup = BeautifulSoup(response.text, "html.parser")
        for a in soup.find_all("a", href=True):
            link = urljoin(base_url, a['href'])
            if base_url in link and "?" in link:
                found_links.append(link)
    except:
        pass
    return found_links

@app.route("/scan", methods=["POST"])
def scan():
    url = request.json.get("url")
    if not url:
        return jsonify({"error": "Missing URL"}), 400

    links = crawl(url)
    results = []
    for link in links:
        results.extend(scan_url(link))
    return jsonify(results)

if __name__ == "__main__":
    app.run(debug=True)
