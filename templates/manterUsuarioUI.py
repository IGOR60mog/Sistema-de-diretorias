import streamlit as st
import pandas as pd
from view import View
import time

class ManterUsuarioUI:
    def main():
        st.header("Cadastro de Usuários")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1: ManterUsuarioUI.listar()
        with tab2: ManterUsuarioUI.inserir()
        with tab3: ManterUsuarioUI.atualizar()
        with tab4: ManterUsuarioUI.excluir()

    def listar():
        usuarios = View.usuario_listar()
        if len(usuarios) == 0: 
            st.write("Nenhum usuario cadastrado")
        else:    
            dic = []

            for obj in usuarios: 
                dic_sem_senha = obj.to_json()
                del dic_sem_senha['senha']
                del dic_sem_senha['confsenha']                
                dic.append(dic_sem_senha)
            df = pd.DataFrame(dic)
            st.dataframe(df, width=1000, hide_index=True)

    def inserir():
        nome = st.text_input("Informe o nome do usuário")
        telefone = st.text_input("Informe o fone")
        email = st.text_input("Informe o e-mail")
        senha = st.text_input("Informe a senha", type="password") 
        confsenha = st.text_input("Confirme a senha", type="password") 
        if st.button("Inserir"):
            if senha != confsenha:
                st.error("Confirmação de senha inválida")
            else:
                View.usuario_inserir(nome, telefone, email, senha, confsenha)
                st.success("Usuário inserido com sucesso")
                time.sleep(2)
                st.rerun()

    def atualizar():
        usuarios = View.usuario_listar()
  
        if len(usuarios) == 0: 
            st.write("Nenhum usuario cadastrado")
        else:
            op = st.selectbox("Atualização de usuario", usuarios)
            nome = st.text_input("Informe o novo nome do usuario", op.get_nome())
            telefone = st.text_input("Informe o novo fone", op.get_telefone())
            email = st.text_input("Informe o novo e-mail", op.get_email())
            senha = st.text_input("Informe a nova senha", op.get_senha(), type="password")
            confsenha = st.text_input("Confirme a nova senha", op.get_confsenha(), type="password")
            if st.button("Atualizar"):
                View.usuario_atualizar(op.get_id(), nome, telefone, email, senha, confsenha)
                st.success("Usuário atualizado com sucesso")
                time.sleep(2)
                st.rerun()

    def excluir():
        usuarios = View.usuario_listar()
        if len(usuarios) == 0: 
            st.write("Nenhum usuario cadastrado")
        else:
            op = st.selectbox("Exclusão de usuário", usuarios)
            if st.button("Excluir"):
                View.usuario_excluir(op.get_id())
                st.success("Usuário excluído com sucesso")
                time.sleep(2)
                st.rerun()
