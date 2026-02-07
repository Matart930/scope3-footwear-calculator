import pandas as pd

use = pd.read_csv("../data/use_phase.csv")
grid = pd.read_csv("../data/electricity.csv")

# assume US electricity
factor = grid.loc[grid["region"] == "US", "kgco2_per_kwh"].values[0]

use["emissions_kgco2"] = use["washes"] * use["kwh_per_wash"] * factor

use.to_csv("../outputs/use_phase_summary.csv", index=False)

print(use)