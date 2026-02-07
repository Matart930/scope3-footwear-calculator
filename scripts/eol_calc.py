import pandas as pd

bom = pd.read_csv("../data/bom.csv")
eol = pd.read_csv("../data/eol.csv")
factors = pd.read_csv("../data/eol_factors.csv")

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

result.to_csv("../outputs/eol_summary.csv", index=False)

print(result)