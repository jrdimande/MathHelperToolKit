# módulos e funções
import math
from math import sqrt
import random
from time import sleep


def line():
    print('_' * 115)


def time():
    sleep(2)


def menu():
    print('Em o que podemos ajudar-te?')
    print('__________________________________________________________________')
    print('|A=tabuada de x                    |B=raiz quadrada e cúbica de x |')
    print('|__________________________________|______________________________|')
    print('|C=logaritmo de x na base 2        |D=equação do segundo grau     |')
    print('|__________________________________|______________________________|')
    print('|E=sistema de duas equações        |F=sistema de três equações    |')
    print('|__________________________________|______________________________|')
    print('|G=calculadora de média aritmética |Q=sair                        |')
    print('|__________________________________|______________________________|')
    print('Clique Enter para continuar')


def problem():
    print('Ocorreu um problema!!')
    print('Tente novamente')


def fin():
    line()
    print('Obrigado por usar o programa, volte sempre :)')
    print('Entre em contato com o desenvolvedor pelo e-mail: timoteojrdimande@gmail.com')
    line()


def solproblem():
    print('O sistema não tem solução')


def handle_tabuada():
    try:
        line()
        u = int(input('Digite um número para ver a sua tabuada: '))
        for i in range(1, 13):
            print('{} x {} = {}'.format(u, i, u * i))
    except ValueError:
        print('Ocorreu um erro! Tente novamente.')
    finally:
        fin()


def handle_raizes():
    try:
        line()
        r = int(input('Digite um número para ver a sua raiz quadrada e cúbica: '))
        raizq = math.sqrt(r)
        raizc = r ** (1 / 3)
        line()
        print('A raiz quadrada de {} é {} e a raiz cúbica é {}'.format(r, raizq, raizc))
    except ValueError:
        problem()
    finally:
        fin()


def handle_logaritmo():
    try:
        line()
        u = int(input('Digite um número para ver o logaritmo na base 2: '))
        log = math.log2(u)
        line()
        print('O logaritmo de {} na base 2 é {}'.format(u, log))
    except ValueError:
        problem()
    finally:
        fin()


def handle_equacao2grau():
    try:
        a = int(input('Introduza o coeficiente de a: '))
        b = int(input('Introduza o coeficiente de b: '))
        c = int(input('Introduza o coeficiente de c: '))
        d = b ** 2 - 4 * a * c
        if d < 0:
            solproblem()
        else:
            d1 = sqrt(d)
            v1 = (-b + d1) / (2 * a)
            v2 = (-b - d1) / (2 * a)
            line()
            print('As soluções da equação são x1={} e x2={}'.format(v1, v2))
    except ValueError:
        problem()
    except ZeroDivisionError:
        solproblem()
    finally:
        fin()


def handle_sistema2equacoes():
    try:
        x = int(input('Introduza o coeficiente de x da primeira equação: '))
        y = int(input('Introduza o coeficiente de y da primeira equação: '))
        i = int(input('Introduza o termo independente da primeira equação: '))
        x1 = int(input('Introduza o coeficiente de x da segunda equação: '))
        y1 = int(input('Introduza o coeficiente de y da segunda equação: '))
        i1 = int(input('Introduza o termo independente da segunda equação: '))

        d = (x * y1) - (x1 * y)
        dx = (i * y1) - (i1 * y)
        dy = (x * i1) - (x1 * i)

        b = dx / d
        c = dy / d

        line()
        print('As soluções das equações são x = {} e y = {}'.format(b, c))
    except ZeroDivisionError:
        solproblem()
    except ValueError:
        problem()
    finally:
        fin()


def handle_sistema3equacoes():
    try:
        X1 = int(input('Digite o coeficiente de x da primeira equação: '))
        Y1 = int(input('Digite o coeficiente de y da primeira equação: '))
        Z1 = int(input('Digite o coeficiente de z da primeira equação: '))
        I1 = int(input('Digite o valor do termo independente da primeira equação: '))
        line()

        X2 = int(input('Digite o coeficiente de x da segunda equação: '))
        Y2 = int(input('Digite o coeficiente de y da segunda equação: '))
        Z2 = int(input('Digite o coeficiente de z da segunda equação: '))
        I2 = int(input('Digite o valor do termo independente da segunda equação: '))
        line()

        X3 = int(input('Digite o coeficiente de x da terceira equação: '))
        Y3 = int(input('Digite o coeficiente de y da terceira equação: '))
        Z3 = int(input('Digite o coeficiente de z da terceira equação: '))
        I3 = int(input('Digite o valor do termo independente da terceira equação: '))

        D = (X1 * Y2 * Z3 + Y1 * Z2 * X3 + Z1 * X2 * Y3) - (X3 * Y2 * Z1 + Y3 * Z2 * X1 + Z3 * X2 * Y1)
        DX = (I1 * Y2 * Z3 + Y1 * Z2 * I3 + Z1 * I2 * Y3) - (I3 * Y2 * Z1 + Y3 * Z2 * I1 + Z3 * I2 * Y1)
        DY = (X1 * I2 * Z3 + I1 * Z2 * X3 + Z1 * X2 * I3) - (X3 * I2 * Z1 + I3 * Z2 * X1 + Z3 * X2 * I1)
        DZ = (X1 * Y2 * I3 + Y1 * I2 * X3 + I1 * X2 * Y3) - (X3 * Y2 * I1 + Y3 * I2 * X1 + I3 * X2 * Y1)

        if D == 0:
            print('Discriminante é 0')
        else:
            X = DX / D
            Y = DY / D
            Z = DZ / D
            line()
            print('A solução é x={}, y={}, z={}'.format(X, Y, Z))
    except ZeroDivisionError:
        print('O sistema não tem solução')
    except ValueError:
        problem()
    finally:
        fin()


def handle_media():
    try:
        print('Coloque as suas notas de cada avaliação!')
        primeira = int(input('Primeira avaliação: '))
        segunda = int(input('Segunda avaliação: '))
        terceira = int(input('Terceira avaliação: '))

        S = primeira + segunda + terceira
        resultado = S / 3
        line()
        print('A sua média é {}'.format(resultado))

        if resultado < 7:
            print('Reprovado')
        else:
            print('Aprovado')
    except ValueError:
        problem()
    finally:
        fin()


# Loop principal do programa
while True:
    menu()
    user = input('Escolha uma letra que corresponde a um problema ou Q para sair: ').strip().upper()

    if user == 'A':
        handle_tabuada()
    elif user == 'B':
        handle_raizes()
    elif user == 'C':
        handle_logaritmo()
    elif user == 'D':
        handle_equacao2grau()
    elif user == 'E':
        handle_sistema2equacoes()
    elif user == 'F':
        handle_sistema3equacoes()
    elif user == 'G':
        handle_media()
    elif user == 'Q':
        fin()
        break
    else:
        print('Escolha uma letra válida.')
