import pandas as pd
import os

# ----------------------------------------------------
# Path setup
# ----------------------------------------------------
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

DATA_DIR = os.path.join(BASE_DIR, "data")
OUTPUT_DIR = os.path.join(BASE_DIR, "outputs")

# ----------------------------
# Load data
# ----------------------------
use = pd.read_csv(os.path.join(DATA_DIR, "use_phase.csv"))
grid = pd.read_csv(os.path.join(DATA_DIR, "electricity.csv"))

# assume US electricity
factor = grid.loc[grid["region"] == "US", "kgco2_per_kwh"].values[0]

use["emissions_kgco2"] = use["washes"] * use["kwh_per_wash"] * factor

# ----------------------------
# Save
# ----------------------------
use.to_csv(os.path.join(OUTPUT_DIR, "use_phase_summary.csv"), index=False)

print(use)