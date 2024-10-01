#==> Importando bibliotecas
import streamlit as st
import pandas as pd
import time
from openpyxl import load_workbook
from matplotlib import pyplot as plt
import altair as alt

#-------------------------------------------------------------------------

st.markdown("""
<p style="text-align: center; font-size: 30px; color: navy; font-weight: bold;">
    TP3 - Desenvolvimento Front-End com Python <br>Maik Júnior dos Santos
</p>
""", unsafe_allow_html=True)


st.markdown('---')
st.markdown('## Questão 1') #-------------------------------------------------------------------------

st.markdown('R = O objetivo da criação do dashboard é identificar quais cidades receberam mais visitantes e evidenciar os fatores que motivam a visita a uma cidade. Serão utilizados recursos de filtros, visualização e criação de métricas por meio do Streamlit.')

st.markdown('---')
st.markdown('## Questão 2') #-------------------------------------------------------------------------

uploaded_file = st.file_uploader('Selecione o Arquivo', type=['csv'], key='uploader_1')
if uploaded_file is not None:
    dataframe = pd.read_csv(uploaded_file)
    with st.spinner('Carregando...'):
        time.sleep(3)
        st.markdown('**Percentual de visitantes**')
        st.write(dataframe)

st.markdown('---')
st.markdown('## Questão 3') #-------------------------------------------------------------------------

#==> Checkbox
select = st.checkbox('Selecione para subir outro conjunto')
if select:
    uploaded_file2 = st.file_uploader('Selecione o Arquivo', type=['csv'], key='uploader_2')
    if uploaded_file2 is not None:
        dataframe2 = pd.read_csv(uploaded_file2)
        with st.spinner('Carregando...'):
            time.sleep(3)
            st.markdown('**Conjunto de Dados**')
            st.write(dataframe2)
            
            #==> Radio
            escolha = st.radio("Selecione para ver os dados de:", ('Rio de Janeiro', 'São Paulo', 'Porto Alegre'))
            if escolha == 'São Paulo':
                st.write(dataframe2[[str(dataframe2.columns[0]), 'São_Paulo']])
                dataframe2[[str(dataframe2.columns[0]), 'São_Paulo']].to_csv('../file/São_Paulo.csv', index=False)
            elif escolha == 'Rio de Janeiro':
                st.write(dataframe2[[str(dataframe2.columns[0]), 'Rio_de_Janeiro']])
                dataframe2[[str(dataframe2.columns[0]), 'Rio_de_Janeiro']].to_csv('../file/Rio_de_Janeiro.csv', index=False)
            elif escolha == 'Porto Alegre':
                st.write(dataframe2[[str(dataframe2.columns[0]), 'Porto_Alegre']])
                dataframe2[[str(dataframe2.columns[0]), 'Porto_Alegre']].to_csv('../file/Porto_Alegre.csv', index=False)

            #==> Selectbox
            opcoes = dataframe2[str(dataframe2.columns[0])].unique()
            opcao_selecionada = st.selectbox("Selecione:", opcoes)
            dados = dataframe2[dataframe2[str(dataframe2.columns[0])] == opcao_selecionada]
            st.write(dados)

st.markdown('---')
st.markdown('## Questão 4') #-------------------------------------------------------------------------

#==> Radio
escolha = st.radio("Selecione para baixar os dados:", ('Rio de Janeiro', 'São Paulo', 'Porto Alegre'))
if escolha == 'Rio de Janeiro':
    dados = pd.read_csv('../file/Rio_de_Janeiro.csv')
elif escolha == 'São Paulo':
    dados = pd.read_csv('../file/São_Paulo.csv')
elif escolha == 'Porto Alegre':
    dados = pd.read_csv('../file/Porto_Alegre.csv')
    
#==> Download 
if dados is not None:
    csv = dados.to_csv(index=False)
    st.download_button(
        label='Download CSV',
        data=csv,
        file_name=f'{escolha.replace(" ", "_")}.csv',
        mime='text/csv'
    )

st.markdown('---')
st.markdown('## Questão 5') #-------------------------------------------------------------------------

#==> Progresso
st.write('Deseja ver o relatorio principal >>>')

@st.cache_resource
def leitura_df():
    dt = pd.read_csv('../file/preprocessing_perfil_do_turista.csv')
    
    progress_bar = st.progress(0)
    
    for carregamento in range(100):
        time.sleep(0.05)
        progress_bar.progress(carregamento + 1)
    st.dataframe(dt)
    
#==> Spinner 
if st.button('Clique aqui'):
    leitura_df()
    with st.spinner(''):
        time.sleep(2)
        st.write('carregado.')
             
st.markdown('---')
st.markdown('## Questão 6') #-------------------------------------------------------------------------
            
# #==> Picker
# color = st.color_picker('Defina a cor de fundo', '#FFFFFF')

# #==> Aplicando cor
# st.markdown(
#     f"""
#     <style>
#     .stApp {{
#         background-color: {color};
#     }}
#     </style>
#     """,
#     unsafe_allow_html=True
# )

st.markdown('---')
st.markdown('## Questão 7') #-------------------------------------------------------------------------
   
