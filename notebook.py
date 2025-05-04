from cadastro import Produto


class Notebook(Produto):
  def __init__(self, modelo, cor, preco, categoria, tempoDeBateria):
      super().__init__(modelo, cor, preco, categoria)
      self.__tempoDeBateria = tempoDeBateria

  def getInformacoes(self):
      return super().getInformacoes() + f", Tempo de Bateria: {self.__tempoDeBateria}"

  def cadastrar(self):
      print("Notebook cadastrado com sucesso!")

  # Getter e Setter para tempoDeBateria
  def get_tempoDeBateria(self):
      return self.__tempoDeBateria

  def set_tempoDeBateria(self, tempoDeBateria):
      self.__tempoDeBateria = tempoDeBateria