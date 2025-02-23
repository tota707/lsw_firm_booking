import requests
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
LLAMA_API_KEY = os.getenv("LLAMA_API_KEY")

if not LLAMA_API_KEY:
    print("❌ LLAMA_API_KEY is missing! Check your .env file.")
    exit()

# Define API request
url = "https://api.llama.ai/chat"  # Replace with actual Llama API URL
headers = {"Authorization": f"Bearer {LLAMA_API_KEY}", "Content-Type": "application/json"}
data = {
    "model": "llama-2-7b-chat",
    "messages": [{"role": "user", "content": "Hello"}]
}

# Make request
try:
    response = requests.post(url, json=data, headers=headers)
    print("🔄 Testing API connection...")

    if response.status_code == 200:
        print("✅ API is working! Response:", response.json())
    else:
        print(f"❌ API Error! Status Code: {response.status_code}")
        print("Response:", response.text)

except requests.exceptions.RequestException as e:
    print(f"❌ Connection Error: {e}")
