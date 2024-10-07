import streamlit as st
from mplsoccer import Sbopen
from mplsoccer.pitch import Pitch
    
def get_match_label(matches, match_id):
    row = matches[matches['match_id'] == match_id].iloc[0]
    return f"{row['match_date']} - {row['home_team']} vs {row['away_team']}"

def plot_passes(match, player_name):
    player_filter = (match.type_name  == 'Pass') & (match.player_name'] == player_name)
    pass_data = match.loc[player_filter, ['x', 'y', 'end_y']]
    pitch = Pitch(pitch_type='statsbomb', orientation='vertical', stripe=True, line_color='black')
    
    fig, ax = pitch.grid()
    pitch.lines(pass_data['start_x'], pass_data['start_y'],
                pass_data['end_x'], pass_data['end_y'],
                ax=ax, color='blue', linewidth=2, alpha=0.6)
    ax.set_title(f"Passes by {player_name}")
    st.pyplot(fig)




def main():
    col1, col2 = st.columns(2)
    
    with col_1:
        st.write("Killian Mbappé")
    
    with col_2:
        st.write("Lionel Messi")
    
if __name__ == "__main__":
    main()

