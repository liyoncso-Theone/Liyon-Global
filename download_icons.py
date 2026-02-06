import urllib.request
import os

ICONS = {
    "n8n": "https://cdn.simpleicons.org/n8n",
    "openai": "https://cdn.simpleicons.org/openai",
    "python": "https://cdn.simpleicons.org/python",
    "docker": "https://cdn.simpleicons.org/docker",
    "anthropic": "https://cdn.simpleicons.org/anthropic",
    "google": "https://cdn.simpleicons.org/google",
    "googlegemini": "https://cdn.simpleicons.org/googlegemini"
}

TARGET_DIR = "images/icons"
os.makedirs(TARGET_DIR, exist_ok=True)

def download_icon(name, url):
    try:
        req = urllib.request.Request(
            url, 
            data=None, 
            headers={
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
            }
        )
        with urllib.request.urlopen(req) as response:
            if response.status == 200:
                file_path = f"{TARGET_DIR}/{name}.svg"
                with open(file_path, "wb") as f:
                    f.write(response.read())
                print(f"Downloaded {name}")
                return True
            else:
                print(f"Failed to download {name}: {response.status}")
                return False
    except Exception as e:
        print(f"Error downloading {name}: {e}")
        return False

print("Starting download...")
for name, url in ICONS.items():
    download_icon(name, url)

# Try xAI / Grok variations
variations = ["grok", "xai"]
for v in variations:
    url = f"https://cdn.simpleicons.org/{v}"
    if download_icon(v, url):
        break
