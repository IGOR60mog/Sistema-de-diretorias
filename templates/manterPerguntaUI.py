import streamlit as st
import pandas as pd
from view import View
import time

class ManterPerguntaUI:
    def main():
        st.header("Cadastro de Perguntas")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1: ManterPerguntaUI.listar()
        with tab2: ManterPerguntaUI.inserir()
        with tab3: ManterPerguntaUI.atualizar()
        with tab4: ManterPerguntaUI.excluir()

    def listar():
        Perguntas = View.pergunta_listar()
        if len(Perguntas) == 0:
            st.write("Nenhum Pergunta cadastrado")
        else:
            lista = []
            for obj in Perguntas:
                dic = {}
                dic['id'] = obj.get_id()
                curso = View.get_cursos_id(obj.get_id_curso())
                dic['curso'] = curso.get_nome()
                dic['conteúdo'] = obj.get_conteudo()
                lista.append(dic)
            df = pd.DataFrame(lista)
            st.dataframe(df, width=1000, hide_index=True)

    def inserir():
        curso = st.selectbox("Informe o curso: ", View.curso_listar())
        conteudo = st.text_input("Informe o conteúdo: ")
        if st.button("Inserir"):
                View.pergunta_inserir(curso.get_id(), conteudo)
                st.success("Pergunta inserida com sucesso")
                time.sleep(2)
                st.rerun()

    def atualizar():
        Perguntas = View.pergunta_listar()
  
        if len(Perguntas) == 0: 
            st.write("Nenhuma Pergunta cadastrado")
        else:
            op = st.selectbox("Atualização de Pergunta", Perguntas)
            curso = st.selectbox("Informe o curso: ", View.curso_listar(), key=2)
            conteudo = st.text_input("Informe o conteúdo: ", op.get_conteudo())
            if st.button("Atualizar"):
                View.pergunta_atualizar(op.get_id(), curso.get_id(), conteudo)
                st.success("Pergunta atualizado com sucesso")
                time.sleep(2)
                st.rerun()

    def excluir():
        Perguntas = View.pergunta_listar()
        if len(Perguntas) == 0: 
            st.write("Nenhuma Pergunta cadastrado")
        else:
            op = st.selectbox("Exclusão de Pergunta", Perguntas)
            if st.button("Excluir"):
                View.pergunta_excluir(op.get_id())
                st.success("Pergunta excluído com sucesso")
                time.sleep(2)
                st.rerun()
