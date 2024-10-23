import tkinter as tk
from tkinter import messagebox
import random

# Variáveis globais
current_player = "X"
board = [""] * 9
buttons = []
vs_cpu = False

# Função para resetar o jogo
def reset_game():
    global board, current_player, buttons
    current_player = "X"
    board = [""] * 9
    for button in buttons:
        button.config(text="", bg="#f0f0f0")

# Função de controle de clique
def button_click(index):
    global current_player, vs_cpu
    if board[index] == "":
        board[index] = current_player
        buttons[index].config(text=current_player, fg="#00BFFF" if current_player == "X" else "#FF6347")
        
        if check_winner():
            messagebox.showinfo("Fim de Jogo", f"Jogador {current_player} venceu!")
            reset_game()
        elif "" not in board:
            messagebox.showinfo("Fim de Jogo", "Empate!")
            reset_game()
        else:
            if vs_cpu and current_player == "X":
                current_player = "O"
                cpu_play()
            else:
                current_player = "O" if current_player == "X" else "X"
    else:
        messagebox.showwarning("Jogada Inválida", "Escolha outra casa!")

# Função para jogada da CPU (jogador automático)
def cpu_play():
    global current_player
    empty_positions = [i for i, val in enumerate(board) if val == ""]
    if empty_positions:
        index = random.choice(empty_positions)
        board[index] = "O"
        buttons[index].config(text="O", fg="#FF6347")
        
        if check_winner():
            messagebox.showinfo("Fim de Jogo", "A CPU venceu!")
            reset_game()
        elif "" not in board:
            messagebox.showinfo("Fim de Jogo", "Empate!")
            reset_game()
        else:
            current_player = "X"

# Função para verificar a vitória
def check_winner():
    win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                      (0, 3, 6), (1, 4, 7), (2, 5, 8),
                      (0, 4, 8), (2, 4, 6)]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] != "":
            return True
    return False

# Função para escolher o modo de jogo
def choose_mode(mode):
    global vs_cpu
    vs_cpu = (mode == "cpu")
    start_game()

# Iniciar o jogo
def start_game():
    # Criar o tabuleiro de jogo
    global buttons
    root.geometry("400x450")
    frame.pack()
    title_label.config(text="Jogo da Velha")
    mode_frame.pack_forget()
    reset_game()

# Configuração da janela principal
root = tk.Tk()
root.title("Jogo da Velha")
root.geometry("400x450")
root.configure(bg="#87CEEB")

# Título do jogo
title_label = tk.Label(root, text="Jogo da Velha", font=("Helvetica", 24, "bold"), bg="#87CEEB", fg="#fff")
title_label.pack(pady=20)

# Frame para o tabuleiro
frame = tk.Frame(root)

# Criar os botões do tabuleiro
for i in range(9):
    button = tk.Button(frame, text="", font=("Helvetica", 20), width=5, height=2, 
                       bg="#f0f0f0", command=lambda i=i: button_click(i))
    button.grid(row=i//3, column=i%3, padx=5, pady=5)
    buttons.append(button)

# Frame de seleção de modo de jogo
mode_frame = tk.Frame(root, bg="#87CEEB")
mode_label = tk.Label(mode_frame, text="Escolha o Modo de Jogo:", font=("Helvetica", 18), bg="#87CEEB", fg="#fff")
mode_label.pack(pady=20)

player_vs_player_button = tk.Button(mode_frame, text="Jogador vs Jogador", font=("Helvetica", 16), 
                                    bg="#32CD32", fg="#fff", command=lambda: choose_mode("player"))
player_vs_player_button.pack(pady=10)

player_vs_cpu_button = tk.Button(mode_frame, text="Jogador vs CPU", font=("Helvetica", 16), 
                                 bg="#FF6347", fg="#fff", command=lambda: choose_mode("cpu"))
player_vs_cpu_button.pack(pady=10)

mode_frame.pack(pady=50)

# Iniciar o loop do tkinter
root.mainloop()
