from inventory_report.inventory.product import Product


def test_relatorio_produto():
    product = Product(
        1,
        "Pasta de amendoim",
        "Amenduim",
        "2022/10/30",
        "2023/10/30",
        "00000001",
        "Ao abrigo de luz solar"
    )

    assert(
        product.__repr__() ==
        f"O produto {product.nome_do_produto}"
        + f" fabricado em {product.data_de_fabricacao}"
        + f" por {product.nome_da_empresa} com validade"
        + f" até {product.data_de_validade}"
        + f" precisa ser armazenado {product.instrucoes_de_armazenamento}."
    )
