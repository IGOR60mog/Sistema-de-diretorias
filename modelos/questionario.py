import json
from datetime import datetime
from crud import *


class Questionario:
    def __init__(self,id, idU, d, p, idC):
        self.__id = id
        self.__id_usuario = idU
        self.__data = d
        self.__pontos = p
        self.__id_curso = idC

        self.set_id(id)
        self.set_id_usuario(idU)
        self.set_data(d)
        self.set_pontos(p)

    def set_id(self, id):
      self.__id = id

    def set_id_usuario(self, idU):
       if idU < 0: raise ValueError("Usuário inválido")
       else: self.__id_usuario = idU
      
    def set_data(self, d):
       if d != datetime(1, 1, 1): self.__data = d
       else: raise ValueError("Data inválida")

    def set_pontos(self, p):
       if p >= 0: self.__pontos = p
       else: raise ValueError("Pontuação inválida")

    def set_id_curso(self, idC):
       if idC < 0: raise ValueError("Curso inválido")
       else: self.__id_curso = idC

    def get_id(self): return self.__id
    def get_id_usuario(self): return self.__id_usuario
    def get_data(self): return self.__data
    def get_pontos(self): return self.__pontos
    def get_id_curso(self): return self.__id_curso

    def to_json(self):
       dic = {}
       dic["id"] = self.__id
       dic["id_usuario"] = self.__id_usuario
       dic["data"] = self.__data.strftime("%d/%m/%Y %H:%M:%S") 
       dic["pontos"] = self.__pontos
       dic["curso"] = self.__id_curso
       return dic
    
    def __str__(self):
        return f"id - {self.__id}, usuario - {self.__id_usuario}, data - {self.__data}, pontos - {self.__pontos}, curso - {self.__id_curso}"
    
class Questionarios (CRUD):
  @classmethod
  def salvar(cls):
    with open("questionarios.json", mode="w") as arquivo:   # w - write
      json.dump(cls.objetos, arquivo, default = Questionario.to_json)

  @classmethod
  def abrir(cls):
    cls.objetos = []
    try:
      with open("questionarios.json", mode="r") as arquivo:   # r - read
        texto = json.load(arquivo)
        for obj in texto:   
          data = datetime.strptime(obj["data"], "%d/%m/%Y %H:%M:%S")
          c = Questionario(obj["id"], obj["id_usuario"], data, obj["pontos"], obj["curso"])
          cls.objetos.append(c)
    except FileNotFoundError:
      pass   