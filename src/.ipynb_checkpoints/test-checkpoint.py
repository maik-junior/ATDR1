# import streamlit as st
# from statsbombpy import sb
# import pandas as pd
# import time



# # st.dataframe(sb.competitions())

# df = pd.DataFrame(sb.competitions())

# st.dataframe(df.columns)



# st.sidebar(
    
        
#     col1, col2, col3 = st.columns(3)
    
#     with col1:
#         competitions = sb.competitions()
#         competitions_names = competitions["competition_name"].unique() 
#         competition = st.selectbox('Selecione a competicao', competitions_names)                                  
#         competition_id = competitions[competitions["competition_name"] == competition]["competition_id"].values[0]
        
#     with col2:
#         seasons = competitions[competitions["competition_name"] == competition]["season_name"].unique()           
#         season_name = st.selectbox('Selecione a temporada', seasons)                                      
#         season_id = competitions[competitions["season_name"] == season_name]["season_id"].values[0]
               
#     with col3:
#         def get_match_label(matches, match_id):
#             row = matches[matches["match_id"] == match_id].iloc[0]
#             return f"{row['match_date']} - {row['home_team']} vs {row['away_team']}"
    
#         matches = sb.matches(competition_id = competition_id, season_id = season_id) #Recuperando jogos
#         st.selectbox('Selecione o jogo', matches["match_id"], format_func=lambda idx: get_match_label(matches, idx)) # Selecionando partida
# )
    
    