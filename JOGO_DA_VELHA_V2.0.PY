import tkinter as tk
from tkinter import messagebox
import random

# Classe para a Inteligência Artificial da Máquina
class CPU:
    def __init__(self, level="easy"):
        self.level = level

    # Escolher jogada dependendo do nível
    def make_move(self, board):
        if self.level == "easy":
            return self.easy_move(board)
        elif self.level == "medium":
            return self.medium_move(board)
        elif self.level == "hard":
            return self.hard_move(board)

    # Jogada aleatória (fácil)
    def easy_move(self, board):
        empty_positions = [i for i, val in enumerate(board) if val == ""]
        return random.choice(empty_positions)

    # Nível médio (algumas tentativas de bloqueio/vitória)
    def medium_move(self, board):
        # Primeiro tenta ganhar
        for i in range(9):
            if board[i] == "":
                board[i] = "O"
                if check_winner(board):
                    board[i] = ""
                    return i
                board[i] = ""
        
        # Depois tenta bloquear o jogador
        for i in range(9):
            if board[i] == "":
                board[i] = "X"
                if check_winner(board):
                    board[i] = ""
                    return i
                board[i] = ""

        # Caso contrário, jogada aleatória
        return self.easy_move(board)

    # Nível difícil (minimax ou estratégia mais avançada)
    def hard_move(self, board):
        # Lógica mais complexa, você pode implementar o algoritmo Minimax aqui
        # Exemplo: Melhorando as jogadas do computador
        return self.medium_move(board)  # Placeholder: usa o nível médio como base

# Classe principal do jogo
class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.current_player = "X"
        self.board = [""] * 9
        self.buttons = []
        self.vs_cpu = False
        self.cpu = None
        self.cpu_level = "easy"
        
        self.setup_ui()

    # Interface do jogo
    def setup_ui(self):
        self.root.title("Jogo da Velha")
        self.root.geometry("400x450")
        self.root.configure(bg="#87CEEB")

        # Título do jogo
        title_label = tk.Label(self.root, text="Jogo da Velha", font=("Helvetica", 24, "bold"), bg="#87CEEB", fg="#fff")
        title_label.pack(pady=20)

        # Frame do tabuleiro
        frame = tk.Frame(self.root)
        for i in range(9):
            button = tk.Button(frame, text="", font=("Helvetica", 20), width=5, height=2, 
                               bg="#f0f0f0", command=lambda i=i: self.button_click(i))
            button.grid(row=i//3, column=i%3, padx=5, pady=5)
            self.buttons.append(button)
        frame.pack()

        # Frame de seleção de modo de jogo
        self.mode_frame = tk.Frame(self.root, bg="#87CEEB")
        mode_label = tk.Label(self.mode_frame, text="Escolha o Modo de Jogo:", font=("Helvetica", 18), bg="#87CEEB", fg="#fff")
        mode_label.pack(pady=20)

        player_vs_player_button = tk.Button(self.mode_frame, text="Jogador vs Jogador", font=("Helvetica", 16), 
                                            bg="#32CD32", fg="#fff", command=lambda: self.choose_mode("player"))
        player_vs_player_button.pack(pady=10)

        player_vs_cpu_button = tk.Button(self.mode_frame, text="Jogador vs CPU", font=("Helvetica", 16), 
                                         bg="#FF6347", fg="#fff", command=self.choose_difficulty)
        player_vs_cpu_button.pack(pady=10)

        self.mode_frame.pack(pady=50)

    # Escolher o modo de jogo
    def choose_mode(self, mode):
        self.vs_cpu = (mode == "cpu")
        self.start_game()

    # Escolher a dificuldade do jogo
    def choose_difficulty(self):
        self.mode_frame.pack_forget()

        difficulty_frame = tk.Frame(self.root, bg="#87CEEB")
        difficulty_label = tk.Label(difficulty_frame, text="Escolha a Dificuldade:", font=("Helvetica", 18), bg="#87CEEB", fg="#fff")
        difficulty_label.pack(pady=20)

        easy_button = tk.Button(difficulty_frame, text="Fácil", font=("Helvetica", 16), bg="#32CD32", fg="#fff", 
                                command=lambda: self.set_difficulty("easy", difficulty_frame))
        easy_button.pack(pady=10)

        medium_button = tk.Button(difficulty_frame, text="Médio", font=("Helvetica", 16), bg="#FFD700", fg="#fff", 
                                  command=lambda: self.set_difficulty("medium", difficulty_frame))
        medium_button.pack(pady=10)

        hard_button = tk.Button(difficulty_frame, text="Difícil", font=("Helvetica", 16), bg="#FF6347", fg="#fff", 
                                command=lambda: self.set_difficulty("hard", difficulty_frame))
        hard_button.pack(pady=10)

        difficulty_frame.pack(pady=50)

    # Configura a dificuldade e inicia o jogo
    def set_difficulty(self, level, frame):
        self.cpu_level = level
        self.cpu = CPU(level=self.cpu_level)
        frame.pack_forget()
        self.start_game()

    # Começar o jogo
    def start_game(self):
        self.board = [""] * 9
        self.current_player = "X"
        for button in self.buttons:
            button.config(text="", bg="#f0f0f0")
        self.mode_frame.pack_forget()

    # Lógica do clique nos botões
    def button_click(self, index):
        if self.board[index] == "":
            self.board[index] = self.current_player
            self.buttons[index].config(text=self.current_player, fg="#00BFFF" if self.current_player == "X" else "#FF6347")

            if check_winner(self.board):
                messagebox.showinfo("Fim de Jogo", f"Jogador {self.current_player} venceu!")
                self.start_game()
            elif "" not in self.board:
                messagebox.showinfo("Fim de Jogo", "Empate!")
                self.start_game()
            else:
                if self.vs_cpu and self.current_player == "X":
                    self.current_player = "O"
                    cpu_move = self.cpu.make_move(self.board)
                    self.button_click(cpu_move)
                else:
                    self.current_player = "O" if self.current_player == "X" else "X"

# Verificar se há vencedor
def check_winner(board):
    win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                      (0, 3, 6), (1, 4, 7), (2, 5, 8),
                      (0, 4, 8), (2, 4, 6)]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] != "":
            return True
    return False

# Iniciar a aplicação
root = tk.Tk()
game = TicTacToe(root)
root.mainloop()
