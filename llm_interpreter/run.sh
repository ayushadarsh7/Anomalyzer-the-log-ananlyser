#!/bin/bash

# Exit on error
set -e

# 1. Create virtual environment
echo " Creating virtual environment..."
python3 -m venv .venv

# 2. Activate it
source .venv/bin/activate

# 3. Install required Python packages
echo " Installing required packages..."
pip install requests python-dotenv

# 4. Run the script
echo "🚀 Running log interpretation for all analyzed logs using Hugging Face API..."
python3 llm_analysis.py

echo "✅ Done. Check ../final_results.txt for results."
