import streamlit as st
import math
import tintas as t


#------------------|INICIO DA CONFIGURAÇÃO DE LAYOUT|--------------------------#
cont1 = st.container()
q1,q2 = st.columns(2)
cont2 = st.container()
cont3 = st.container()
colu1,colu2 = st.columns(2)
cont4 = st.container()
k1,k2 = st.columns(2)
co1,co2,co3,co4 = st.columns(4)
c1,c2,c3,c4 = st.columns(4)
col1,col2 = st.columns(2)

opcoes = t.tintas



#------------------|FIM DA CONFIGURAÇÃO DE LAYOUT|--------------------------#

#------------------|INICIO DO PROGRAMA|--------------------------#


with cont1:
    st.subheader('Calculadora de Rendimentos - Obra & Lar:')
    tintas = st.selectbox('Selecione a Tinta:', opcoes)
    rend = opcoes[tintas]['rendimento']
    dilu = opcoes[tintas]['diluicao']
    if opcoes == 'Selecione um modelo':
        msg_dilu = st.warning('Selecione a Tinta para saber como é feita sua diluição.')
    elif opcoes != 'Selecione um modelo':
        msg_dilu = st.success(f'{dilu}')
with cont2:
    parede = st.selectbox('Sua parede possui porta ou janela?',['Não','Sim'])
    with colu1:
        if parede == 'Sim':
            with colu1:    
                port_alt = st.number_input('Altura da Porta/Janela: (Metros)',key='parede_alt')
            with colu2:
                port_lar = st.number_input('Largura da Porta/Janela: (Metros)',key='parede_lar')
                with colu1:
                    altura = st.number_input('Altura da Parede: (Metros)',key='altura')
                with colu2:
                    largura = st.number_input('Largura da Parede: (Metros)',key='largura')
                port = (port_alt * port_lar)
                par = (altura * largura)
                area = (par - port)
                rendimento = (area / rend)
                
        elif parede == 'Não':
                with colu1:
                    altura = st.number_input('Altura da Parede: (Metros)',key='altura')
                with colu2:
                    largura = st.number_input('Largura da Parede: (Metros)',key='largura')
                par = (altura * largura)
                rendimento = math.ceil(par / rend)

#------------------|INICIO DO CÁLCULO|--------------------------#

def lata (txt):
    if txt <= 1:
        emb = 'unidade'
    if txt > 1:
        emb = 'unidades'
    return emb

latas = lata(rendimento)

with cont4:
    if altura == 0 and largura == 0:
        msg_rend = st.warning('Insira um valor de Altura e Largura da Parede para calcularmos quantas unidades você precisará.')
    else:
        msg_rend1 = st.success(f'Você precisará de {rendimento} {latas} de {tintas} para pintar uma parede de {par} m²')

#------------------|FIM DO CÁLCULO|--------------------------#
#------------------|FIM DO PROGRAMA|--------------------------#




    