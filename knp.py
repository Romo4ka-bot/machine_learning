import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

def create_clusters(matrix_smallest_way):
    maxim = 0
    i_max, j_max = -1, -1
    for i in range(n):
        for j in range(i + 1, n):
            if matrix_smallest_way[i][j] == 1:
                if first_matrix[i][j] > maxim:
                    maxim = first_matrix[i][j]
                    i_max, j_max = i, j
    matrix_smallest_way[i_max][j_max] = 0
    matrix_smallest_way[j_max][i_max] = 0
    return matrix_smallest_way

def create_first_edge(matrix_smallest_way):
    minim = first_matrix[0][1]
    i_min, j_min = 0, 1
    for i in range(n):
        for j in range(i + 1, n):
            if minim > first_matrix[i][j] != 0:
                minim = first_matrix[i][j]
                i_min, j_min = i, j
    matrix_smallest_way[i_min][j_min] = matrix_smallest_way[j_min][i_min] = 1
    matrix_smallest_way[i_min][i_min] = matrix_smallest_way[j_min][j_min] = -1
    return matrix_smallest_way

def create_next_edges(matrix_smallest_way):
    minim = None
    i_min, j_min = 0, 1
    for i in range(n):
        if matrix_smallest_way[i][i] == -1:
            for j in range(n):
                if matrix_smallest_way[j][j] == 0:
                    if minim is None or (minim > first_matrix[i][j] != 0):
                        minim = first_matrix[i][j]
                        i_min, j_min = i, j
    matrix_smallest_way[i_min][j_min] = matrix_smallest_way[j_min][i_min] = 1
    matrix_smallest_way[i_min][i_min] = matrix_smallest_way[j_min][j_min] = -1
    return matrix_smallest_way

def create_graph(matrix_smallest_way, begin_matrix, n):
    result_graph = np.zeros((n, n))

    for i in range(n):
        for j in range(n):
            if matrix_smallest_way[i][j] != -1:
                result_graph[i][j] = matrix_smallest_way[i][j] * begin_matrix[i][j]
            else:
                result_graph[i][j] = -1

    G = nx.from_numpy_matrix(result_graph, create_using=nx.DiGraph)
    layout = nx.spring_layout(G)
    nx.draw(G, layout, node_color='lightgreen', edge_color='b')
    nx.draw_networkx_edge_labels(G, pos=layout)
    plt.show()

def knp(matrix, n, k):
    matrix_smallest_way = np.zeros((n, n))
    matrix_smallest_way = create_first_edge(matrix_smallest_way)
    for i in range(n - 2):
        matrix_smallest_way = create_next_edges(matrix_smallest_way)

    print("Вывод графа кратчайшего пути")
    result_graph = np.zeros((n, n))

    for i in range(n):
        for j in range(n):
            if matrix_smallest_way[i][j] != -1:
                result_graph[i][j] = matrix_smallest_way[i][j] * first_matrix[i][j]
            else:
                result_graph[i][j] = -1

    G = nx.from_numpy_matrix(result_graph, create_using=nx.DiGraph)
    layout = nx.spring_layout(G)
    nx.draw(G, layout, node_color='lightgreen', edge_color='b')
    nx.draw_networkx_edge_labels(G, pos=layout)
    plt.show()


    for i in range(k - 1):
        matrix_smallest_way = create_clusters(matrix_smallest_way)

    print("Путь в графе с разделением на кластеры")
    print(matrix_smallest_way)

    create_graph(matrix_smallest_way, matrix, n)


if __name__ == '__main__':
    n, k = 5, 3
    first_matrix = np.zeros((n, n))

    for i in range(n):
        for j in range(i + 1, n):
          if i == 3:
            first_matrix[i][j] = first_matrix[j][i] = 0
          else:
            first_matrix[i][j] = first_matrix[j][i] = np.random.randint(1, 100)
    print(first_matrix)

    G = nx.from_numpy_matrix(first_matrix, create_using=nx.DiGraph)
    layout = nx.spring_layout(G)
    nx.draw(G, layout, node_color='lightgreen', edge_color='b')
    nx.draw_networkx_edge_labels(G, pos=layout)
    plt.show()

    knp(first_matrix, n, k)
