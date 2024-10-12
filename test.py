import requests
import re

def check_with_google_safe_browsing(api_key, url):
    safe_browsing_url = "https://safebrowsing.googleapis.com/v4/threatMatches:find"
    payload = {
        "client": {
            "clientId": "yourcompanyname",
            "clientVersion": "1.0"
        },
        "threatInfo": {
            "threatTypes": ["MALWARE", "SOCIAL_ENGINEERING"],
            "platformTypes": ["ANY_PLATFORM"],
            "threatEntryTypes": ["URL"],
            "threatEntries": [{"url": url}]
        }
    }

    params = {'key': api_key}
    response = requests.post(safe_browsing_url, json=payload, params=params)

    if response.status_code == 200:
        result = response.json()
        if 'matches' in result:
            return "URL is unsafe according to Google Safe Browsing."
        else:
            return "URL is safe according to Google Safe Browsing."
    else:
        return f"Error: {response.status_code}"


def check_with_virustotal(api_key, url):
    vt_url = "https://www.virustotal.com/vtapi/v2/url/report"
    params = {'apikey': api_key, 'resource': url}
    response = requests.get(vt_url, params=params)

    if response.status_code == 200:
        result = response.json()
        if result['response_code'] == 1:
            # Отображение детализированной информации о результатах сканирования
            positives = result.get('positives', 0)
            total = result.get('total', 0)
            if positives > 0:
                return f"URL is flagged as malicious by {positives} out of {total} sources."
            else:
                return "URL is safe according to VirusTotal."
        else:
            return "URL not found in VirusTotal database."
    else:
        return f"Error: {response.status_code}"


def check_url(url, google_api_key, vt_api_key):
    results = []

    # Проверка с Google Safe Browsing
    gs_result = check_with_google_safe_browsing(google_api_key, url)
    results.append(gs_result)

    # Проверка с VirusTotal
    vt_result = check_with_virustotal(vt_api_key, url)
    results.append(vt_result)

    # Дополнительные проверки структуры URL
    if not url.startswith("https://"):
        results.append("URL is not using HTTPS, which could indicate a security risk.")

    if contains_suspicious_chars(url):
        results.append("URL contains suspicious characters, possibly a phishing attempt.")

    return "\n".join(results)

def contains_suspicious_chars(url):
    suspicious_patterns = [r'\.\.', r'@', r'%', r'!', r'\.exe', r'\\']
    for pattern in suspicious_patterns:
        if re.search(pattern, url):
            return True
    return False

url_to_check = "http://example.com"
status = check_url(url_to_check)
print(status)