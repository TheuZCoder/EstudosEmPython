import tkinter as tk
from tkinter import messagebox
import random
import threading
import time

class JogoBatalhaNaval:
    def __init__(self, root):
        self.root = root
        self.root.title("Batalha Naval")
        self.tabuleiro = [['~' for _ in range(10)] for _ in range(10)]

        self.botao_tabuleiro = [[None for _ in range(10)] for _ in range(10)]

        self.criar_tabuleiro()
        self.posicionar_navios()
        
    def criar_tabuleiro(self):
        # Rótulos para coordenadas
        for i in range(10):
            lbl_coluna = tk.Label(self.root, text=chr(ord('A') + i))
            lbl_coluna.grid(row=0, column=i+1)

            lbl_linha = tk.Label(self.root, text=str(i))
            lbl_linha.grid(row=i+1, column=0)

            for j in range(10):
                self.botao_tabuleiro[i][j] = tk.Button(self.root, text='', width=3, height=1,
                                                       command=lambda i=i, j=j: self.clicar_botao(i, j))
                self.botao_tabuleiro[i][j].grid(row=i+1, column=j+1)

    def posicionar_navios(self):
        self.posicionar_navio('O', 5)  # Navio de tamanho 5
        self.posicionar_navio('X', 3)  # Navio de tamanho 3
        self.posicionar_navio('-', 2)  # Navio de tamanho 2

    def posicionar_navio(self, simbolo, tamanho):
        for _ in range(5):  # Tente posicionar 5 vezes
            orientacao = random.choice(['horizontal', 'vertical'])
            x = random.randint(0, 9)
            y = random.randint(0, 9)

            if orientacao == 'horizontal' and y + tamanho <= 10:
                posicoes = [(x, y + i) for i in range(tamanho)]
            elif orientacao == 'vertical' and x + tamanho <= 10:
                posicoes = [(x + i, y) for i in range(tamanho)]
            else:
                continue  # Tente novamente se não puder posicionar

            colisao = any(self.tabuleiro[i][j] != '~' for i, j in posicoes)
            if not colisao:
                for i, j in posicoes:
                    self.tabuleiro[i][j] = simbolo
                return

    def clicar_botao(self, linha, coluna):
        if self.tabuleiro[linha][coluna] == '~':
            self.animate_erro(linha, coluna)
        elif self.tabuleiro[linha][coluna] in ['O', 'X', '-']:
            self.animate_afundamento(linha, coluna)

    def animate_erro(self, linha, coluna):
        def animate():
            for i in range(5):  # Simulação de 5 frames de animação
                self.botao_tabuleiro[linha][coluna].config(bg='gray')
                self.root.update()
                time.sleep(0.2)
                self.botao_tabuleiro[linha][coluna].config(bg='SystemButtonFace')
                self.root.update()
                time.sleep(0.2)

            self.botao_tabuleiro[linha][coluna].config(text='-', state='disabled')
            messagebox.showinfo("Erro", "Ops! Você errou o tiro.")
            
        # Iniciar a thread de animação
        threading.Thread(target=animate).start()

    def animate_afundamento(self, linha, coluna):
        def animate():
            simbolo = self.tabuleiro[linha][coluna]
            afundado_horizontal = all(simbolo == self.tabuleiro[linha][j] for j in range(10))
            afundado_vertical = all(simbolo == self.tabuleiro[i][coluna] for i in range(10))

            for i in range(5):  # Simulação de 5 frames de animação
                self.botao_tabuleiro[linha][coluna].config(bg='red')
                self.root.update()
                time.sleep(0.2)
                self.botao_tabuleiro[linha][coluna].config(bg='SystemButtonFace')
                self.root.update()
                time.sleep(0.2)

            self.botao_tabuleiro[linha][coluna].config(text='X', state='disabled')

            if afundado_horizontal or afundado_vertical:
                messagebox.showinfo("Parabéns", f"Você afundou um navio de tamanho {len(simbolo)}!")
            
        # Iniciar a thread de animação
        threading.Thread(target=animate).start()

if __name__ == "__main__":
    root = tk.Tk()
    jogo = JogoBatalhaNaval(root)
    root.mainloop()
