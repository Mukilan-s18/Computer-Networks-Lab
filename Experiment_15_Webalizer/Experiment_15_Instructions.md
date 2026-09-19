# Experiment 15: Web Log Analysis using Webalizer

## Objective
Analyze different types of web logs using the Webalizer tool.

## Dataset
A synthetic `access.log` file has been generated in this directory for analysis. It contains simulated HTTP requests in the Common Log Format.

## Instructions for Webalizer
1. **Download & Install**: Download the Webalizer windows/linux version from the official website.
2. **Input Log File**: Specify the `access.log` file generated in this folder as the input.
3. **Run Webalizer**: Execute the tool from the command line:
   ```bash
   webalizer -c webalizer.conf access.log
   ```
4. **Analyze Output**:
   - Webalizer generates HTML reports in the output directory.
   - Open `index.html` in a web browser.
   - Review the Monthly Statistics, Hits by Response Code, Top URLs, and Top User Agents charts.
