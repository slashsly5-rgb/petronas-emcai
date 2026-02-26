"""Test n8n GraphRAG AI endpoint with GET request"""
import requests
import json
from urllib.parse import urlencode

GRAPHRAG_ENDPOINT = "https://n8n.srv986677.hstgr.cloud/webhook/d5960b8c-7caa-43fb-b4b4-7e4cda6b7595"

print("Testing n8n GraphRAG AI endpoint with GET...")
print(f"URL: {GRAPHRAG_ENDPOINT}\n")

# Test query
test_query = "Hello, can you hear me?"

print(f"Sending test query: '{test_query}'")
print("Waiting for response...\n")

try:
    # Try GET with query parameter
    params = {"query": test_query}
    url_with_params = f"{GRAPHRAG_ENDPOINT}?{urlencode(params)}"

    print(f"Full URL: {url_with_params}\n")

    response = requests.get(url_with_params, timeout=30)

    print(f"Status Code: {response.status_code}")
    print(f"Response Headers: {dict(response.headers)}\n")

    if response.status_code == 200:
        print("[SUCCESS] AI endpoint is working with GET!")
        print(f"\nRaw Response:")
        print(response.text[:500])  # First 500 chars

        try:
            result = response.json()
            print(f"\nResponse JSON:")
            print(json.dumps(result, indent=2))
        except:
            print("\n(Response is not JSON)")

    else:
        print(f"[ERROR] Received status code {response.status_code}")
        print(f"Response: {response.text}")

except requests.exceptions.Timeout:
    print("[ERROR] Request timed out (>30 seconds)")

except Exception as e:
    print(f"[ERROR] {str(e)}")
    print(f"Error type: {type(e).__name__}")

print("\n" + "="*60)
print("Test complete!")
