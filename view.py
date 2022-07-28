from meu_tk import *


class View(Janela):
    def __init__(self):
        super().__init__('My Mini Mart', 1, 2)
        f1 = Frame(self, 1, 1, (0, 0), bd=10, relief=tk.SUNKEN)
        f2 = Frame(self, 1, 1, (0, 1), bd=10, relief=tk.SUNKEN)
        f3 = Frame(self, 1, 1, (0, 2), bd=10, relief=tk.SUNKEN)

        l1 = Label(f1, 'Inventário', (0, 0))
        self.inventario = Label(f1, '0', (1, 0))
        self.vender = Button(f1, 'Vender', (2, 0))
        self.moeda = Label(f1, 'R$ ', (2, 1))
        self.dinheiro = Label(f1, '0', (2, 2))

        l2 = Label(f2, 'Macieira', (0, 0))
        self.maça = Label(f2, '0', (1, 0))
        self.maça_pegar = Button(f2, 'Pegar', (2, 0))

        l3 = Label(f3, 'Prateleira de maçã', (0, 0))
        self.maças = Label(f3, '0', (1, 0))
        self.maça_colocar = Button(f3, 'Colocar', (2, 0))

        l = [l1, l2, self.inventario, self.vender, self.maça, self.maça_pegar, l3, self.maças, self.maça_colocar, self.moeda, self.dinheiro]
        for i in l:
            i.font('', 18)

def main():
    v = View()
    v.mainloop()

if __name__ == '__main__':
    main()