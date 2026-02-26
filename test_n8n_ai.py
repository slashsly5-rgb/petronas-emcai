"""Test n8n GraphRAG AI endpoint connection"""
import requests
import json

GRAPHRAG_ENDPOINT = "https://n8n.srv986677.hstgr.cloud/webhook/d5960b8c-7caa-43fb-b4b4-7e4cda6b7595"

print("Testing n8n GraphRAG AI endpoint...")
print(f"URL: {GRAPHRAG_ENDPOINT}\n")

# Test query
test_query = "Hello, can you hear me?"

print(f"Sending test query: '{test_query}'")
print("Waiting for response...\n")

try:
    response = requests.post(
        GRAPHRAG_ENDPOINT,
        json={"query": test_query},
        timeout=30
    )

    print(f"Status Code: {response.status_code}")
    print(f"Response Headers: {dict(response.headers)}\n")

    if response.status_code == 200:
        result = response.json()
        print("[SUCCESS] AI endpoint is working!")
        print(f"\nResponse JSON:")
        print(json.dumps(result, indent=2))

        # Try to extract the actual response
        if isinstance(result, dict):
            if 'response' in result:
                print(f"\n[OK] AI Response: {result['response']}")
            elif 'answer' in result:
                print(f"\n[OK] AI Answer: {result['answer']}")
            elif 'output' in result:
                print(f"\n[OK] AI Output: {result['output']}")
            else:
                print(f"\n[OK] AI said: {result}")
        else:
            print(f"\n[OK] AI said: {result}")
    else:
        print(f"[ERROR] Received status code {response.status_code}")
        print(f"Response: {response.text}")

        # Try to parse error message
        try:
            error_json = response.json()
            print(f"\nError details:")
            print(json.dumps(error_json, indent=2))
        except:
            pass

except requests.exceptions.Timeout:
    print("[ERROR] Request timed out (>30 seconds)")
    print("The AI endpoint might be slow or unavailable")

except requests.exceptions.ConnectionError:
    print("[ERROR] Could not connect to n8n server")
    print("Check if the URL is correct and the server is accessible")

except Exception as e:
    print(f"[ERROR] {str(e)}")
    print(f"Error type: {type(e).__name__}")

print("\n" + "="*60)
print("Test complete!")
