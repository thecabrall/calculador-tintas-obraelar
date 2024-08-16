


with cont2:
    parede = st.selectbox('Sua parede possui porta ou janela?',['','Sim','Não'])
    with colu1:
        if parede == 'Sim':
            with colu1:    
                port_alt = st.number_input('Altura da Porta/Janela: (Metros)',key='parede_alt')
            with colu2:
                port_lar = st.number_input('Largura da Porta/Janela: (Metros)',key='parede_lar')
                janela = (port_alt * port_lar)
                parede = (altura * largura)
                area_janela = (parede - janela)
                rd = tinta['tintas']['rendimento']
                rende = float()
                area2 = (area_janela/rd)
                with cont4:
                    st.subheader(f'Sua escolha foi a tinta {tinta}')
                    st.subheader(f'Você precisará de {area2:.2f} L/m²')
        elif parede =='Não':
            rende = t.tintas(['tintas']['rendimento'])
            valor = t.tintas(['tintas']['rendimento'])
            rd = float(valor)
            parede = (altura * largura)
            area = (parede/valor)
            with cont4:
                litros = math.ceil(parede / rende )
                st.subheader(f'Sua escolha foi a tinta {tinta}')
                st.subheader(f'Você precisará de {litros:.0f} L/m²')
        else:
            st.warning('Preencha todos os campos para ter o cálculo exato de rendimento.')
        