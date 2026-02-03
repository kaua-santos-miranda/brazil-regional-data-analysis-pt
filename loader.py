import pandas as pd


def load_excel(file_path: str) -> pd.DataFrame:
    """
    Carrega um arquivo Excel (.xlsx) e retorna um DataFrame do pandas.
    """

    try:
        df = pd.read_excel(file_path, engine="openpyxl")

        if df.empty:
            raise ValueError("O arquivo Excel está vazio.")

        return df

    except FileNotFoundError:
        raise FileNotFoundError(f"Arquivo não encontrado: {file_path}")

    except ValueError:
        raise

    except Exception as error:
        raise RuntimeError(f"Erro na leitura do arquivo Excel: {error}")
