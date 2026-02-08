import pandas as pd
import os

# ----------------------------------------------------
# Path setup
# ----------------------------------------------------
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

DATA_DIR = os.path.join(BASE_DIR, "data")
OUTPUT_DIR = os.path.join(BASE_DIR, "outputs")

# ----------------------------
# Load all stages
# ----------------------------
materials = pd.read_csv(os.path.join(OUTPUT_DIR, "materials_summary.csv"))
transport = pd.read_csv(os.path.join(OUTPUT_DIR, "transport_summary.csv"))
use = pd.read_csv(os.path.join(OUTPUT_DIR, "use_phase_summary.csv"))
eol = pd.read_csv(os.path.join(OUTPUT_DIR, "eol_summary.csv"))
vol = pd.read_csv(os.path.join(DATA_DIR, "volumes.csv"))

# ----------------------------
# Merge everything
# ----------------------------
df = materials.merge(transport, on="product_id")
df = df.merge(use[["product_id", "emissions_kgco2"]], on="product_id")
df = df.merge(eol, on="product_id")

df.columns = [
    "product_id",
    "materials",
    "transport",
    "use",
    "eol"
]

df["total_per_pair"] = df[["materials", "transport", "use", "eol"]].sum(axis=1)

# ----------------------------
# Multiply by production volume
# ----------------------------
df = df.merge(vol, on="product_id")

df["total_company_kgco2"] = df["total_per_pair"] * df["pairs"]

# ----------------------------
# Save
# ----------------------------
df.to_csv(os.path.join(OUTPUT_DIR, "final_footprint.csv"), index=False)

print(df)