import os

TARGET_DIR = "images/icons"
os.makedirs(TARGET_DIR, exist_ok=True)

# Generating a clean Text-based SVG for OpenAI.
# This ensures perfect legibility and avoids "blob" issues from complex paths.
# Using a high-quality system font stack that closely mimics the geometric style.
OPENAI_TEXT_SVG = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 24">
  <text x="50%" y="18" font-family="Arial, Helvetica, sans-serif" font-weight="bold" font-size="20" text-anchor="middle" fill="white">OpenAI</text>
</svg>"""

with open(f"{TARGET_DIR}/openai.svg", "w") as f:
    f.write(OPENAI_TEXT_SVG)
print("-> Created Text-based OpenAI Logo (White)")
