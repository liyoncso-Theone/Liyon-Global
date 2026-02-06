import urllib.request
import os

TARGET_DIR = "images/icons"
os.makedirs(TARGET_DIR, exist_ok=True)

# OpenAI Path Data (from search result)
OPENAI_PATH = "M22.2819 9.8211a5.9847 5.9847 0 0 0-.5157-4.9108 6.0462 6.0462 0 0 0-6.5098-2.9A6.0651 6.0651 0 0 0 4.9807 4.1818a5.9847 5.9847 0 0 0-3.9977 2.9 6.0462 6.0462 0 0 0 .7427 7.0966 5.98 5.98 0 0 0 .511 4.9107 6.051 6.051 0 0 0 6.5146 2.9001A5.9847 5.9847 0 0 0 13.2599 24a6.0557 6.0557 0 0 0 5.7718-4.2058 5.9894 5.9894 0 0 0"

def create_svg_from_path(name, path_data, viewbox="0 0 24 24"):
    # Using explicit white fill for dark mode compatibility
    svg_content = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="{viewbox}" fill="white">
  <path d="{path_data}" fill-rule="evenodd"/>
</svg>"""
    with open(f"{TARGET_DIR}/{name}.svg", "w") as f:
        f.write(svg_content)
    print(f"Created {name}.svg")

# Create OpenAI Icon
create_svg_from_path("openai", OPENAI_PATH, "0 0 24 24")

# Grok - We will use a text based SVG as a reliable fallback since direct download failed
# and simple icons doesn't have it yet.
GROK_SVG = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor">
  <path d="M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2m-7 3h2v2h-2zm0 4h2v2h-2zm-4-4h2v2H8zm0 4h2v2H8zm-4-4h2v2H4zm0 4h2v2H4zm0 4h2v2H4zm14 4h-2v-2h2zm0-4h-2v-2h2zm0-4h-2v-2h2z"/>
  <text x="50%" y="50%" dy=".3em" text-anchor="middle" font-family="Arial" font-weight="bold" font-size="14">X</text>
</svg>"""

# Actually, let's use a simpler "X" symbol for xAI / Grok for now to be safe and clean
# This is a stylized slash/X similar to xAI
XAI_PATH = "M18.92 6.01C18.72 5.42 18.16 5 17.5 5h-11c-.66 0-1.22.42-1.42 1.01L3 12v8c0 .55.45 1 1 1h1c.55 0 1-.45 1-1v-1h12v1c0 .55.45 1 1 1h1c.55 0 1-.45 1-1v-8l-2.08-5.99zM6.5 16c-.83 0-1.5-.67-1.5-1.5S5.67 13 6.5 13s1.5.67 1.5 1.5S7.33 16 6.5 16zm11 0c-.83 0-1.5-.67-1.5-1.5s.67-1.5 1.5-1.5 1.5.67 1.5 1.5-.67 1.5-1.5 1.5zM5 11l1.5-4.5h11L19 11H5z"
# That was a car icon, wait. Let's make a simple text SVG for "Grok"
GROK_SVG_TEXT = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 40">
  <text x="50" y="25" font-family="Arial, sans-serif" font-weight="bold" font-size="30" text-anchor="middle" fill="white">Grok</text>
</svg>"""

with open(f"{TARGET_DIR}/grok.svg", "w") as f:
    f.write(GROK_SVG_TEXT)
print("Created grok.svg")

