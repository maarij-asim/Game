
import streamlit as st

# Initialize session state
if 'board' not in st.session_state:
    st.session_state.board = [" "] * 9
if 'current_player' not in st.session_state:
    st.session_state.current_player = "X"
if 'game_over' not in st.session_state:
    st.session_state.game_over = False

# Check for a win
def check_win(board, player):
    for i in range(0, 9, 3):
        if board[i] == board[i+1] == board[i+2] == player:
            return True
    for i in range(3):
        if board[i] == board[i+3] == board[i+6] == player:
            return True
    if board[0] == board[4] == board[8] == player:
        return True
    if board[2] == board[4] == board[6] == player:
        return True
    return False

# Check for draw
def check_draw(board):
    return all(cell != " " for cell in board)

# Game title
st.title("Tic-Tac-Toe by Maarij")

# Emoji mapping
emoji_map = {"X": "❌", "O": "⭕", " ": " "}

# Display the board in a 3x3 grid
cols = st.columns(3)
for i in range(9):
    display_value = emoji_map[st.session_state.board[i]]
    if cols[i % 3].button(display_value, key=i, use_container_width=True, disabled=st.session_state.board[i] != " " or st.session_state.game_over):
        st.session_state.board[i] = st.session_state.current_player
        if check_win(st.session_state.board, st.session_state.current_player):
            st.success(f"Player {emoji_map[st.session_state.current_player]} wins!")
            st.session_state.game_over = True
        elif check_draw(st.session_state.board):
            st.info("It's a draw!")
            st.session_state.game_over = True
        else:
            st.session_state.current_player = "O" if st.session_state.current_player == "X" else "X"

# Show current player if game is not over
if not st.session_state.game_over:
    st.write(f"Current Player: {emoji_map[st.session_state.current_player]}")

# Reset button
if st.button("Restart Game"):
    st.session_state.board = [" "] * 9
    st.session_state.current_player = "X"
    st.session_state.game_over = False

