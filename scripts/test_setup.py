import pandas as pd

bom = pd.read_csv("../data/bom.csv")
factors = pd.read_csv("../data/material_factors.csv")

print("BOM loaded:")
print(bom.head())

print("\nFactors loaded:")
print(factors.head())
