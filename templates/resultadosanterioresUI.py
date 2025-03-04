import streamlit as st
from view import View
import time

class ResultadosAnterioresUI:
    def main():
        st.header("Resultados anteriores")
        QuestsAnteriores = []
        for x in View.questionario_listar():
            if x.get_id_usuario() == st.session_state['usuario_id']:
                QuestsAnteriores.append(x)
        if QuestsAnteriores == []:
            st.write("Nenhum resultado encontrado.")
        for x in QuestsAnteriores:
            st.subheader(f"Questionário de {x.get_data()}", divider=True)
            curso = View.get_cursos_id(x.get_id_curso())
            st.write(f"- **Curso** - {curso.get_nome()}")
            st.write(f"- **Pontuação** - {x.get_pontos()} pontos")

