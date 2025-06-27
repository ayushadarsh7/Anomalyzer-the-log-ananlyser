# Auto Boot Log Analysis using OpenMP + PCRE + LLM (with cron integration)

This project automatically analyzes Linux system boot logs using a combination of:

- OpenMP-parallelized C log parsers
- PCRE-based rule matching
- LLM-based interpretation (via Hugging Face API)
- Desktop notification upon completion

It is triggered on every system boot and produces a human-readable summary of boot-time issues.

---

##  Structure

├── get_logs.sh # Extracts current boot log using journalctl
├── parallel/ # OpenMP+PCRE parallel C log analyzers & parsers
├── llm_interpreter/ # Python LLM-based explanation engine
├── final_results.txt # Human-readable summary output
├── start_pipeline.sh # Master script (runs all components)
└── README.md

---

## Manual Use
### Step 1: Creating a Hugging-face token
```bash
cd llm_interpreter
nano .env
add your huggingface token here
```
- if you don't have one, you can generate one at : https://huggingface.co/settings/tokens

### Step 2: running the script 
You can run the full log analysis manually with:

```bash
./start_pipeline.sh
```
This script will:
- Wait 60 seconds for system and internet to stabilize

- Extract current boot logs via journalctl

- Run OpenMP-parallelized C parser to detect anomalies

- Use an LLM via Hugging Face API to generate natural-language explanations

- Notify the user with a desktop popup:
    ✅ “Boot Log Analysis Complete — final_results.txt is ready to view.”

## Auto-Run on System Boot
### Step 1: Make your startup script executable
```bash
chmod +x start_pipeline.sh
```
### Step 2: Open your user’s crontab
```bash
crontab -e
```
### Step 3: Add this line at the bottom
```bash
@reboot .......root/start_pipeline.sh
```
### Permissions Tip
- Ensure your user has permission to run journalctl on boot:
- Add your user to the systemd-journal group:
```bash
sudo usermod -aG systemd-journal $USER
```
