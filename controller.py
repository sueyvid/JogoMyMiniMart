from model import *
from view import *


class Controller:
    def __init__(self):
        self.personagem = Personagem()
        self.macieira = Macieira()
        self.prateleira_maça = PrateleiraMaças()
        self.view = None

    def inicia(self, v):
        self.view = v
        self._configura()

    def _configura(self):
        self.view.maça_pegar.command(self.pegar_maça)
        self.view.vender.command(self.vender)
        self.view.maça_colocar.command(self.colocar_maça)
        self.view.after(1000, self.nascer)
        self.view.after(1000, self.novo_cliente)
        self.view.after(100, self.comprou)

    def colocar_maça(self):
        try:
            self.personagem.soltar('maçã')
            self.prateleira_maça.armazenar('maçã')
            self.view.inventario.texto = self.personagem.inventario_qtd_items()
            self.view.maças.texto = self.prateleira_maça.inventario_qtd_items()
        except:
            print('erro armazenar!')
    
    def comprou(self):
        try:
            qtd = self.prateleira_maça.fila.primeiro().comprar
            self.prateleira_maça.retirar('maçã', qtd)
            self.prateleira_maça.sair()
            self.personagem.ganhar(qtd)
            self.view.maças.texto = self.prateleira_maça.inventario_qtd_items()
            self.view.dinheiro.texto = self.personagem.qtd_dinheiro()
            print('comprou')
        except:
            None
        self.view.after(100, self.comprou)

    def novo_cliente(self):
        try:
            self.prateleira_maça.esperar()
        except:
            print('erro cliente!')
        print('----- Novo Cliente -----')
        for i in self.prateleira_maça.retorna_fila():
            print(i)
        t = randint(1000, 5000)
        self.view.after(t, self.novo_cliente)
    
    def nascer(self):
        try:
            self.macieira.armazenar('maçã')
            self.view.maça.texto = self.macieira.inventario_qtd_items()
        except:
            None
        self.view.after(1000, self.nascer)

    def vender(self):
        try:
            self.prateleira_maça.retirar('maçã')
            self.personagem.ganhar(1)
            self.view.maças.texto = self.prateleira_maça.inventario_qtd_items()
            self.view.dinheiro.texto = self.personagem.qtd_dinheiro()
        except:
            print('erro venda!')

    def pegar_maça(self):
        try:
            self.macieira.retirar('maçã')
            self.personagem.pegar('maçã')
            maça = self.view.maça.texto
            self.view.maça.texto = str(int(maça)-1)
            inventario = self.view.inventario.texto
            self.view.inventario.texto = str(int(inventario)+1)
        except:
            print('erro colher!')

def main():
    v = View()
    c = Controller()
    c.inicia(v)
    v.mainloop()

if __name__ == '__main__':
    main()