import streamlit as st
import pandas as pd
from view import View
import time

class ManterCursoUI:
    def main():
        st.header("Cadastro de Cursos")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1: ManterCursoUI.listar()
        with tab2: ManterCursoUI.inserir()
        with tab3: ManterCursoUI.atualizar()
        with tab4: ManterCursoUI.excluir()

    def listar():
        Cursos = View.curso_listar()
        if len(Cursos) == 0:
            st.write("Nenhum Curso cadastrado")
        else: 
            lista = []
            for obj in Cursos: 
                dic = {}
                dic['id'] = obj.get_id()
                diretoria = View.get_diretorias_id(obj.get_idDiretoria())
                dic['diretoria'] = diretoria.get_nome()
                dic['nome'] = obj.get_nome()
                dic['descrição'] = obj.get_descricao()
                dic['duração'] = obj.get_duracao()
                lista.append(dic)
            df = pd.DataFrame(lista)
            st.dataframe(df, width=1000, hide_index=True)

    def inserir():
        Diretoria = st.selectbox("Informe a diretoria", View.diretoria_listar())
        nome = st.text_input("informe o nome: ")
        descricao = st.text_input("informe a descrição: ")
        duracao = st.text_input("informe o duração em anos: ")
        if st.button("Inserir"):
                View.curso_inserir(Diretoria.get_id(), nome, descricao, duracao)
                st.success("Curso inserida com sucesso")
                time.sleep(2)
                st.rerun()

    def atualizar():
        Cursos = View.curso_listar()
  
        if len(Cursos) == 0: 
            st.write("Nenhuma Curso cadastrado")
        else:
            op = st.selectbox("Atualização de Curso", Cursos)
            Diretoria = st.selectbox("Informe a diretoria", View.diretoria_listar(), key=2)
            nome = st.text_input("informe nvo nome: ", op.get_nome())
            descricao = st.text_input("informe nova descrição: ", op.get_descricao())
            duracao = st.text_input("informe novo duração: ", op.get_duracao())
            if st.button("Atualizar"):
                View.curso_atualizar(op.get_id(), Diretoria.get_id(), nome, descricao, duracao)
                st.success("Curso atualizado com sucesso")
                time.sleep(2)
                st.rerun()

    def excluir():
        Cursos = View.curso_listar()
        if len(Cursos) == 0: 
            st.write("Nenhuma Curso cadastrado")
        else:
            op = st.selectbox("Exclusão de Curso", Cursos)
            if st.button("Excluir"):
                View.curso_excluir(op.get_id())
                st.success("Curso excluído com sucesso")
                time.sleep(2)
                st.rerun()
