import pandas as pd
import plotly.express as px

# Carregar dados
df = pd.read_excel("data/south_br_pop_geog_reg_sun_2022_pt.xlsx")

# Nomes de coluna limpos
df.columns = df.columns.str.strip()

# Classifique e selecione as 10 principais regiões por população
top_10 = df.sort_values("POP_2022", ascending=False).head(10)

fig = px.sunburst(
    top_10,
    path=["ESTADO", "REG"],
    values="POP_2022",
    title=(
        "As 10 regiões geográficas intermediárias mais populosas:\n"
        "Região Sul do Brasil"
    )
)

fig.write_html("reports/south_br_pop_geog_reg_sun_2022_pt.html")
