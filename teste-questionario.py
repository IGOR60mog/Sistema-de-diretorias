from view import View
from datetime import datetime

class UI:

    @staticmethod
    def menu():
        print("Questionário")
        print("1 - começar questionário, 2 - resultados anteriores")
        return int(input("Escolha opção: "))
        
    @staticmethod
    def main():

        op = UI.menu()
        if op == 1: UI.questionario()
        if op == 2: UI.resultados()

    @staticmethod
    def questionario():

        questionario_id = View.questionario_inserir(1, datetime.now(), 0, 0)
        sorteio = View.sortear_perguntas()
        contador = 0
        respostas = []
        for x in sorteio:
            contador+=1
            print(f"{contador} {x.get_conteudo()}")
            print('1 - discordo totalmente'
                  '2 - discordo'
                  '3 - mais ou menos'
                  '4 - concordo'
                  '5 - concordo totalmente')
            op = int(input("escolha opção: "))
            if op < 0 or op > 5:
                raise ValueError("Opção inválida")
            resp = View.resposta_inserir(x.get_id(), questionario_id, op)
            respostas.append(resp)
        resultado = View.calculo_pontos(questionario_id, respostas)
        print(resultado)

        UI.main()

    def resultados():
        contador = 0
        for x in View.questionario_listar():
            contador += 1
            curso = View.get_cursos_id(x.get_id_curso())
            print(f"{contador} - QUESTIONÁRIOO {x.get_data()}" "\n"
                  f"Curso - {curso.get_nome()} com {x.get_pontos()} pontos!")
        UI.main()
UI.main()
        
            