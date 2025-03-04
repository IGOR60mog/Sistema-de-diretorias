import streamlit as st
from view import View
import time

class CadastroUI:
    def main():
        st.header("Abrir Conta no Sistema")
        CadastroUI.inserir()

    def inserir():
        nome = st.text_input("Informe o nome")
        telefone = st.text_input("Informe o telefone")
        email = st.text_input("Informe o e-mail")
        senha = st.text_input("Informe a senha", type="password")
        confsenha = st.text_input("Confirme a senha", type="password")
        if st.button("Inserir"):
            if senha != confsenha:
                st.error("Confirmação de senha inválida!")
            View.usuario_inserir(nome, telefone, email, senha, confsenha)
            st.success("Conta criada com sucesso")
            time.sleep(2)
            st.rerun()
