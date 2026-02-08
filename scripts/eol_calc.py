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
bom = pd.read_csv(os.path.join(DATA_DIR, "bom.csv"))
eol = pd.read_csv(os.path.join(DATA_DIR, "eol.csv"))
factors = pd.read_csv(os.path.join(DATA_DIR, "eol_factors.csv"))

weight_kg = bom["weight_g"].sum() / 1000

row = eol.iloc[0]

emissions = (
    row["landfill"] * factors[factors["method"]=="landfill"]["kgco2_per_kg"].values[0] +
    row["incineration"] * factors[factors["method"]=="incineration"]["kgco2_per_kg"].values[0] +
    row["recycle"] * factors[factors["method"]=="recycle"]["kgco2_per_kg"].values[0]
) * weight_kg

result = pd.DataFrame({
    "product_id": [row["product_id"]],
    "eol_kgco2": [emissions]
})

# ----------------------------
# Save
# ----------------------------
result.to_csv(os.path.join(OUTPUT_DIR, "eol_summary.csv"), index=False)

print(result)