import json
from crud import *


class Usuario:
    def __init__(self,id, n, t, e, s, cs):
        self.__id = id
        self.__nome = n
        self.__telefone = t
        self.__email = e
        self.__senha = s
        self.__confsenha = cs

        self.set_nome(n)
        self.set_telefone(t)
        self.set_email(e)
        self.set_senha(s)
        self.set_confsenha(cs)

    def set_id(self, id):
      self.__id = id
    def set_nome (self, n):
      if n == "": raise ValueError("Nome vazio!")
      else: self.__nome = n
    def set_telefone(self, t):
        if t == "": raise ValueError("Telefone vazio!")
        else: self.__telefone = t
    def set_email(self, e):
        if e == "": raise ValueError("Email vazio!")
        else: self.__email = e
    def set_senha(self, s):
        if s == "": raise ValueError("Senha vazia!")
        else: self.__senha = s
    def set_confsenha(self, cs):
        if cs == "": raise ValueError("Confirmação de senha vazia!")
        else: self.__confsenha = cs       

    def get_id(self): return self.__id
    def get_nome(self): return self.__nome
    def get_telefone(self): return self.__telefone
    def get_email(self): return self.__email
    def get_senha(self): return self.__senha
    def get_confsenha(self): return self.__confsenha


    def to_json(self):
       dic = {}
       dic["id"] = self.__id
       dic["nome"] = self.__nome
       dic["telefone"] = self.__telefone
       dic["email"] = self.__email
       dic["senha"] = self.__senha
       dic["confsenha"] = self.__confsenha
       return dic

    def __str__(self):
        return f"id - {self.__id}, nome - {self.__nome}, telefone - {self.__telefone}, email - {self.__email}"
    
class Usuarios (CRUD):
  @classmethod
  def salvar(cls):
    with open("usuarios.json", mode="w") as arquivo:
      json.dump(cls.objetos, arquivo, default = Usuario.to_json)

  @classmethod
  def abrir(cls):
    cls.objetos = []
    try:
      with open("usuarios.json", mode="r") as arquivo:  
        texto = json.load(arquivo)
        for obj in texto:   
          c = Usuario(obj["id"], obj["nome"], obj["telefone"], obj["email"], obj["senha"], obj["confsenha"])
          cls.objetos.append(c)
    except FileNotFoundError:
      pass