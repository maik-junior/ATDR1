import streamlit as st
import time



def get_value(selected_option):
    time.sleep(3)
    if selected_option == "A":
        return 1
    elif selected_option == "B":
        return 2
    elif selected_option == "C":
        return 3
    else:
        return None

st.title('Spinner Example')


#if st.button("Iniciar alguma operação"):
#    with st.spinner("Aguarde..."):
#        time.sleep(30)
#    st.success("Operação concluída com sucesso!")
#    st.balloons()


options = ["A", "B", "C"]

selected_option = st.selectbox("Selecione uma opção", options)


with st.spinner("Making magic happen"):
    value = get_value(selected_option)
    st.write(f"O valor selecionado foi: {value}")
    st.metric("Valor", value)
