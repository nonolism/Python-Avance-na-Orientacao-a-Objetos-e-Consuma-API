from modelos.cardapio.item_cardapio import ItemCardapio

class Sobremesa(ItemCardapio):
    def __init__(self, nome: str, preco: float, tipo: str, tamanho: str, descricao: str):
        super().__init__(nome, preco)
        self._tipo = tipo
        self._tamanho = tamanho
        self._descricao = descricao
    
    def __str__(self):
        return f"{self._nome} ({self._tipo}, {self._tamanho}) - {self._descricao}"
    
    def aplicar_desconto(self):
        return self._preco - (self._preco * 0.10)