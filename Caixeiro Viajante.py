
import turtle
import random

#pontos = int(input('Digite Quantos pontos você quer: '))

pontos = 50

cidades = [(random.randint(-200, 200), random.randint(-200, 200)) for _ in range(pontos)]

def desenhar_cidades():
    turtle.penup()
    for cidade in cidades:
        turtle.goto(cidade)
        turtle.dot(5)
    turtle.hideturtle()

def desenhar_caminho(caminho):
    turtle.penup()
    turtle.goto(cidades[caminho[0]])
    turtle.pendown()
    turtle.color('red')
    for cidade in caminho[1:]:
        turtle.goto(cidades[cidade])
    turtle.goto(cidades[caminho[0]])
    turtle.color('black')

def main():
    # Supondo que você já tenha uma função para resolver o TSP e obter o caminho
    caminho = list(range(pontos))  # Exemplo de caminho inicial (apenas visitação sequencial)
    random.shuffle(caminho)  # Embaralhar o caminho
    turtle.speed(5)
    desenhar_cidades()
    desenhar_caminho(caminho)
    turtle.done()

if __name__ == '__main__':
    main()
