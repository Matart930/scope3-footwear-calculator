# 1. Get latest data from GitHub
git pull

# 2. Run all calculation steps
python scripts/materials_calc.py
python scripts/transport_calc.py
python scripts/use_phase_calc.py
python scripts/eol_calc.py
python scripts/final_footprint.py

# 3. Push updated results
git add outputs/*.csv
git commit -m "Auto update after factor change"
git push