#==> Uploaded de arquivo
uploaded_file3 = st.file_uploader('Suba o arquivo', type=['csv'],key='uploader_3')
if uploaded_file3 is not None:
    dataframe3 = pd.read_csv(uploaded_file3)

#==> Selecionar colunas
selected_columns = st.multiselect(
    'Selecione as colunas desejadas',
    options=dataframe3.columns,
    default=dataframe3.columns.tolist()
)

#==> Exibindo e filtrando dataset com recurso de <@st.cache>
@st.cache_resource
def exibe_dataframe(conjunto, colunas):
    if colunas:
        filtered_df = conjunto[colunas]
        st.write('DataFrame filtrado:')
        st.dataframe(filtered_df)
    else:
        st.write('Nenhuma coluna selecionada.')

#==> Exibe conjunto
exibe_dataframe(dataframe3, selected_columns)


st.markdown('---')
st.markdown('## Questão 8') #-------------------------------------------------------------------------

#==> Uploaded de arquivo
uploaded_file4 = st.file_uploader('Suba o arquivo', type=["csv"],key='uploader_4')
if uploaded_file4 is not None:
    dataframe4 = pd.read_csv(uploaded_file4)
    
#==> Funcao para inicializar o Session State
def init_session_state(dataframe):
    if 'selected_columns' not in st.session_state:
        # Inicializa com todas as colunas do dataframe se ele não estiver vazio
        st.session_state.selected_columns = dataframe.columns.tolist() if not dataframe.empty else []

#==> Inicializar o Session State
if uploaded_file4 is not None:  # Verifica se o arquivo foi carregado antes de chamar a função
    dataframe4 = pd.read_csv(uploaded_file4)
    init_session_state(dataframe4)  # Passa o dataframe para a função

#==> Seletor de colunas com persistência
st.session_state.selected_columns = st.multiselect(
    'Selecione as colunas desejadas',
    options=dataframe4.columns,
    default=st.session_state.selected_columns, key='2'
)

#==> Exibir o conjunto filtrado
def exibe_dataframe(conjunto, colunas):
    if colunas:
        filtered_df = conjunto[colunas]
        st.write('DataFrame filtrado:')
        st.dataframe(filtered_df)
    else:
        st.write('Nenhuma coluna selecionada.')

#==> Exibir conjunto
exibe_dataframe(dataframe4, st.session_state.selected_columns)


st.markdown('---')
st.markdown('## Questão 9') #-------------------------------------------------------------------------

from services.graf_iterative_1 import iteratividade_graf as iterative1
iterative1()

st.markdown('---')
st.markdown('## Questão 10') #-------------------------------------------------------------------------

from services.graf_iterative_2 import iteratividade_graf as iterative2

#==> Recuperando Conjunto de dados
dt = iterative2()

#==> Plotando grafico de barras
graf_barras = alt.Chart(dt).mark_bar().encode(
    x=dt.columns[0],
    y=dt.columns[1],
    color='Hospedagem'
)

st.altair_chart(graf_barras)

#==> Plotando grafico de pizza
graf_pizza = alt.Chart(dt).mark_arc().encode(
    theta=alt.Theta(field='Rio_de_Janeiro',type='quantitative'),
    color='Hospedagem'
)

st.altair_chart(graf_pizza)


#==> Plotando grafico de linha
graf_line = alt.Chart(dt).mark_line(point=True).encode(
    x='Hospedagem',
    y='Rio_de_Janeiro',
    color='Hospedagem'
).properties(width=600,
            height=300
            )

st.altair_chart(graf_line)

st.markdown('---')
st.markdown('## Questão 11') #------------------------------------------------------------------------

#==> Plotando grafico de Scatter Plot
scatter_plot = alt.Chart(dt).mark_circle(size=150).encode(
    x=alt.X('Hospedagem', sort=None),  # Colocando as categorias no eixo X
    y='Rio_de_Janeiro',                   # Colocando os valores no eixo Y
    color='Hospedagem',
    tooltip=['Hospedagem', 'Rio_de_Janeiro']  # Tooltip para mostrar valores
).properties(
    width=600,
    height=400
)

st.altair_chart(scatter_plot)


st.markdown('---')
st.markdown('## Questão 12') #------------------------------------------------------------------------

col1, col2 = st.columns(2)
with col1:
    st.write('Percentual Máximo')
    max_value = dt['Rio_de_Janeiro'].max()
    # Exibir o valor com estilo de métrica
    st.markdown(f"""<div style="font-size:50px; color:#4CAF50; font-weight:bold; text-align:center;">{max_value}</div>""",unsafe_allow_html=True)
with col2:
    st.write('Percentual Mínimo')
    min_value = dt['Rio_de_Janeiro'].min()
    # Exibir o valor com estilo de métrica
    st.markdown(f"""<div style="font-size:50px; color:#4CAF50; font-weight:bold; text-align:center;">{min_value}</div>""",unsafe_allow_html=True)

#-------------------------------------------------------------------------

st.markdown("""
[**Repositório - Clique Aqui!**](https://github.com/maik-junior/front_end_tp3)
""")
