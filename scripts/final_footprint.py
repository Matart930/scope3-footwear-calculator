import pandas as pd

materials = pd.read_csv("../outputs/materials_summary.csv")
transport = pd.read_csv("../outputs/transport_summary.csv")
use = pd.read_csv("../outputs/use_phase_summary.csv")
eol = pd.read_csv("../outputs/eol_summary.csv")
vol = pd.read_csv("../data/volumes.csv")

# Merging everything
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

df["total_per_pair"] = df[["materials", "transport","use","eol"]].sum(axis=1)

# Multiply by production volume
df = df.merge(vol, on="product_id")

df["total_company_kgco2"] = df["total_per_pair"] * df["pairs"]

df.to_csv("../outputs/final_footprint.csv", index=False)

print(df)