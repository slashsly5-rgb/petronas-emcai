"""Direct test of AI endpoint"""
import requests
from urllib.parse import urlencode
import time

GRAPHRAG_ENDPOINT = "https://n8n.srv986677.hstgr.cloud/webhook/d5960b8c-7caa-43fb-b4b4-7e4cda6b7595"

test_query = "What is 2 plus 2?"
print(f"Testing AI: '{test_query}'")
print("Waiting up to 60 seconds for response...\n")

params = {"query": test_query}
url = f"{GRAPHRAG_ENDPOINT}?{urlencode(params)}"

start_time = time.time()
response = requests.get(url, timeout=60)
elapsed = time.time() - start_time

print(f"Status: {response.status_code}")
print(f"Time taken: {elapsed:.2f} seconds")
print(f"\nResponse:")
print(response.text)
print(f"\nResponse length: {len(response.text)} characters")

if "Workflow was started" in response.text:
    print("\n[WARNING] Still getting async response!")
    print("Please check:")
    print("1. Webhook node 'Respond' = 'Using Respond to Webhook Node'")
    print("2. Workflow is SAVED (Ctrl+S)")
    print("3. Workflow is ACTIVE (green toggle)")
elif len(response.text) > 50:
    print("\n[SUCCESS] Got a real AI response!")
