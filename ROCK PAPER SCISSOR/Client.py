import tkinter as tk
from tkinter import messagebox
import socket

def send_choice(choice):
    client_socket.send(choice.encode('utf-8'))
    result = client_socket.recv(1024).decode('utf-8')
    messagebox.showinfo("Result", result)

def play_rock():
    send_choice("Rock")

def play_paper():
    send_choice("Paper")

def play_scissors():
    send_choice("Scissors")

root = tk.Tk()
root.title("Rock, Paper, Scissors")

rock_button = tk.Button(root, text="Rock", command=play_rock, width=20, height=3)
rock_button.pack(pady=10)

paper_button = tk.Button(root, text="Paper", command=play_paper, width=20, height=3)
paper_button.pack(pady=10)

scissors_button = tk.Button(root, text="Scissors", command=play_scissors, width=20, height=3)
scissors_button.pack(pady=10)

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('127.0.0.1', 5005))

root.mainloop()