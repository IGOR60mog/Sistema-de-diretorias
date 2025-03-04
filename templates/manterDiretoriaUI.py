import streamlit as st
import pandas as pd
from view import View
import time

class ManterDiretoriaUI:
    def main():
        st.header("Cadastro de Diretorias")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1: ManterDiretoriaUI.listar()
        with tab2: ManterDiretoriaUI.inserir()
        with tab3: ManterDiretoriaUI.atualizar()
        with tab4: ManterDiretoriaUI.excluir()

    def listar():
        Diretorias = View.diretoria_listar()
        if len(Diretorias) == 0:
            st.write("Nenhum Diretoria cadastrado")
        else:
            dic = []
            for obj in Diretorias: dic.append(obj.to_json())
            df = pd.DataFrame(dic)
            st.dataframe(df, width=1000, hide_index=True)

    def inserir():
        nome = st.text_input("informe o nome: ")
        finalidade = st.text_input("informe a finalidade: ")
        email = st.text_input("informe o email: ")
        if st.button("Inserir"):
                View.diretoria_inserir(nome, finalidade, email)
                st.success("Diretoria inserida com sucesso")
                time.sleep(2)
                st.rerun()

    def atualizar():
        Diretorias = View.diretoria_listar()
  
        if len(Diretorias) == 0: 
            st.write("Nenhuma Diretoria cadastrado")
        else:
            op = st.selectbox("Atualização de Diretoria", Diretorias)
            nome = st.text_input("informe nvo nome: ", op.get_nome())
            finalidade = st.text_input("informe nova finalidade: ", op.get_finalidade())
            email = st.text_input("informe novo email: ", op.get_email())
            if st.button("Atualizar"):
                View.diretoria_atualizar(op.get_id(), nome, finalidade, email)
                st.success("Diretoria atualizado com sucesso")
                time.sleep(2)
                st.rerun()

    def excluir():
        Diretorias = View.diretoria_listar()
        if len(Diretorias) == 0: 
            st.write("Nenhuma Diretoria cadastrado")
        else:
            op = st.selectbox("Exclusão de Diretoria", Diretorias)
            if st.button("Excluir"):
                View.diretoria_excluir(op.get_id())
                st.success("Diretoria excluído com sucesso")
                time.sleep(2)
                st.rerun()
