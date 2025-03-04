import streamlit as st
import pandas as pd
from view import View
import time

class ManterRespostaUI:
    def main():
        st.header("Cadastro de Respostas")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1: ManterRespostaUI.listar()
        with tab2: ManterRespostaUI.inserir()
        with tab3: ManterRespostaUI.atualizar()
        with tab4: ManterRespostaUI.excluir()

    def listar():
        Respostas = View.resposta_listar()
        if len(Respostas) == 0:
            st.write("Nenhuma Resposta cadastrada")
        else:
            lista = []
            for obj in Respostas: 
                dic = {}
                dic['id'] = obj.get_id()
                pergunta = View.get_perguntas_id(obj.get_id_pergunta())
                questionario = View.get_questionarios_id(obj.get_id_questionario())
                usuario = View.get_usuarios_id(questionario.get_id_usuario())
                dic['pergunta'] = pergunta.get_conteudo()
                dic['questionário'] = f"{questionario.get_data()} - {usuario.get_nome()}"
                dic['resposta'] = obj.get_resposta()

                lista.append(dic)
            df = pd.DataFrame(lista)
            st.dataframe(df, width=1000, hide_index=True)

    def inserir():
        pergunta = st.selectbox("Informe a pergunta", View.pergunta_listar())
        questionario = st.selectbox("Informe o questionário", View.questionario_listar())
        resposta = st.text_input("informe N° da resposta (op1, op2, op3, op4, op5):")
        if st.button("Inserir"):
                View.resposta_inserir(pergunta.get_id(), questionario.get_id(), resposta)
                st.success("Resposta inserida com sucesso")
                time.sleep(2)
                st.rerun()

    def atualizar():
        Respostas = View.resposta_listar()
  
        if len(Respostas) == 0: 
            st.write("Nenhuma resposta cadastrada")
        else:
            op = st.selectbox("Atualização de resposta", Respostas)
            pergunta = st.selectbox("Informe a nova pergunta", View.pergunta_listar())
            questionario = st.selectbox("Informe o novo questionário", View.questionario_listar())
            resposta = st.text_input("informe novo N° da resposta (op1, op2, op3, op4, op5): ", op.get_resposta())
            if st.button("Atualizar"):
                View.resposta_atualizar(op.get_id(), pergunta.get_id(), questionario.get_id(), resposta)
                st.success("Resposta atualizado com sucesso")
                time.sleep(2)
                st.rerun()

    def excluir():
        Respostas = View.resposta_listar()
        if len(Respostas) == 0: 
            st.write("Nenhuma resposta cadastrada")
        else:
            op = st.selectbox("Exclusão de resposta", Respostas)
            if st.button("Excluir"):
                View.resposta_excluir(op.get_id())
                st.success("Resposta excluída com sucesso")
                time.sleep(2)
                st.rerun()
