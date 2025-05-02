import requests

url = "http://127.0.0.1:8000/ask"
payload = {
    "prompt": "Hello AI!"
}

print(f"🔄 Sending request to {url} with payload: {payload}")

try:
    response = requests.post(url, json=payload)
    response.raise_for_status()
    print("✅ Response from API:")
    print(response.json())
except requests.exceptions.RequestException as e:
    print("❌ Request failed:")
    print(e)

