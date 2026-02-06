import urllib.request
import os

TARGET_DIR = "images/icons"
os.makedirs(TARGET_DIR, exist_ok=True)

# Fetching the official 'Black' icon from a reliable CDN.
# Simple Icons default is the brand color, which for OpenAI is often ensuring the correct shape.
# We will NOT modify the content this time.
OPENAI_URL = "https://cdn.simpleicons.org/openai" 

def download_icon(name, url):
    print(f"Fetching {name} from {url}...")
    try:
        req = urllib.request.Request(
            url, 
            headers={'User-Agent': 'Mozilla/5.0'}
        )
        with urllib.request.urlopen(req) as response:
            content = response.read()
            with open(f"{TARGET_DIR}/{name}.svg", "wb") as f:
                f.write(content)
            print(f"-> Saved {name}.svg")
            return True
    except Exception as e:
        print(f"-> Error fetching {name}: {e}")
        return False

download_icon("openai", OPENAI_URL)
