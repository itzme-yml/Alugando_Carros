import streamlit as st
st.title("M- motors Aluguel de Carros")
st.sidebar.title("Escolha seu modelo")
st.sidebar.image("logo.png")

carros = ['BMW', 'Mustang', 'Porche', 'Fusca', 'Toro']

option = st.sidebar.selectbox('Escolha o carro que foi alugado', carros)

st.image(f'{option}.png')
st.markdown(f'## Você alugou o modelo: {option}')
st.markdown('---')


dias = st.text_input(f'Por quantos dias o {option} foi alugado?')
km = st.text_input(f'Quantos km você rodou com o {option}?')