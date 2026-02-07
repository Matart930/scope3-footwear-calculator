import pandas as pd

# --------------------------
# 1. Load data
# --------------------------

bom = pd.read_csv("C:/Users/matth/Documents/scope3_calculator/data/bom.csv")
transport = pd.read_csv("C:/Users/matth/Documents/scope3_calculator/data/transport.csv")
factors = pd.read_csv("C:/Users/matth/Documents/scope3_calculator/data/transport_factors.csv")

# --------------------------
# 2. Get product weight in tons
# --------------------------
total_weight_kg = bom["weight_g"].sum() / 1000
weight_tons = total_weight_kg / 1000

# --------------------------
# 3. Join mode factors
# --------------------------
df = transport.merge(factors, on="mode", how="left")

# --------------------------
# 4. Calculate emissions per leg
# --------------------------
df["emissions_kgco2"] = weight_tons * df["distance_km"] * df["kgco2_per_ton_km"]

# --------------------------
# 5. Summarize
# --------------------------
summary = df.groupby("product_id")["emissions_kgco2"].sum().reset_index()

df.to_csv("C:/Users/matth/Documents/scope3_calculator/outputs/transport_detailed.csv", index=False)
summary.to_csv("C:/Users/matth/Documents/scope3_calculator/outputs/transport_summary.csv", index=False)

print(df)
print("\nTotal transport per pair:")
print(summary)