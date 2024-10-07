import streamlit as st
from statsbombpy import sb
import pandas as pd
import numpy
import time

# Carregar a imagem
st.image("../file/Imagem2.jpg",width=90)
# st.image("caminho_para_imagem.jpg", caption="Redimensionada", width=300)


# def main():
    
competitions = sb.competitions()

#----------------------------sidebar------------------------------------------
# competition = st.sidebar.selectbox("Selecione a competicao", competitions["competition_name"].unique())
# st.title(competition)                                  
# competition_id = competitions[competitions["competition_name"] == competition]["competition_id"].values[0]
# # st.write(f'id da competicao {competition_id}') #==> id da competicao



# season_name =st.sidebar.selectbox('Selecione a temporada', competitions[competitions["competition_name"] == competition]["season_name"].unique())
# season_id = competitions[competitions["season_name"] == season_name]["season_id"].values[0]
# st.write(f'id da temporada {season_id}') #==> id da temporada
#----------------------------sidebar------------------------------------------


def get_match_label(matches, match_id):
        row = matches[matches["match_id"] == match_id].iloc[0]
        # st.write(row[0])
        return f"{row['match_date']} - {row['home_team']} vs {row['away_team']}" #==> jogos
    
matches = sb.matches(competition_id = competition_id, season_id = season_id) #Recuperando jogos

st.write(matches[['match_id','home_team','away_team']])
st.write(matches['match_id'][0])
st.write(matches['home_team'][0])
st.write(matches['away_team'][0])


# st.write(pd.DataFrame(sb.lineups(match_id=3857256)["Serbia"]))

st.sidebar.selectbox('Selecione o jogo', matches["match_id"], format_func=lambda idx: get_match_label(matches, idx))


col1, col2 = st.columns(2)
    
with col1:
    seasons = competitions[competitions["competition_name"] == competition]["season_name"].unique()           
    season_name = st.selectbox('Selecione a temporada', seasons, key=2)                                      
    season_id = competitions[competitions["season_name"] == season_name]["season_id"].values[0]
           
with col2:
    def get_match_label(matches, match_id):
        row = matches[matches["match_id"] == match_id].iloc[0]
        return f"{row['match_date']} - {row['home_team']} vs {row['away_team']}"

    matches = sb.matches(competition_id = competition_id, season_id = season_id) #Recuperando jogos
    st.selectbox('Selecione o jogo', matches["match_id"], format_func=lambda idx: get_match_label(matches, idx),key=3) # Selecionando partida

def recolhe():
    #==> Tabs e colunas
# tab1, tab2, tab3 = st.tabs(['Partida','Time Mandante','Time Visitante'])
# with tab1:
#     pass


# with tab2:
#     #==> Time mandante
#     st.title(f'Time: {matches['home_team'][0]} - Mandante')
#     time_mandante = pd.DataFrame(sb.lineups(match_id=matches['match_id'][0])[matches['home_team'][0]]).drop(columns=['player_nickname', 'cards'])
#     time_mandante['positions'] = time_mandante['positions'].apply(lambda x: x[0]['position'] if isinstance(x, list) and len(x) > 0 else None)
#     time_mandante['player_id'] = time_mandante['player_id'].astype(str) 
#     st.write(time_mandante)

# with tab3:
#     #==> Time visitante   
#     st.title(f'Time: {matches['away_team'][0]} - Visitante')
#     time_vistante = pd.DataFrame(sb.lineups(match_id=matches['match_id'][0])[matches['away_team'][0]]).drop(columns=['player_nickname', 'cards'])
#     time_vistante['positions'] = time_vistante['positions'].apply(lambda x: x[0]['position'] if isinstance(x, list) and len(x) > 0 else None)
#     time_vistante['player_id'] = time_vistante['player_id'].astype(str) 
#     st.write(time_vistante)
    
    pass

# #==> Time mandante
# st.title(f'Time: {matches['home_team'][0]} - Mandante')
# time_mandante = pd.DataFrame(sb.lineups(match_id=matches['match_id'][0])[matches['home_team'][0]]).drop(columns=['player_nickname', 'cards'])
# time_mandante['positions'] = time_mandante['positions'].apply(lambda x: x[0]['position'] if isinstance(x, list) and len(x) > 0 else None)
# time_mandante['player_id'] = time_mandante['player_id'].astype(str) 
# st.write(time_mandante)

# #==> Time visitante   
# st.title(f'Time: {matches['away_team'][0]} - Visitante')
# time_vistante = pd.DataFrame(sb.lineups(match_id=matches['match_id'][0])[matches['away_team'][0]]).drop(columns=['player_nickname', 'cards'])
# time_vistante['positions'] = time_vistante['positions'].apply(lambda x: x[0]['position'] if isinstance(x, list) and len(x) > 0 else None)
# time_vistante['player_id'] = time_vistante['player_id'].astype(str) 
# st.write(time_vistante)

# pd.DataFrame(sb.lineups(match_id=3857256)["Serbia"]).drop(columns=['player_nickname', 'cards'])

#==> Recupera todas as partidas do campeonato da temporada
st.dataframe(sb.matches(competition_id=competition_id, season_id=season_id))





# if __name__ == "__main__":
#     main()