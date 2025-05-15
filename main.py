import matplotlib.pyplot as plt

def create_graph(titulo, eixo_x, eixo_y):
    plt.title(titulo)
    plt.xlabel(eixo_x)
    plt.ylabel(eixo_y)

media_cafes = 4
valor_tomado_hoje = [0, 1, 2, 3, 4]

arr_cafe_tomado = []

for x in range(len(valor_tomado_hoje)):
    tomados = valor_tomado_hoje[x] - media_cafes
    arr_cafe_tomado.append(tomados)

create_graph(titulo='Café', eixo_x='Tomados', eixo_y='Média')

plt.scatter(arr_cafe_tomado, valor_tomado_hoje, color='black')
plt.plot(arr_cafe_tomado, valor_tomado_hoje, color='blue')

plt.ylim(0, 10)

plt.show()
