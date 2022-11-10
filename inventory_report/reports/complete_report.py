from inventory_report.reports.simple_report import SimpleReport
from collections import Counter


class CompleteReport(SimpleReport):
    @classmethod
    def products_stocked_by_company(cls, products_list: list) -> str:
        products_count = Counter(
            [product["nome_da_empresa"] for product in products_list]
        ).most_common()

        message = ""

        for company, count in products_count:
            message += f"- {company}: {count}\n"

        return message

    @classmethod
    def generate(cls, products_list: list) -> str:
        return (
            super().generate(products_list)
            + f"\nProdutos estocados por empresa:\n"
            f"{cls.products_stocked_by_company(products_list)}"
        )
