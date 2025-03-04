from templates.loginUI import *
from templates.cadastroUI import *
from templates.infoDiretoriasUI import *
from templates.manterCursoUI import *
from templates.manterDiretoriaUI import *
from templates.manterPerguntaUI import *
from templates.manterQuestionarioUI import *
from templates.manterRespostaUI import *
from templates.manterUsuarioUI import *
from templates.novoQuestionarioUI import *
from templates.resultadosanterioresUI import *
import streamlit as st
from view import View




class IndexUI:
    def menu_visitante():
        op = st.sidebar.selectbox("Menu", ["Entrar no Sistema", "Abrir Conta"])
        if op == "Entrar no Sistema": LoginUI.main()
        if op == "Abrir Conta": CadastroUI.main()
    
    def menu_admin():            
        op = st.sidebar.selectbox("Menu", ["Cadastro de Cursos", "Cadastro de Diretorias", "Cadastro de Perguntas", "Cadastro de Questionários", "Cadastro de Respostas", "Cadastro de Usuarios"])
        if op == "Cadastro de Cursos": ManterCursoUI.main()
        if op == "Cadastro de Diretorias": ManterDiretoriaUI.main()
        if op == "Cadastro de Perguntas": ManterPerguntaUI.main()
        if op == "Cadastro de Questionários": ManterQuestionarioUI.main()
        if op == "Cadastro de Respostas": ManterRespostaUI.main()
        if op == "Cadastro de Usuarios": ManterUsuarioUI.main()

    def menu_usuario():
        op = st.sidebar.selectbox("Menu", ["Novo Questionário", "Resultados Anteriores", "Informações sobre Diretorias"])
        if op == "Novo Questionário": NovoQuestionarioUI.main()
        if op == "Resultados Anteriores": ResultadosAnterioresUI.main()
        if op == "Informações sobre Diretorias": InfoDiretoriasUI.main()

    def sair_do_sistema():
        if st.sidebar.button("Sair"):
            del st.session_state["usuario_id"]
            del st.session_state["usuario_nome"]
            if st.session_state['questionario_id']:  del st.session_state['questionario_id']
            if st.session_state['sorteio']: del st.session_state['sorteio']
            if st.session_state['respostas']: del st.session_state['respostas']
        st.rerun()
    
    def sidebar():
        if "usuario_id" not in st.session_state:
            IndexUI.menu_visitante()   
        else:
            admin = st.session_state["usuario_nome"] == "admin"
            st.sidebar.write("Bem-vindo(a), " + st.session_state["usuario_nome"])
            if admin: IndexUI.menu_admin()
            else: IndexUI.menu_usuario()
            IndexUI.sair_do_sistema() 
    
    def main():
        View.usuario_admin()
        IndexUI.sidebar()
       
IndexUI.main()
