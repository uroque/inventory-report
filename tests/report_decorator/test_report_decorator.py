from inventory_report.reports.colored_report import ColoredReport
from inventory_report.reports.simple_report import SimpleReport


def test_decorar_relatorio():
    product = [
        {
            "id": 1,
            "nome_do_produto": "Pasta de amendoim",
            "nome_da_empresa": "Amenduim",
            "data_de_fabricacao": "2022-10-30",
            "data_de_validade": "2023-10-30",
            "numero_de_serie": "00000001",
            "instrucoes_de_armazenamento": "Ao abrigo de luz solar",
        }
    ]

    message = (
        "\033[32mData de fabricação mais antiga:\033[0m"
        " \033[36m2022-10-30\033[0m\n"
        "\033[32mData de validade mais próxima:\033[0m"
        " \033[36m2023-10-30\033[0m\n"
        "\033[32mEmpresa com mais produtos:\033[0m"
        " \033[31mAmenduim\033[0m"
    )

    report = ColoredReport(SimpleReport).generate(product)
    assert message == report
