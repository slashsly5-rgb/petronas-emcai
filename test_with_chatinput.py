"""Test with chatInput parameter instead of query"""
import requests
from urllib.parse import urlencode
import time

GRAPHRAG_ENDPOINT = "https://n8n.srv986677.hstgr.cloud/webhook/d5960b8c-7caa-43fb-b4b4-7e4cda6b7595"

test_query = "What is electrical maintenance?"
print(f"Testing with chatInput parameter: '{test_query}'")
print("Waiting up to 60 seconds...\n")

# Use chatInput instead of query
params = {"chatInput": test_query}
url = f"{GRAPHRAG_ENDPOINT}?{urlencode(params)}"

print(f"Full URL: {url}\n")

start_time = time.time()

try:
    response = requests.get(url, timeout=60)
    elapsed = time.time() - start_time

    print(f"Status: {response.status_code}")
    print(f"Time taken: {elapsed:.2f} seconds")
    print(f"Response length: {len(response.text)} characters\n")

    print("Response content:")
    print("=" * 60)
    print(response.text)
    print("=" * 60)

    if elapsed > 2 and len(response.text) > 20:
        print("\n[SUCCESS] AI is working! Response took time and has content!")
    elif len(response.text) == 0:
        print("\n[WARNING] Empty response - check Respond to Webhook node")
    else:
        print("\n[INFO] Got quick response - might be cached or not running AI")

except Exception as e:
    print(f"\n[ERROR] {e}")
