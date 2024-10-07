import streamlit as st
from statsbombpy import sb
import pandas as pd
import time

#==> Usando Cache v800
# @st.cache_data(show_spinner=False)  # Removido suppress_st_warning
# def load_data():
#     url = "https://raw.githubusercontent.com/wcota/covid19br/master/cases-brazil-cities-time.csv.gz"
#     # Tenta carregar os dados sem usar o pyarrow
#     data = pd.read_csv(url, compression='gzip', engine='python', dtype=str)  # Força como string
#     return data


def get_match_label(matches, match_id):
    row = matches[matches["match_id"] == match_id].iloc[0]
    return f"{row['match_date']} - {row['home_team']} vs {row['away_team']}"

def main():
    st.write('Desenvolva aqui todo o dashboard')
    menu = ['Home', 'Explore Data', 'Data Analysis', 'About']   #Criando menu
    choice = st.sidebar.selectbox('Menu', menu)                 #Criando Sidebar
    if choice == 'Home':
        st.write('menu selecionado')
    elif choice == 'Explore Data':              #Selecionando competicoes
        st.write('explore as competicoes')
        competitions = sb.competitions()
        # competitions = competitions[["competitions_id","season_id","competition_name","country_name"]]
        
        competitions_names = competitions["competition_name"].unique()                                              #Definindo competicao
        
        competition = st.selectbox('Selecione a competicao', competitions_names)                                    #Selectbox para escolher competicao
       competition_id = competitions[competitions["competition_name"] == competition]["competition_id"].values[0] #Recuperando id da competicao
       
       seasons = competitions[competitions["competition_name"] == competition]["season_name"].unique()            #Temporadas
       season_name = st.selectbox('Selecione a temporada', seasons)                                      #Selecionando temporada
       season_id = competitions[competitions["season_name"] == season_name]["season_id"].values[0]
       
       matches = sb.matches(competition_id = competition_id, season_id = season_id) #Recuperando jogos
       st.selectbox('Selecione o jogo', matches["match_id"], format_func=lambda idx: get_match_label(matches, idx)) # Selecionando partida

        game= st.selectbox("Select Match", maches["match_id"]),format_func= lambda idx: get_mach_label(matches, idx))
        
        st.write('Home Team')
        hoe_team = matches['matches'["match_id"] == game["home_team.valus"][0]v4939

        
        






        
    



# Título da aplicação
st.title("Dashboard")

# with st.container():
    

#==> Sidebar
st.sidebar.header('Sidebar')

#==> Tabs e colunas
tab1, tab2 = st.tabs(['tab1','tab2'])
with tab1:
    col1, col2 = st.columns(2)

with col1:
    st.write('nova coluna 1')
    

with col2:
    st.write('nova coluna 2')
    

with tab2:
    col1, col2 = st.columns(2)
    
    with col1:
        st.write('testando')
    
    with col2:
        st.write('testando')






if __name__ == "__main__":
