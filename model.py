from random import randint


class ExcecaoJogo(Exception):
    pass

class Lotado(ExcecaoJogo):
    pass

class Vazio(ExcecaoJogo):
    pass

class Maximo(ExcecaoJogo):
    pass

class Minimo(ExcecaoJogo):
    pass

class Fila:
    def __init__(self):
        self._fila = list()

    def entra(self, i):
        self._fila.append(i)

    def sai(self):
        self._fila.pop(0)

    def retorna_fila(self):
        return self._fila

    def primeiro(self):
        return self._fila[0]

class Inventario:
    def __init__(self, tamanho):
        self.tipo = dict()
        self.tamanho = tamanho
        self.espacos = self.tamanho

    def armazenar(self, item):
        try:
            if self.espacos < 1:
                raise Lotado()
            self.espacos -= 1
            if item not in self.tipo.keys():
                self.tipo[item] = 0
            self.tipo[item] += 1
        except:
            raise Lotado()
    
    def retirar(self, item, qtd=1):
        try:
            if self.espacos+qtd >= self.tamanho+1:
                raise Vazio()
            self.espacos += qtd
            self.tipo[item] -= qtd
        except:
            raise Vazio()

    def inventario_qtd_items(self):
        return self.tamanho - self.espacos

    def __str__(self):
        s = 'Inventário:\n'
        for item, qtd in self.tipo.items():
            s += f'{item}: {qtd}\n'
        return s

class Personagem:
    def __init__(self):
        self.segurando = Inventario(4)
        self.dinheiro = 0

    def pegar(self, i):
        self.segurando.armazenar(i)

    def soltar(self, i):
        self.segurando.retirar(i)

    def inventario_qtd_items(self):
        return self.segurando.tamanho - self.segurando.espacos

    def ganhar(self, d):
        self.dinheiro += d

    def gastar(self, d):
        self.dinheiro -= d

    def qtd_dinheiro(self):
        return self.dinheiro

    def ver_inventario(self):
        print(self.segurando)

class PrateleiraMaças(Inventario):
    def __init__(self):
        super().__init__(15)
        self.fila = Fila()

    def esperar(self):
        try:
            tam_fila = len(self.fila.retorna_fila())
            if tam_fila == 4:
                raise Lotado()
            p = 'Pessoa '
            p += str(tam_fila)
            c = Cliente(p)
            self.fila.entra(c)
        except:
            print('Lotado')

    def sair(self):
        self.fila.sai()

    def retorna_fila(self):
        return self.fila.retorna_fila()

class Macieira(Inventario):
    def __init__(self):
        super().__init__(4)

class Cliente:
    def __init__(self, nome):
        self.nome = nome
        self.comprar = randint(1, 3)

    def quer_comprar(self):
        return self.comprar

    def __str__(self):
        return f'{self.nome}: quer comprar {self.comprar} maçãs'

def main():
    p = Personagem()
    try:
        p.pegar('maçã')
        p.pegar('maçã')
        p.pegar('maçã')
        p.pegar('leite')
        p.pegar('maçã')
        p.soltar('maçã')
    except:
        print('erro')
    p.ver_inventario()

if __name__ == '__main__':
    main()