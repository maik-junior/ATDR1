import streamlit as st
import matplotlib.pyplot as plt
from statsbombpy import sb
import pandas as pd
import numpy
import time

def main():
    #==> Imagem
    # st.image('file/Imagem2.jpg',width=120)

    #==> Criando sidebar
    competitions = sb.competitions()
    competition = st.sidebar.selectbox("Selecione a competicao", competitions["competition_name"].unique())
    
    #==> Nome da competicao
    st.title(competition) 
    
    #==> Recuperando inndex da competicao
    competition_id = competitions[competitions["competition_name"] == competition]["competition_id"].values[0]
    
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
        id = st.selectbox('Selecione o jogo', matches["match_id"], format_func=lambda idx: get_match_label(matches, idx),key=3) # Selecionando partida
    
    #==> Criando df
    df_partida = pd.DataFrame(matches[['match_id','home_team','away_team']])
    df_partida = df_partida.reset_index(drop=False)
    df_partida = df_partida.loc[df_partida['match_id'] == id, :]
    
    index = int(df_partida[['index']][:1].values)
    
    #==> Recuperando dados
    _id = df_partida['match_id'][index]
    home_team = df_partida['home_team'][index]
    away_team = df_partida['away_team'][index]
    
    # def recolhe():
    
    #==> Tabs e colunas
    tab1, tab2, tab3 = st.tabs(['Partida','Time Mandante','Time Visitante'])
    with tab1:
        #==> Gols
        eventos = pd.DataFrame(sb.events(match_id=_id))
        resultado = eventos[['team_id','shot_outcome','team']].groupby(['shot_outcome','team']).count().reset_index()
        
        st.subheader('Gols')
        st.write(resultado.loc[resultado['shot_outcome'] == 'Goal', :])
    
        st.subheader('Posse de bola')
        eventos = pd.DataFrame(sb.events(match_id=_id))
        team_counts = eventos[['possession', 'team']].groupby('team').team.count()
        
        #==> Grafico pizza
        fig, ax = plt.subplots()
        ax.pie(team_counts, labels=team_counts.index, autopct='%1.1f%%', startangle=90)
        ax.axis('equal')
        st.pyplot(fig)
        
        st.subheader('Jogada Predominante')
        duel_count = eventos.groupby('duel_type').size()
        
        #==> Grafico de pizza
        fig, ax = plt.subplots()
        ax.pie(duel_count, labels=duel_count.index, autopct='%1.1f%%', startangle=90)
        ax.axis('equal')
        st.pyplot(fig)
    
    
        st.subheader('Jogadores mais Requisitados em Campo')
        player_team_count = eventos[['player_id', 'player', 'team']].groupby(['player', 'team']).count().sort_values(by='player_id', ascending=False)
        
        #==> Grafico de barras
        fig, ax = plt.subplots()
        player_team_count['player_id'].plot(kind='bar', ax=ax, figsize=(10, 6))
        ax.set_xlabel('Jogador e Equipe')
        ax.set_ylabel('Contagem de Eventos')
        ax.set_title('Eventos por Jogador e Equipe')
        plt.xticks(rotation=90)
        st.pyplot(fig)
    
    
    
    with tab2:
        #==> Time mandante
        st.title(f'Time: {home_team} - Mandante')
        time_mandante = pd.DataFrame(sb.lineups(match_id=_id)[home_team]).drop(columns=['player_nickname', 'cards'])
        time_mandante['positions'] = time_mandante['positions'].apply(lambda x: x[0]['position'] if isinstance(x, list) and len(x) > 0 else None)
        time_mandante['player_id'] = time_mandante['player_id'].astype(str) 
        st.write(time_mandante)
    
    with tab3:
        #==> Time visitante   
        st.title(f'Time: {away_team} - Visitante')
        time_vistante = pd.DataFrame(sb.lineups(match_id=_id)[away_team]).drop(columns=['player_nickname', 'cards'])
        time_vistante['positions'] = time_vistante['positions'].apply(lambda x: x[0]['position'] if isinstance(x, list) and len(x) > 0 else None)
        time_vistante['player_id'] = time_vistante['player_id'].astype(str) 
        st.write(time_vistante)
        pass


if __name__ == "__main__":
    main()