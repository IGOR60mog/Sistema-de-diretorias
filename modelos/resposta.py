import json
from crud import *


class Resposta:
    def __init__(self,id, idP, idQ, r):
        self.__id = id
        self.__id_pergunta = idP
        self.__id_questionario = idQ
        self.__resposta = r

        self.set_id(id)
        self.set_id_pergunta(idP)
        self.set_id_questionario(idQ)
        self.set_resposta(r)
   
    def set_id(self, id):
      self.__id = id 
    def set_id_pergunta(self, idP):
      if idP < 0: raise ValueError("Pergunta inválida!")
      self.__id_pergunta = idP

    def set_id_questionario(self, idQ):
      if idQ < 0: raise ValueError("Questionário inválido!")
      else: self.__id_questionario = idQ

    def set_resposta (self, r):
      if r >= 0: self.__resposta = r
      else: raise ValueError("Resposta inválida")

    def get_id(self): return self.__id
    def get_id_pergunta(self): return self.__id_pergunta
    def get_id_questionario(self): return self.__id_questionario
    def get_resposta(self): return self.__resposta

    def to_json(self):
       dic = {}
       dic["id"] = self.__id
       dic["id_pergunta"] = self.__id_pergunta
       dic["id_questionario"] = self.__id_questionario
       dic["resposta"] = self.__resposta
       return dic
        
    def __str__(self):
        return f"id - {self.__id}, resposta - {self.__id_pergunta}, questionário - {self.__id_questionario}, resposta - {self.__resposta}"
    
class Respostas (CRUD):
  @classmethod
  def salvar(cls):
    with open("respostas.json", mode="w") as arquivo:   # w - write
      json.dump(cls.objetos, arquivo, default = Resposta.to_json)

  @classmethod
  def abrir(cls):
    cls.objetos = []
    try:
      with open("respostas.json", mode="r") as arquivo:   # r - read
        texto = json.load(arquivo)
        for obj in texto:   
          c = Resposta(obj["id"], obj["id_pergunta"], obj["id_questionario"], obj["resposta"])
          cls.objetos.append(c)
    except FileNotFoundError:
      pass   