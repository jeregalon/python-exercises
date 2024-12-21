import random
import time

# Inicialización del tablero y variables globales
def reset_game():
    global board, userTurn, gameComplete
    board = [i + 1 for i in range(9)]
    userTurn = random.choice([True, False])  # Primer turno aleatorio
    gameComplete = False

reset_game()

def printBoard():
    print()
    for i in range(0, 9, 3):
        print(f"{board[i]} | {board[i+1]} | {board[i+2]}")
        if i < 6:
            print("--+---+--")
    print()

def check_winner():
    """Verifica si hay un ganador o un empate."""
    winning_combinations = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Filas
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columnas
        (0, 4, 8), (2, 4, 6)              # Diagonales
    ]
    for a, b, c in winning_combinations:
        if board[a] == board[b] == board[c]:
            return board[a]  # Retorna "X" o "O" si hay un ganador
    if all(type(square) != int for square in board):  # Tablero lleno
        return "Empate"
    return None

def find_best_move(player):
    """Encuentra la mejor jugada para el jugador (X o O)."""
    winning_combinations = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Filas
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columnas
        (0, 4, 8), (2, 4, 6)              # Diagonales
    ]
    # Prioridad 1: Ganar
    for a, b, c in winning_combinations:
        if board[a] == board[b] == player and type(board[c]) == int:
            return c
        if board[a] == board[c] == player and type(board[b]) == int:
            return b
        if board[b] == board[c] == player and type(board[a]) == int:
            return a
    # Prioridad 2: Bloquear
    opponent = "O" if player == "X" else "X"
    for a, b, c in winning_combinations:
        if board[a] == board[b] == opponent and type(board[c]) == int:
            return c
        if board[a] == board[c] == opponent and type(board[b]) == int:
            return b
        if board[b] == board[c] == opponent and type(board[a]) == int:
            return a
    # Prioridad 3: Ocupar el centro
    if type(board[4]) == int:
        return 4
    # Prioridad 4: Ocupar una esquina
    for i in [0, 2, 6, 8]:
        if type(board[i]) == int:
            return i
    # Prioridad 5: Movimiento aleatorio
    for i in range(9):
        if type(board[i]) == int:
            return i

def playGame():
    global userTurn, gameComplete
    
    if userTurn:
        # Turno del usuario
        while True:
            try:
                print()
                numPlayed = int(input("Introduce un número para jugar: "))
                print()
                if not (1 <= numPlayed <= 9):
                    print("\nNúmero no válido. Intenta de nuevo.\n")
                elif board[numPlayed - 1] in ["X", "O"]:
                    print("\nCasilla ocupada. Intenta de nuevo.\n")
                else:
                    board[numPlayed - 1] = "O"
                    break
            except ValueError:
                print("\nPor favor introduce un número válido.\n")
    else:
        # Turno de la computadora
        print("\nPensando...\n")
        time.sleep(2)  # Simula el pensamiento
        best_move = find_best_move("X")
        board[best_move] = "X"
        print(f"\nJugué en la casilla {best_move + 1}. Tu turno.\n")

    printBoard()
    winner = check_winner()
    if winner:
        if winner == "Empate":
            print("\n¡Es un empate!\n")
        else:
            print(f"\n¡{winner} gana el juego!\n")
        reset_game()
        print("\nEl juego se reinicia...\n")
        time.sleep(2)
        printBoard()
    else:
        userTurn = not userTurn

# Inicia el juego con el tablero impreso
print("\n¡Bienvenido al juego de Tic Tac Toe!\n")
printBoard()
if not userTurn:
    print("\nLa computadora juega primero.\n")
else:
    print("\nTú juegas primero.\n")

while True:
    playGame()
