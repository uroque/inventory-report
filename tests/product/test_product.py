from inventory_report.inventory.product import Product


def test_cria_produto():
    product = Product(
        1,
        "Pasta de amendoim",
        "Amenduim",
        "2022/10/30",
        "2023/10/30",
        "00000001",
        "Ao abrigo de luz solar"
    )

    assert product.id == 1
    assert product.nome_do_produto == "Pasta de amendoim"
    assert product.nome_da_empresa == "Amenduim"
    assert product.data_de_fabricacao == "2022/10/30"
    assert product.data_de_validade == "2023/10/30"
    assert product.numero_de_serie == "00000001"
    assert product.instrucoes_de_armazenamento == "Ao abrigo de luz solar"
