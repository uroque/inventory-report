from collections import Counter


class SimpleReport:
    @classmethod
    def get_oldest_product(cls, products_list):
        dates = [product["data_de_fabricacao"] for product in products_list]
        oldest = min(dates)
        return oldest

    @classmethod
    def get_nearest_expiring_product(cls, products_list):
        dates = [product["data_de_validade"] for product in products_list]
        expiring = min(dates)
        return expiring

    @classmethod
    def get_company_bigger_stock(cls, products_list):
        companies = [product[
            "nome_da_empresa"
        ] for product in products_list]
        sum = Counter(companies)
        return sum.most_common(1)[0][0]

    @classmethod
    def generate(cls, products_list) -> str:
        older = SimpleReport.get_oldest_product(products_list)
        nearest_expiring = SimpleReport.get_nearest_expiring_product(
            products_list
        )
        bigger_stock_company = SimpleReport.get_company_bigger_stock(
            products_list
        )

        return (
            f"Data de fabricação mais antiga: {older}\n"
            f"Data de validade mais próxima: {nearest_expiring}\n"
            f"Empresa com mais produtos: {bigger_stock_company}"
        )
