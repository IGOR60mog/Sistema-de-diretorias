import streamlit as st
from view import View
import time
import pandas as pd


class InfoDiretoriasUI:
    def main():

        st.header("Informações sobre as diretorias")
        
        InfoDiretoriasUI.mostrar_diretorias_e_cursos()

    def mostrar_diretorias_e_cursos():

        for x in View.diretoria_listar():
            st.subheader(x.get_nome(), divider=True)
            st.write(f"Diretoria acadêmica de {x.get_finalidade()}. Email para contato: {x.get_email()}.")
            for y in View.curso_listar():
                if y.get_idDiretoria() == x.get_id():
                    st.write(" ")
                    st.write(f" **{y.get_nome()}**")
                    st.write(f" Descrição: {y.get_descricao()}.")
                    st.write(f" Duração: {y.get_duracao()} anos.")         