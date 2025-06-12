from modelos.cardapio.item_cardapio import ItemCardapio

class Prato(ItemCardapio):
    def __init__(self, nome: str, preco: float, descricao: str):
        """
        Inicializa uma nova instância da classe com nome, preço e descrição.

        Args:
            nome (str): O nome do prato.
            preco (float): O preço do prato.
            descricao (str): A descrição do prato.
        """
        super().__init__(nome, preco)#  Chama o construtor da classe pai 
                                    #   (ItemCardapio) com nome e preço como argumentos.
        self._descricao = descricao
        
    def __str__(self):
        return self._nome
    
    def aplicar_desconto(self):
        self._preco -= (self._preco * 0.05)