import random
import streamlit as st

# Initialize session state for scores
if "player_score" not in st.session_state:
    st.session_state.player_score = 0
if "computer_score" not in st.session_state:
    st.session_state.computer_score = 0
if "result" not in st.session_state:
    st.session_state.result = ""

def get_winner(player, computer):
    if player == computer:
        return "tie"
    elif (player == "rock" and computer == "scissors") or \
         (player == "scissors" and computer == "paper") or \
         (player == "paper" and computer == "rock"):
        return "player"
    else:
        return "computer"

def play_game(player_choice):
    computer_choice = random.choice(["rock", "paper", "scissors"])
    result = get_winner(player_choice, computer_choice)

    if result == "player":
        st.session_state.player_score += 1
        st.session_state.result = "🎉 You win!"
    elif result == "computer":
        st.session_state.computer_score += 1
        st.session_state.result = "💻 Computer wins!"
    else:
        st.session_state.result = "🤝 It's a tie!"

    return player_choice, computer_choice

# --- UI ---
st.set_page_config(page_title="Rock Paper Scissors", page_icon="🪨", layout="centered")
st.title("🎮 Rock, Paper, Scissors")
st.markdown("Choose your weapon below:")

# Columns for layout
col1, col2, col3 = st.columns(3)
with col1:
    if st.button("🪨 Rock"):
        player, computer = play_game("rock")
with col2:
    if st.button("📄 Paper"):
        player, computer = play_game("paper")
with col3:
    if st.button("✂️ Scissors"):
        player, computer = play_game("scissors")

# Show result and choices
if "result" in st.session_state and st.session_state.result:
    st.markdown(f"**You chose:** {player} | **Computer chose:** {computer}")
    st.subheader(st.session_state.result)

# Scoreboard
st.markdown("---")
st.markdown("### 📊 Scoreboard")
st.write(f"**You:** {st.session_state.player_score} | **Computer:** {st.session_state.computer_score}")

# Reset button
if st.button("🔄 Reset Game"):
    st.session_state.player_score = 0
    st.session_state.computer_score = 0
    st.session_state.result = ""
    st.experimental_rerun()

