import requests

def fetch_certificates(domain, include_expired=False):
    url = f"https://crt.sh/json?identity={domain}"
    if not include_expired:
        url += "&exclude=expired"

    response = requests.get(url)
    response.raise_for_status()
    return response.json()