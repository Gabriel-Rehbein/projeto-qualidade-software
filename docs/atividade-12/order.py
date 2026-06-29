def calcular_total_pedido(itens, taxa_entrega=0.0):
    total_itens = sum(item["preco"] * item["quantidade"] for item in itens)
    return round(total_itens + taxa_entrega, 2)
