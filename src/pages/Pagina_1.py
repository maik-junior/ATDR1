import streamlit as st

#==> Partidas da temporada
st.header('Todas Partidas da Temporada')

#==> Verificando matches em sessao
if 'matches' in st.session_state:
    with st.spinner('Carregando os dados...'):
        #==> Recuperando matches
        matches = st.session_state.matches
        
        #==> Verificando se as colunas selecionadas foram armazenadas
        if 'selected_columns' in st.session_state:
            selected_columns = st.session_state.selected_columns
            
            #==> Exibindo colunas armazenadas
            selected_columns = st.multiselect(
                'Selecione os dados desejados',
                options=matches.columns,
                default=selected_columns
            )
            
            #==> Atualiza as colunas na sessao
            st.session_state.selected_columns = selected_columns
            
            #==> Filtra os dados com as colunas selecionadas
            dados_filtrados_matches = matches[st.session_state.selected_columns]
            
            #==> Exibe o dataframe filtrado
            st.dataframe(dados_filtrados_matches)

            #==> Download dos dados filtrados
            @st.cache_data
            def convert_csv(df):
                return df.to_csv(index=False).encode('utf-8')

            #==> Converte para .csv
            data = convert_csv(dados_filtrados_matches)
            
            #==> Botão para download
            st.download_button(
                label="Download",
                data=data,
                file_name='dados_partidas.csv',
                mime='text/csv',
            )
