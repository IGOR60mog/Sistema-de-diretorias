import json
from crud import *


class Pergunta:
    def __init__(self, id, idC, c):
        self.__id = id
        self.__id_curso = idC
        self.__conteudo = c
    
        self.set_id(id)
        self.set_id_curso(idC)
        self.set_conteudo(c)

    def set_id(self, id): self.__id = id        
    def set_id_curso (self, idC):
      if idC < 0: raise ValueError("Curso inválido")
      else: self.__id_curso = idC
    def set_conteudo (self, c):
       if c == "": raise ValueError("Conteúdo vazio")
       else: self.__conteudo = c

    def get_id(self): return self.__id
    def get_id_curso(self): return self.__id_curso
    def get_conteudo(self): return self.__conteudo
  
    def to_json(self):
       dic = {}
       dic["id"] = self.__id
       dic["id_curso"] = self.__id_curso
       dic["conteudo"] = self.__conteudo
       return dic
    
    def __str__(self):
        return f"id - {self.__id}, curso - {self.__id_curso}, pergunta - {self.__conteudo}"
    
class Perguntas (CRUD):
  @classmethod
  def salvar(cls):
    with open("perguntas.json", mode="w") as arquivo:   # w - write
      json.dump(cls.objetos, arquivo, default = Pergunta.to_json)

  @classmethod
  def abrir(cls):
    cls.objetos = []
    try:
      with open("perguntas.json", mode="r") as arquivo:   # r - read
        texto = json.load(arquivo)
        for obj in texto:   
          c = Pergunta(obj["id"], obj["id_curso"], obj["conteudo"])
          cls.objetos.append(c)
    except FileNotFoundError:
      pass   