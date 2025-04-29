import random
import streamlit as st

def play_rps():
    st.title("Rock, Paper, Scissors Game")

    choices = ["rock", "paper", "scissors"]
    player_choice = st.selectbox("Choose your weapon:", choices)

    if st.button("Play"):
        computer_choice = random.choice(choices)

        st.write(f"**You chose:** {player_choice}")
        st.write(f"**Computer chose:** {computer_choice}")

        if player_choice == computer_choice:
            st.info("It's a tie!")
        elif (player_choice == "rock" and computer_choice == "scissors") or \
             (player_choice == "scissors" and computer_choice == "paper") or \
             (player_choice == "paper" and computer_choice == "rock"):
            st.success("You win!")
        else:
            st.error("Computer wins!")

if __name__ == "__main__":
    play_rps()


