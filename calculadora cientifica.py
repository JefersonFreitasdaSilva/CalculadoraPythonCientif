from tkinter import *
import math


class Calculator(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        master.title("Calculadora")

        # Criando o display
        self.display = Entry(master, width=20, font=('Arial', 16))
        self.display.grid(row=0, column=0, columnspan=6, padx=5, pady=5)
        self.display.insert(0, "0")

        # Lista de textos dos botões
        button_texts_top = [
            "x!", "nPr", "nCr", "sqrt",
            "x^y", "log", "ln", "1/x"
        ]

        # Criando os botões da parte de cima
        row = 1
        column = 0
        for text in button_texts_top:
            # Adicionando quebra de linha a cada 4 botões, exceto "(" e ")"
            if column % 4 == 0 and column > 0 and text not in ["(", ")"]:
                row += 1
                column = 0

            self.create_button(text, row, column)
            column += 1

        # Lista de textos dos botões
        button_texts = [
            "(", ")", "<-", "C",
            "7", "8", "9", "+",
            "4", "5", "6", "*",
            "1", "2", "3", "-",
            "0", ".", ",", "/", "="
        ]

        # Criando os botões da parte de baixo
        row =3
        column = 0
        for text in button_texts:
            # Adicionando quebra de linha a cada 4 botões, exceto "(" e ")"
            if column % 4 == 0 and column > 0 and text not in ["(", ")"]:
                row += 1
                column = 0

            self.create_button(text, row, column)
            column += 1

    def create_button(self, text, row, column, columnspan=1):
        button = Button(self.master, text=text, width=5, height=2, font=('Arial', 14),
                        command=lambda: self.button_click(text))
        button.grid(row=row, column=column, columnspan=columnspan, padx=5, pady=5)

    def button_click(self, text):
        if text == "C":
            self.display.delete(0, END)
            self.display.insert(0, "0")
        elif text == "<-":
            current = self.display.get()[:-1]  # remove o último caractere
            self.display.delete(0, END)
            self.display.insert(0, current)
        elif text == "=":
            expression = self.display.get()
            expression = expression.replace(",", ".")  # substitui vírgula por ponto
            try:
                result = str(eval(expression))
                self.display.delete(0, END)
                self.display.insert(0, result)
            except:
                self.display.delete(0, END)
                self.display.insert(0, "Erro")

        # Operações matemáticas
        elif text == "x!":
            try:
                result = str(math.factorial(int(self.display.get())))
                self.display.delete(0, END)
                self.display.insert(0, result)
            except:
                self.display.delete(0, END)
                self.display.insert(0, "Erro")
        elif text == "nPr":
            self.display.insert(END, "P")
        elif text == "nCr":
            self.display.insert(END, "C")
        elif text == "sqrt":
            try:
                result = str(math.sqrt(float(self.display.get())))
                self.display.delete(0, END)
                self.display.insert(0, result)
            except:
                self.display.delete(0, END)
                self.display.insert(0, "Erro")
        elif text == "x^y":
            self.display.insert(END, "**")
        elif text == "log":
            self.display.insert(END, "log10")
        elif text == "ln":
            self.display.insert(END, "log")
        elif text == "1/x":
            try:
                result = str(1 / float(self.display.get()))
                self.display.delete(0, END)
                self.display.insert(0, result)
            except:
                self.display.delete(0, END)
                self.display.insert(0, "Erro")

        # Adicionando números e operadores
        else:
            # Se a expressão começar com erro, substitui o 0 pelo número ou operador pressionado
            if self.display.get() == "Erro":
                self.display.delete(0, END)
                self.display.insert(END, text)
            else:
                self.display.insert(END, text)


# Criando a janela principal e iniciando a aplicação
root = Tk()
calculator = Calculator(root)
root.mainloop()