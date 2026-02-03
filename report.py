import os
from datetime import datetime


def generate_report(results: dict, output_path: str) -> None:
    """
    Gera um relatório em formato .txt com os resultados da análise.

    :param results: Dicionário contendo estatísticas por coluna
    :param output_path: Caminho onde o relatório será salvo
    """

    # Certifica de que o diretório de saída exista.
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(output_path, mode="w", encoding="utf-8") as file:
        file.write("Relatório de análise de dados em Excel\n")
        file.write("=" * 40 + "\n")
        file.write(f"Gerado em: {timestamp}\n")

        for column, stats in results.items():
            file.write("\n")
            file.write(f"Coluna: {column}\n")
            file.write("-" * 40 + "\n")

            for key, value in stats.items():
                file.write(f"{key.capitalize():<10}: {value:.2f}\n")
