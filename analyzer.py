import pandas as pd


def analyze(df: pd.DataFrame) -> dict:
    """
    Analisa colunas numéricas de um DataFrame do pandas e retorna estatísticas descritivas básicas.

    :param df: DataFrame do pandas carregado de um arquivo Excel
    :return: Dicionário com estatísticas por coluna numérica
    """

    if df.empty:
        raise ValueError("Não há dados disponíveis para análise.")

    # Seleciona apenas colunas númericas
    numeric_df = df.select_dtypes(include="number")

    if numeric_df.empty:
        raise ValueError("Nenhuma coluna numérica foi encontrada no arquivo Excel.")

    results = {}

    for column in numeric_df.columns:
        results[column] = {
            "min": numeric_df[column].min(),
            "max": numeric_df[column].max(),
            "mean": numeric_df[column].mean(),
            "median": numeric_df[column].median(),
            "std": numeric_df[column].std(),
        }

    return results
