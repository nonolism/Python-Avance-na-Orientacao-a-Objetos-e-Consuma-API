from modelos.veiculo import Veiculo

class Carro(Veiculo):
    def __init__(self, marca, modelo, portas: int):
        super().__init__(marca, modelo)
        self._portas = portas
    
    def __str__(self):
        return f'{super().__str__()} | Portas: {self._portas}'