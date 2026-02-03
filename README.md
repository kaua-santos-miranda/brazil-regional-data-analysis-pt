# Análise Econômica e Demográfica Regional do Brasil

## Visão Geral
Este projeto realiza uma análise de dados econômicos e demográficos com foco no Brasil, combinando dados de PIB em nível estadual e dados populacionais de regiões geográficas intermediárias da Região Sul do país.

O projeto foi desenvolvido para fins de portfólio, com ênfase em organização de código, uso de dados do mundo real e aplicação de técnicas adequadas de visualização de dados.

---

## Objetivos
- Analisar a evolução do PIB dos estados brasileiros entre 2002, 2010 e 2023
- Identificar:
  - Os 10 estados com maior crescimento percentual do PIB
  - Os 10 estados com os maiores valores absolutos de PIB
  - Os 10 estados com menor crescimento percentual do PIB
- Analisar a distribuição populacional das regiões geográficas intermediárias da Região Sul
- Apresentar os resultados por meio de visualizações estáticas e interativas

---

## Fontes de Dados
- Dados de PIB: Wikipedia / IBGE (Instituto Brasileiro de Geografia e Estatística)
- Dados populacionais: IBGE – Regiões Geográficas Intermediárias (divisão de 2017)

Todos os conjuntos de dados foram organizados manualmente e normalizados para garantir consistência entre os anos e as regiões analisadas.

O arquivo `sample.xlsx` contém dados fictícios e é utilizado apenas para fins de demonstração e testes. Ele não faz parte dos conjuntos de dados reais analisados no projeto.

---

## Tecnologias Utilizadas
- Python 3.10+
- pandas
- matplotlib
- plotly
- openpyxl

---

## Visualizações

### Análise do PIB
- Gráfico de barras: Top 10 maiores crescimentos percentuais do PIB (2002–2023)
- Gráfico de linhas: Tendência do PIB dos 10 maiores estados
- Gráfico de barras: Top 10 menores crescimentos percentuais do PIB

### Análise Populacional (Região Sul)
- Gráfico de pizza: Distribuição populacional das 10 regiões geográficas intermediárias mais populosas
- Gráfico sunburst (interativo): Hierarquia populacional por estado e região intermediária

---

## Estrutura do Projeto


excel-data-analyzer/
│
├── data/
│ ├── gdp_br_states_evolution.xlsx
│ ├── south_br_pop_geog_reg_2022.xlsx
│ ├── south_br_pop_geog_reg_sun_2022.xlsx
│ └── sample.xlsx
│
├── reports/
│ ├── .gitkeep
│ └── excel_analysis_report.txt
│
├── analyzer.py
├── evolution_states_gdp.py
├── loader.py
├── main.py
├── report.py
├── south_br_pop.py
├── south_br_pop_sunburst.py
├── README.md

---


## Como Executar o Projeto

### Instalar as dependências

pip install pandas matplotlib plotly openpyxl

### Executar a análise principal

python main.py

### Executar a análise de evolução do PIB

python evolution_states_gdp.py

### Executar a análise populacional (gráfico de pizza)

python south_br_pop.py

### Executar a análise populacional (sunburst)

python south_br_pop_sunburst.py

---

## Principais Insights
- Valores absolutos elevados de PIB não implicam necessariamente maior crescimento relativo
- Estados com economias menores podem apresentar maior crescimento percentual ao longo do tempo
- A população da Região Sul está fortemente concentrada em grandes centros urbanos
- A escolha adequada do tipo de visualização melhora a clareza da análise

---

## Observações
- Visualizações interativas podem levar alguns segundos para serem renderizadas
- Gráficos sunburst são gerados com Plotly e renderizados localmente
- Os nomes das colunas são padronizados para evitar inconsistências entre diferentes fontes de dados

---

## Melhorias Futuras
- Análise de PIB per capita
- Agregação regional por macrorregiões do Brasil
- Ingestão automática de dados
- Integração com dashboards

---

## Licença
Este projeto é destinado a fins educacionais e de portfólio.
