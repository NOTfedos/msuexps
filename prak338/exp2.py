import pandas as pd
from uncertainties import unumpy, ufloat


data = pd.read_csv("./datadir/coefs.csv")

s_Cu = 60
A_Cu = ufloat(data[data["Mater"] == "Cu"]["A"].values[0], data[data["Mater"] == "Cu"]["sA"].values[0])


for index, row in data.iterrows():
    print(row["Mater"], ufloat(row["A"], row["sA"]) / A_Cu * s_Cu)
