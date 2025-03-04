from abc import ABC, abstractmethod

# Persistência
class CRUD(ABC):
  objetos = []    # atributo estático

  @classmethod
  def inserir(cls, obj):
    if cls.objetos != []:
        cls.abrir()
        m = 0
        for c in cls.objetos:
            if c.get_id() > m: m = c.get_id()
            x = m + 1
            obj.set_id(x)
    else:
      obj.set_id(1)
    cls.objetos.append(obj)
    cls.salvar() 

  @classmethod
  def listar_id(cls, id):
    cls.abrir()
    for c in cls.objetos:
      if c.get_id() == id: return c
    return None  
  
  @classmethod
  def atualizar(cls, obj):
    c = cls.listar_id(obj.get_id())
    if c != None:
      cls.objetos.remove(c)
      cls.objetos.append(obj)
      cls.salvar()

  @classmethod
  def excluir(cls, obj):
    c = cls.listar_id(obj.get_id())
    if c != None:
      cls.objetos.remove(c)
      cls.salvar()
  
  @classmethod
  def listar(cls):
    cls.abrir()
    return cls.objetos

  @classmethod
  @abstractmethod
  def salvar(cls):
    pass

  @classmethod
  @abstractmethod
  def abrir(cls):
    pass