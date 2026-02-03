import pandas as pd
import matplotlib.pyplot as plt

# Carregar dados
df = pd.read_excel("data/evolucao_estados_pib_2002_2022.xlsx")

# Define o estado como índice
df.set_index("Estado", inplace=True)

# Calcula o crescimento percentual de 2002 a 2023
df["Growth_%"] = ((df["PIB_2023"] - df["PIB_2002"]) / df["PIB_2002"]) * 100

# TOP 10 CRESCIMENTO_% #

top_10_growth = df.sort_values("Growth_%", ascending=False).head(10)

plt.figure()
top_10_growth["Growth_%"].plot(kind="bar")
plt.title("As 10 maiores taxas de crescimento percentual do PIB (2002–2023)")
plt.xlabel("Estado")
plt.ylabel("Crescimento percentual (%)")
plt.tight_layout()
plt.show()

# TOP 10 PIB #

top_10_gdp = df.sort_values("PIB_2023", ascending=False).head(10)

plt.figure()
for state in top_10_gdp.index:
    plt.plot(
        ["2002", "2010", "2023"],
        [
            top_10_gdp.loc[state, "PIB_2002"],
            top_10_gdp.loc[state, "PIB_2010"],
            top_10_gdp.loc[state, "PIB_2023"],
        ],
        label=state
    )

plt.title("Tendência do PIB dos 10 maiores estados (2002–2023)")
plt.xlabel("Ano")
plt.ylabel("PIB")
plt.legend()
plt.tight_layout()
plt.show()

bottom_10_growth = df.sort_values("Growth_%", ascending=True).head(10)

plt.figure()
bottom_10_growth["Growth_%"].plot(kind="bar")
plt.title("As 10 menores taxas de crescimento percentual do PIB (2002–2023)")
plt.xlabel("Estado")
plt.ylabel("Crescimento percentual (%)")
plt.tight_layout()
plt.show()
