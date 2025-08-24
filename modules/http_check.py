import requests
from urllib.parse import urlparse, parse_qs, urlencode, urlunparse

# Common payloads for SQLi and XSS
SQLI_PAYLOADS = ["' OR 1=1--", "\" OR \"1\"=\"1\"", "';--"]
XSS_PAYLOADS = ["<script>alert(1)</script>", "\"'><img src=x onerror=alert(2)>"]

DB_ERRORS = [
    "You have an error in your SQL syntax;",
    "Warning: mysql_fetch",
    "Unclosed quotation mark after the character string",
    "quoted string not properly terminated",
    "Internal Server Error"
]

def check_http_vulnerabilities(target_url):
    print(f"Checking HTTP vulnerabilities on {target_url}...")
    results = {
        "sql_injection": [],
        "xss": []
    }
    # Parse URL and parameters
    parsed = urlparse(target_url)
    params = parse_qs(parsed.query)
    
    if not params:
        return {"error": "No parameters to test in URL."}
    
    # For each parameter, inject SQLI payloads
    print(f"Testing SQL Injection vulnerabilities...")
    for param in params:
        for payload in SQLI_PAYLOADS:
            test_params = params.copy()
            test_params[param] = [payload]  # Assign as list for urlencode compatibility
            test_query = urlencode(test_params, doseq=True)
            test_url = urlunparse(parsed._replace(query=test_query))
            try:
                resp = requests.get(test_url, timeout=5)
                for err in DB_ERRORS:
                    if err.lower() in resp.text.lower():
                        results["sql_injection"].append({
                            "parameter": param,
                            "payload": payload,
                            "url": test_url
                        })
            except Exception as e:
                continue

    # For each parameter, inject XSS payloads
    print(f"Testing XSS vulnerabilities...")
    for param in params:
        for payload in XSS_PAYLOADS:
            test_params = params.copy()
            test_params[param] = [payload]  # Assign as list for urlencode compatibility
            test_query = urlencode(test_params, doseq=True)
            test_url = urlunparse(parsed._replace(query=test_query))
            try:
                resp = requests.get(test_url, timeout=5)
                if payload in resp.text:
                    results["xss"].append({
                        "parameter": param,
                        "payload": payload,
                        "url": test_url
                    })
            except Exception as e:
                continue

    return results
