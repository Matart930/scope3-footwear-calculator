import pandas as pd

# ----------------------------
# 1. Load data
# ----------------------------
bom = pd.read_csv("C:/Users/matth/Documents/scope3_calculator/data/bom.csv")
factors = pd.read_csv("C:/Users/matth/Documents/scope3_calculator/data/material_factors.csv")

# ----------------------------
# 2. Convert grams → kg
# ----------------------------
bom["weight_kg"] = bom["weight_g"] / 1000

# ----------------------------
# 3. Join emission factors
# ----------------------------
df = bom.merge(factors, on="material", how="left")

# ----------------------------
# 4. Calculate emissions
# ----------------------------
df["emissions_kgco2"] = df["weight_kg"] * df["ef_kgco2_per_kg"]

# ----------------------------
# 5. Add scrap rate (8%)
# ----------------------------
SCRAP_RATE = 0.08
df["emissions_with_scrap"] = df["emissions_kgco2"] * (1 + SCRAP_RATE)

# ----------------------------
# 6. Summarize per product
# ----------------------------
summary = df.groupby("product_id")["emissions_with_scrap"].sum().reset_index()

# ----------------------------
# 7. Save results
# ----------------------------
df.to_csv("C:/Users/matth/Documents/scope3_calculator/outputs/materials_detailed.csv", index=False)
summary.to_csv("C:/Users/matth/Documents/scope3_calculator/outputs/materials_summary.csv", index=False)

print("Detailed results:")
print(df)

print("\nPer-pair total:")
print(summary)
