from modelos.veiculo import Veiculo

class Carro(Veiculo):
    def __init__(self, marca: str, modelo: str, cor: str):
        super().__init__(marca, modelo)
        self._cor = cor
        
    def ligar(self):
        return f"O carro {self._marca} {self._modelo} de cor {self._cor} está ligado."