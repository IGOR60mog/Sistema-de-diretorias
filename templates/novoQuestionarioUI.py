import streamlit as st
from datetime import datetime
import random
from view import View
from datetime import *
import time

class NovoQuestionarioUI:
    @staticmethod
    def main():
        st.header("QUESTIONÁRIO")
        if 'questionario_id' not in st.session_state:
            
            st.write("Olá")
            if st.button("começar questionário"):
                if 'sorteio' in st.session_state: del st.session_state['sorteio']
                if 'respostas' in st.session_state: del st.session_state['respostas']
                #Cria questionário 
                st.session_state['questionario_id'] = View.questionario_inserir(st.session_state['usuario_id'], datetime.now(), 0, 0)
                st.write(st.session_state['questionario_id'])

                st.session_state['sorteio'] = View.sortear_perguntas()
                st.write(len(st.session_state['sorteio']))

                q = st.session_state['questionario_id']

                # Garante que não há respostas duplicadas
                st.session_state['respostas'] = []

                #Inserimos todas os objetos resposta no json com sua pergunta
                for x in st.session_state['sorteio']:
                    idp = x.get_id()
                    r = 0
                    View.resposta_inserir(idp, q, r)

                #Inserimos todos os objetos resposta no session_state
                for x in View.resposta_listar():
                    if x.get_id_questionario() == q:
                        st.session_state['respostas'].append(x)

                NovoQuestionarioUI.exibir_perguntas(st.session_state['questionario_id'], st.session_state['respostas'])
                # st.rerun()

        else:
            #Mostra as perguntas 
            NovoQuestionarioUI.exibir_perguntas(st.session_state['questionario_id'], st.session_state['respostas'])

    def exibir_perguntas(id, respostas):

        st.write(respostas)

        if st.button("cancelar questionário"):
            View.questionario_excluir(id)
            for x in View.resposta_listar():
                if x.get_id_questionario() == id:
                    View.resposta_excluir(x.get_id())
            del st.session_state['questionario_id']
            st.rerun()     

        #INSERIR TODAS AS RESPOSTAS A PARTIR DO SORTEIO, E APENAS EXIBIR OS OBJETOS. EX.: MOSTRAR PERGUNTA DA RESPOSTA ID 2. 
        # TODA VEZ QUE O OBJETO TIVER RESPOSTA > 0, ATUALIZAR OBJETO.
        op = ['1', '2', '3', '4', '5']
        key = 0

        for x in respostas:
            key +=1
            pergunta = View.get_perguntas_id(x.get_id_pergunta())
            p_conteudo = pergunta.get_conteudo()
            resposta_radio = st.radio(f"{key} - {p_conteudo}" , op, index=None, key=key)
            if resposta_radio != None:
                View.resposta_atualizar(x.get_id(), x.get_id_pergunta(), id, int(resposta_radio))
            st.write(resposta_radio)

            #verifica se o questionário foi respondido completamente

        if st.button('Enviar Questionário'):
            lista = View.calculo_pontos()
            st.write(f'SEU CURSO É {lista[0].get_nome()} com {lista[1]} pontos!')
            questionario = View.get_questionarios_id(st.session_state['questionario_id'])
            View.questionario_atualizar(questionario.get_id(), questionario.get_id_usuario(), questionario.get_data(), lista[1], lista[0].get_id())
            del st.session_state['questionario_id']
            del st.session_state['respostas']
            del st.session_state['sorteio']
            if st.button('Reiniciar Questionário'):
                st.rerun()

        
    
    