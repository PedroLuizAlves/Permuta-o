# Importe a biblioteca NetworkX
import networkx as nx
import matplotlib.pyplot as plt

# Crie um objeto de grafo
grafo = nx.Graph()

# Adicione 5 vértices com nomes de pessoas
nomes = ["Predo", "Teus", "Muris", "Julia", "Nath"]
grafo.add_nodes_from(nomes)

# Adicione algumas arestas (conexões entre vértices)
grafo.add_edges_from([(nomes[0], nomes[1]), (nomes[1], nomes[2]), (nomes[2], nomes[3]), (nomes[3], nomes[4]), (nomes[4], nomes[0])])

# Visualize o grafo
nx.draw(grafo, with_labels=True, node_size=500, node_color='skyblue', font_size=10)
plt.show()
