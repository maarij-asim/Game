import streamlit as st

choices = ["rock", "paper", "scissors"]

# Step state control
if "step" not in st.session_state:
    st.session_state.step = 1
if "p1_choice" not in st.session_state:
    st.session_state.p1_choice = None
if "p2_choice" not in st.session_state:
    st.session_state.p2_choice = None
if "p1_score" not in st.session_state:
    st.session_state.p1_score = 0
if "p2_score" not in st.session_state:
    st.session_state.p2_score = 0
if "result" not in st.session_state:
    st.session_state.result = ""

def get_winner(p1, p2):
    if p1 == p2:
        return "tie"
    elif (p1 == "rock" and p2 == "scissors") or \
         (p1 == "scissors" and p2 == "paper") or \
         (p1 == "paper" and p2 == "rock"):
        return "player1"
    else:
        return "player2"

st.title("Two players : Rock, Paper, Scissors game")

if st.session_state.step == 1:
    st.subheader("Player 1's Turn (Player 2, please look away!)")
    st.session_state.p1_choice = st.selectbox("Choose your weapon:", choices, key="p1")
    if st.button("Confirm Player 1's Choice"):
        st.session_state.step = 2
        st.experimental_rerun()

elif st.session_state.step == 2:
    st.subheader("Player 2's Turn (Player 1, no peeking!)")
    st.session_state.p2_choice = st.selectbox("Choose your weapon:", choices, key="p2")
    if st.button("Reveal Winner"):
        winner = get_winner(st.session_state.p1_choice, st.session_state.p2_choice)
        if winner == "tie":
            st.session_state.result = "🤝 It's a tie!"
        elif winner == "player1":
            st.session_state.result = "🎉 Player 1 wins!"
            st.session_state.p1_score += 1
        else:
            st.session_state.result = "🏆 Player 2 wins!"
            st.session_state.p2_score += 1
        st.session_state.step = 3
        st.experimental_rerun()

elif st.session_state.step == 3:
    st.subheader("🔍 Results")
    st.markdown(f"**Player 1 chose:** {st.session_state.p1_choice}")
    st.markdown(f"**Player 2 chose:** {st.session_state.p2_choice}")
    st.subheader(st.session_state.result)
    st.markdown("---")
    st.markdown(f"📊 **Score** - Player 1: {st.session_state.p1_score} | Player 2: {st.session_state.p2_score}")
    if st.button("Play Again"):
        st.session_state.step = 1
        st.session_state.p1_choice = None
        st.session_state.p2_choice = None
        st.session_state.result = ""
        st.experimental_rerun()

if st.button("🔄 Reset Game"):
    for key in ["step", "p1_choice", "p2_choice", "p1_score", "p2_score", "result"]:
        st.session_state[key] = 0 if "score" in key else None
    st.session_state.step = 1
    st.experimental_rerun()
