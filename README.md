# Scope 3 Footwear Carbon Calculator

## Overview
This Python project calculates the **cradle-to-grave Scope 3 carbon footprint** of footwear products. It models emissions across multiple categories:

- **Materials (Category 1)** – Bill of Materials (BOM) × material emission factors  
- **Transportation (Categories 4 & 9)** – Ton-kilometer method for multimodal logistics  
- **Use Phase (Category 11)** – Washing and electricity usage assumptions  
- **End of Life (Category 12)** – Landfill, incineration, and recycling assumptions  

The project outputs **per-pair and company-level emissions**, and includes a **Google Sheets dashboard** for visualization.

## Run-all Automation
This project includes a **run_all.ps1** file that pulls in all changes to data files from github, recalculates and updates output csv files, and pushes those changes back to github
