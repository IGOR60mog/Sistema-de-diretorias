import streamlit as st
import pandas as pd
from view import View
from datetime import datetime
import time

class ManterQuestionarioUI:
    def main():
        st.header("Cadastro de Questionários")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1: ManterQuestionarioUI.listar()
        with tab2: ManterQuestionarioUI.inserir()
        with tab3: ManterQuestionarioUI.atualizar()
        with tab4: ManterQuestionarioUI.excluir()

    def listar():
        Questionarios = View.questionario_listar()
        if len(Questionarios) == 0:
            st.write("Nenhum Questionário cadastrado")
        else:
            lista = []
            for obj in Questionarios: 
                dic = {}
                dic['id'] = obj.get_id()
                usuario = View.get_usuarios_id(obj.get_id_usuario())
                dic['usuário'] = usuario.get_nome()
                dic['data'] = obj.get_data()
                dic['pontos'] = obj.get_pontos()
                dic['curso'] = obj.get_id_curso()
                lista.append(dic)
            df = pd.DataFrame(lista)
            st.dataframe(df, width=1000, hide_index=True)

    def inserir():
        data_str = st.text_input("Informe a data (dd/mm/aaaa): ")
        pontos = st.text_input("Informe os pontos: ")
        usuario = st.selectbox("Informe o usuário:", View.usuario_listar())
        curso = st.selectbox("Informe curso: ", View.curso_listar())
        if st.button("Inserir"):
                data_date = datetime.strptime(data_str, "%d/%m/%Y")
                View.questionario_inserir(usuario.get_id(), data_date, int(pontos), curso.get_id())
                st.success("Questionario inserida com sucesso")
                time.sleep(2)
                st.rerun()

    def atualizar():
        Questionarios = View.questionario_listar()
  
        if len(Questionarios) == 0: 
            st.write("Nenhuma Questionário cadastrado")
        else:
            op = st.selectbox("Atualização de Questionario", Questionarios)
            data_str = st.text_input("Informe nova data (dd/mm/aaaa): ", op.get_data())
            pontos = st.text_input("Informe novos pontos: ", op.get_pontos())
            usuario = st.selectbox("Informe novo usuário:", View.usuario_listar(), key=2)
            curso = st.selectbox("Informe novo curso: ", View.curso_listar())
            if st.button("Atualizar"):
                data_date = datetime.strptime(data_str, "%d/%m/%Y")
                View.questionario_atualizar(op.get_id(), usuario.get_id(), data_date, pontos, curso.get_id())
                st.success("Questionário atualizado com sucesso")
                time.sleep(2)
                st.rerun()

    def excluir():
        Questionarios = View.questionario_listar()
        if len(Questionarios) == 0: 
            st.write("Nenhum Questionário cadastrado")
        else:
            op = st.selectbox("Exclusão de Questionário", Questionarios)
            if st.button("Excluir"):
                View.questionario_excluir(op.get_id())
                st.success("Questionário excluído com sucesso")
                time.sleep(2)
                st.rerun()
