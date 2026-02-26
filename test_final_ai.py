"""Final test for n8n AI with Respond to Webhook"""
import requests
from urllib.parse import urlencode

GRAPHRAG_ENDPOINT = "https://n8n.srv986677.hstgr.cloud/webhook/d5960b8c-7caa-43fb-b4b4-7e4cda6b7595"

test_query = "What is 2+2?"
print(f"Testing AI with query: '{test_query}'")
print("This should now return the actual AI response!\n")

params = {"query": test_query}
url = f"{GRAPHRAG_ENDPOINT}?{urlencode(params)}"

response = requests.get(url, timeout=60)

print(f"Status: {response.status_code}")
print(f"\nResponse:")
print(response.text)

if response.status_code == 200:
    print("\n✅ SUCCESS! AI is responding!")
else:
    print("\n❌ Still need to add 'Respond to Webhook' node")
