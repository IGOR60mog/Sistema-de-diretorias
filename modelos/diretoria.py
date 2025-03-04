import json
from crud import *


class Diretoria:
    def __init__(self, id, n, f, e):
        self.__id = id
        self.__nome = n
        self.__finalidade = f
        self.__email = e

        self.set_id(id)
        self.set_nome(n)
        self.set_finalidade(f)
        self.set_email(e)

    def set_id(self, id):
      self.__id = id 
    def set_nome (self, n):
      if n == "": raise ValueError("Nome vazio!")
      else: self.__nome = n
    def set_finalidade(self, f):
        if f == "": raise ValueError("Finalidade vazia!")
        else: self.__finalidade = f
    def set_email(self, e):
        if e == "": raise ValueError("Email vazio!")
        else: self.__email = e

    def get_id(self): return self.__id
    def get_nome(self): return self.__nome
    def get_finalidade(self): return self.__finalidade
    def get_email(self): return self.__email
    
    def to_json(self):
       dic = {}
       dic["id"] = self.__id
       dic["nome"] = self.__nome
       dic["finalidade"] = self.__finalidade
       dic["email"] = self.__email
       return dic
       
    def __str__(self):
        return f"id - {self.__id}, nome - {self.__nome}, finalidade - {self.__finalidade}, email - {self.__email}"
    
class Diretorias (CRUD):
  @classmethod
  def salvar(cls):
    with open("Diretorias.json", mode="w") as arquivo:   # w - write
      json.dump(cls.objetos, arquivo, default = Diretoria.to_json)

  @classmethod
  def abrir(cls):
    cls.objetos = []
    try:
      with open("Diretorias.json", mode="r") as arquivo:   # r - read
        texto = json.load(arquivo)
        for obj in texto:   
          c = Diretoria(obj["id"], obj["nome"], obj["finalidade"], obj["email"])
          cls.objetos.append(c)
    except FileNotFoundError:
      pass   