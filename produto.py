from abc import ABC, abstractmethod

class Produto(ABC):
    def __init__(self, modelo, cor, preco, categoria):
        self._modelo = modelo
        self._cor = cor
        self._preco = preco
        self._categoria = categoria

    def getInformacoes(self):
        return f"Modelo: {self._modelo}, Cor: {self._cor}, Preço: {self._preco}, Categoria: {self._categoria.get_nome()}"

    @abstractmethod
    def cadastrar(self):
        pass

    # Getters e Setters
    def get_modelo(self):
        return self._modelo

    def set_modelo(self, modelo):
        self._modelo = modelo

    def get_cor(self):
        return self._cor

    def set_cor(self, cor):
        self._cor = cor

    def get_preco(self):
        return self._preco

    def set_preco(self, preco):
        self._preco = preco

    def get_categoria(self):
        return self._categoria

    def set_categoria(self, categoria):
        self._categoria = categoria