#==> Importando bibliotecas
import streamlit as st
import matplotlib.pyplot as plt
from statsbombpy import sb
import pandas as pd

#==> Inplementacao tab1
def _tab1(events_id):
    eventos = pd.DataFrame(events_id)
    resultado = eventos[['team_id', 'shot_outcome', 'team']].groupby(['shot_outcome', 'team']).count().reset_index()
    
    st.subheader('Gols')
    st.write(resultado.loc[resultado['shot_outcome'] == 'Goal', :])

    st.subheader('Posse de bola')
    team_counts = eventos[['possession', 'team']].groupby('team').team.count()
    
    #==> Grafico pizza
    fig, ax = plt.subplots()
    ax.pie(team_counts, labels=team_counts.index, autopct='%1.1f%%', startangle=90)
    ax.axis('equal')
    st.pyplot(fig)
    
    st.subheader('Jogada Predominante')
    duel_count = eventos.groupby('duel_type').size()
    
    #==> Grafico pizza de jogadas
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