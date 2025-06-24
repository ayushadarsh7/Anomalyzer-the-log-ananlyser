import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()
HF_TOKEN = os.getenv("hf_token")

API_URL = "https://router.huggingface.co/featherless-ai/v1/chat/completions"
HEADERS = {
    "Authorization": f"Bearer {HF_TOKEN}",
    "Content-Type": "application/json"
}

MODEL = "NousResearch/Hermes-3-Llama-3.1-8B"

def explain_log_line(log_line):
    prompt = f"""
You are a Linux system log interpreter. Answer ONLY the following two questions, nothing else:
1. What happened and what component is affected?
2. What consequences might this have?

Log:
{log_line}
"""
    payload = {
        "model": MODEL,
        "messages": [
            {"role": "system", "content": "You are a helpful Linux system log analyst."},
            {"role": "user", "content": prompt}
        ]
    }

    response = requests.post(API_URL, headers=HEADERS, json=payload)

    if response.status_code != 200:
        print(f"❌ Request failed with status {response.status_code}")
        print(response.text)
        return "[ERROR]"

    try:
        result = response.json()
        return result["choices"][0]["message"]["content"].strip()
    except Exception as e:
        print("⚠️ Failed to parse response:", e)
        print("Raw output:", response.text)
        return "[INVALID RESPONSE]"

def analyze_all_logs(analyzed_logs_dir="../analyzed_logs", output_path="../final_results.txt"):
    if not os.path.exists(analyzed_logs_dir):
        print(f"❌ analyzed_logs directory not found: {analyzed_logs_dir}")
        return

    log_files = [f for f in os.listdir(analyzed_logs_dir) if os.path.isfile(os.path.join(analyzed_logs_dir, f))]
    if not log_files:
        print(f"❌ No log files found in {analyzed_logs_dir}")
        return

    with open(output_path, "w") as out:
        for log_file in log_files:
            file_path = os.path.join(analyzed_logs_dir, log_file)
            with open(file_path, "r") as f:
                lines = [line.strip() for line in f if line.strip()]
            if not lines:
                continue
            out.write(f"\n{'#'*30}\nFile: {log_file}\n{'#'*30}\n")
            for i, line in enumerate(lines, 1):
                print(f"🔎 Interpreting {log_file} line {i}...")
                explanation = explain_log_line(line)
                out.write(f"Log {i}:\n{line}\n\nExplanation:\n{explanation}\n\n{'='*50}\n")
    print(f"\n✅ All results saved to {output_path}")

if __name__ == "__main__":
    analyze_all_logs()
