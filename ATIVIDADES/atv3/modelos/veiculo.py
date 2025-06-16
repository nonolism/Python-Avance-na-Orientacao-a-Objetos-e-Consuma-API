from abc import ABC, abstractmethod

class Veiculo(ABC):
    def __init__(self, marca: str, modelo: str):
        self._marca = marca
        self._modelo = modelo
    
    def __str__(self):
        return f"{self._marca} {self._modelo}"

    @abstractmethod
    def ligar(self):
        pass