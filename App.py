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

if option == 'BMW' :
     diaria = 450

elif option == 'Mustang' :
    diaria = 500

elif option == 'Porche' :
    diaria = 300

elif option == 'Fusca' :
    diaria = 250

elif option == 'Toro' :
    diaria = 550




if st.button('Calcular'):
    dias = int(dias)
    km = float(km)

    total_dias = dias *diaria
    total_km = km * 0.15
    aluguel_total = total_dias+total_km

    st.warning(f'você alugou o {option} por {dias} dias e rodou {km} km. O valor total a pagar é R${aluguel_total:2f}')
