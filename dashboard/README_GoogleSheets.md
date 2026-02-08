# Google Sheets Dashboard (Live from GitHub)

This project uses Google Sheets instead of Excel Power Query.

## How It Works

Google Sheets pulls CSV outputs directly from GitHub using:

=IMPORTDATA("https://raw.githubusercontent.com/Matart930/scope3-footwear-calculator/main/outputs/materials_summary.csv")

## Tabs to Create

- materials  → materials_summary.csv  
- transport  → transport_summary.csv  
- use        → use_phase_summary.csv  
- eol        → eol_summary.csv  
- final      → final_footprint.csv  

## Refresh Logic

Whenever new results are pushed:

git add outputs/*.csv
git commit -m "Update results"
git push

Google Sheets automatically refreshes.
