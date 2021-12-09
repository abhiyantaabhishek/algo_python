#%%
from collections import defaultdict
from collections import deque
import networkx as nx
import matplotlib.pyplot as plt

#%%
class Graph:
    def __init__(self) -> None:
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def get_edges(self):
        edges = set()
        for key, val in self.graph.items():
            for v in val:
                edges.add((key, v))
        return list(edges)

    def visualise_graph(self):
        G = nx.DiGraph()
        G.add_edges_from(self.get_edges())
        # nx.draw_networkx(G)
        # plt.show()
        my_pos = nx.spring_layout(G, seed=100)
        nx.draw(
            G,
            pos=my_pos,
            with_labels=True,
            node_color="orange",
            node_size=400,
            edge_color="black",
            linewidths=1,
            font_size=15,
        )
        plt.show()

    def dfs(self, v, visited_node=set()):
        print(v)
        visited_node.add(v)
        for neighbours in self.graph[v]:
            if neighbours not in visited_node:
                self.dfs(neighbours, visited_node)

    def bfs(self, v):
        queue = deque()
        visited = set()
        queue.append(v)
        while len(queue) != 0:
            v = queue.popleft()
            print(v)
            visited.add(v)
            for neighbours in self.graph[v]:
                if neighbours not in visited:
                    queue.append(neighbours)


# %%
graph = Graph()
graph.add_edge("A", "B")
graph.add_edge("A", "F")
graph.add_edge("A", "C")
graph.add_edge("C", "D")
graph.add_edge("D", "A")
graph.add_edge("B", "A")
# %%
graph.bfs("B")
# %%
graph.visualise_graph()
