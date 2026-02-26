"""Test the full webhook flow with a real query"""
import requests
from urllib.parse import urlencode
import time

GRAPHRAG_ENDPOINT = "https://n8n.srv986677.hstgr.cloud/webhook/d5960b8c-7caa-43fb-b4b4-7e4cda6b7595"

test_query = "Hello, can you tell me about electrical maintenance?"
print(f"Sending query to webhook: '{test_query}'")
print("This will trigger: Webhook -> AI Agent -> Respond to Webhook")
print("Waiting up to 60 seconds...\n")

# Use the query parameter name that matches what the webhook expects
params = {"query": test_query}
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

    if response.status_code == 200:
        if len(response.text) > 10:
            print("\n[SUCCESS] Got a response from AI!")
        else:
            print("\n[WARNING] Response is too short or empty")
            print("Check your 'Respond to Webhook' node configuration")
    else:
        print(f"\n[ERROR] HTTP {response.status_code}")

except requests.Timeout:
    print("\n[TIMEOUT] Request took longer than 60 seconds")
    print("The AI Agent might be taking too long to process")

except Exception as e:
    print(f"\n[ERROR] {e}")
