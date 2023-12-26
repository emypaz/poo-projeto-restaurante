import tkinter as tk
from tkinter import messagebox
from produto import Produto
from menu import Menu
from pedido import Pedido

class interfaceGrafica:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Pedidos")

        self.opcao_var = tk.StringVar()

        self.criar_interface()

    def criar_interface(self):
        tk.Label(self.root, text="Escolha uma opção:").pack()

        opcoes = [("Adicionar Produtos", "1"), ("Entrar no Menu", "2"), ("Fazer Pedido", "3"), ("Sair do Programa", "0")]

        for texto, valor in opcoes:
            tk.Radiobutton(self.root, text=texto, variable=self.opcao_var, value=valor).pack()

        tk.Button(self.root, text="OK", command=self.processar_opcao).pack()

    def processar_opcao(self):
        opcao = self.opcao_var.get()

        if opcao == "1":
            self.adicionar_produtos()
        elif opcao == "2":
            self.entrar_no_menu()
        elif opcao == "3":
            self.fazer_pedido()
        elif opcao == "0":
            self.root.destroy()
        else:
            messagebox.showinfo("Opção Inválida", "Por favor, escolha uma opção válida.")

    def adicionar_produtos(self):
        produto = Produto('000', 'produtos', '00.00')
        produto.addProdutos()

    def entrar_no_menu(self):
        menu = Menu()

    def fazer_pedido(self):
        pedido = Pedido('00', 'clientes', '000', 'quantidade')
        pedido.mostrarCardapio()
        pedido.fazerPedido('00', 'Cliente')

    

if __name__ == "__main__":
    root = tk.Tk()
    app = interfaceGrafica(root)
    root.mainloop()
