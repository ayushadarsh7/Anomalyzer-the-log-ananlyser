#!/bin/bash

# Change to the working directory
cd /home/ayushadarsh7/openmpcore-self/Log_Analysis/llm_part

# Wait a few seconds to allow for internet connection (adjust as needed)
sleep 60

# Step 1: Get boot log
./get_logs.sh

# Step 2: Compile + run C parallel log parsers
cd parallel
./compile.sh
cd Log_Analyzer
./compile.sh
cd ../..

# Step 3: Run LLM interpreter pipeline (creates final_results.txt)
cd llm_interpreter
./run.sh
cd ..

# Step 4: Open final_results.txt in nano (visible in virtual terminal after login)
# Notify desktop user when done
export DISPLAY=:0
export XDG_RUNTIME_DIR=/run/user/$(id -u)

notify-send "✅ Boot Log Analysis Complete" "final_results.txt is ready to view."
