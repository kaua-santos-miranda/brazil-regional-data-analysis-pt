import pandas as pd
import matplotlib.pyplot as plt

# Carregar dados
df = pd.read_excel("data/south_br_pop_geog_reg_2022_pt.xlsx")

# Nomes de coluna limpos
df.columns = df.columns.str.strip()

# Classifique e selecione os 10 melhores
top_10 = df.sort_values("POP_2022", ascending=False).head(10)

plt.figure()
plt.pie(
    top_10["POP_2022"],
    labels=top_10["REG"],
    autopct="%1.1f%%",
    startangle=90
)
plt.title(
    "As 10 regiões geográficas intermediárias\nmais populosas do sul do Brasil"
)
plt.tight_layout()
plt.show()

explode = [0.1 if p == top_10["POP_2022"].max() else 0 for p in top_10["POP_2022"]]

plt.figure()
plt.pie(
    top_10["POP_2022"],
    labels=top_10["REG"],
    autopct="%1.1f%%",
    startangle=90,
    explode=explode
)
plt.title(
    "As 10 regiões geográficas intermediárias\nmais populosas do sul do Brasil"
)
plt.tight_layout()
plt.show()

