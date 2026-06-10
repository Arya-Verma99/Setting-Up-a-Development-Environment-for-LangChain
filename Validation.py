import os
import sys
from dotenv import load_dotenv

load_dotenv()

print("[INFO] Inspecting Environment...")
print(f"Python Version: {sys.version.split()[0]}")

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    print("[CRITICAL ERROR] GROQ_API_KEY not found.")
    print("-> Check if .env file exists.")
    print("-> Check if variable name matches exactly.")
else:
    masked_key = f"{api_key[:5]}...{api_key[-3:]}"
    print(f"[SUCCESS] API Key Loaded: {masked_key}")
    print("[SYSTEM] Ready for Takeoff.")