from loader import load_excel
from analyzer import analyze
from report import generate_report


def print_results(results: dict) -> None:
    print("\n📊 Análise de dados no Excel")
    print("=" * 40)

    for column, stats in results.items():
        print(f"\nColuna: {column}")
        print("-" * 40)

        for key, value in stats.items():
            print(f"{key.capitalize():<10}: {value:.2f}")


def main():
    file_path = "data/sample_pt.xlsx"
    report_path = "reports/rel_excel.txt"

    try:
        df = load_excel(file_path)
        results = analyze(df)

        print_results(results)
        generate_report(results, report_path)

        print(f"\n📄 Relatório gerado em: {report_path}")

    except Exception as error:
        print(f"❌ Erro: {error}")


if __name__ == "__main__":
    main()
