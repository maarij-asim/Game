import streamlit as st

# Initialize session state
for key in ["p1_choice", "p2_choice", "result", "p1_score", "p2_score"]:
    if key not in st.session_state:
        st.session_state[key] = None if "choice" in key else 0

def get_winner(p1, p2):
    if p1 == p2:
        return "tie"
    elif (p1 == "rock" and p2 == "scissors") or \
         (p1 == "scissors" and p2 == "paper") or \
         (p1 == "paper" and p2 == "rock"):
        return "player1"
    else:
        return "player2"

# --- UI ---
st.set_page_config(page_title="Two Player RPS", page_icon="🎮", layout="centered")
st.title("👬 Rock, Paper, Scissors - 2 Players")

choices = ["rock", "paper", "scissors"]

st.subheader("Player 1")
st.session_state.p1_choice = st.selectbox("Choose your weapon (Player 1):", choices, key="p1_select")

st.subheader("Player 2")
st.session_state.p2_choice = st.selectbox("Choose your weapon (Player 2):", choices, key="p2_select")

if st.button("🎯 Reveal Winner"):
    p1 = st.session_state.p1_choice
    p2 = st.session_state.p2_choice

    winner = get_winner(p1, p2)
    if winner == "tie":
        st.session_state.result = "🤝 It's a tie!"
    elif winner == "player1":
        st.session_state.p1_score += 1
        st.session_state.result = "🎉 Player 1 wins!"
    else:
        st.session_state.p2_score += 1
        st.session_state.result = "🏆 Player 2 wins!"

    st.markdown(f"**Player 1 chose:** {p1} | **Player 2 chose:** {p2}")
    st.subheader(st.session_state.result)

# Scoreboard
st.markdown("---")
st.markdown("### 📊 Scoreboard")
st.write(f"**Player 1:** {st.session_state.p1_score} | **Player 2:** {st.session_state.p2_score}")

# Reset game
if st.button("🔄 Reset Game"):
    st.session_state.p1_choice = None
    st.session_state.p2_choice = None
    st.session_state.result = ""
    st.session_state.p1_score = 0
    st.session_state.p2_score = 0
    st.experimental_rerun()
