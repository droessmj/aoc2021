import sys
import copy

class Edge:
    node1 = None
    node2 = None

    def __init__(self, node1, node2):
        self.node1 = node1
        self.node2 = node2

    def __hash__(self):
        return hash((self.node1,self.node2))

    def __str__(self):
        return f"\n{self.node1}-{self.node2}"

    def __repr__(self):
        return f"\n{self.node1}-{self.node2}"

    def  __eq__(self, other):
        return self.node1 == other.node1 and self.node2 == other.node2

class Node:
    val = str
    big = False

    def __init__(self, val):
        self.val = val
        self.big = val.isupper()

    def __hash__(self):
        return hash((self.val))

    def __str__(self):
        return f"{self.val}:{self.big}"

    def __repr__(self):
        return f"{self.val}:{self.big}"

    def  __eq__(self, other):
        return self.val == other

class Route:
    nodes = []

    def __init__(self, node = None):
        self.nodes = []
        if node:
            self.nodes.append(node)

    def add_node(self,node):
        self.nodes.append(node)

    def __str__(self):
        r = ''
        for node in self.nodes:
            if node.val != 'end':
                r += f"{node.val}->"
            else:
                r += f"{node.val}"
        return r

    def __repr__(self):
        return self.__str__()

    def  __eq__(self, other):
        return self.val == other

class Graph:
    nodes = []
    edges = []
    map = {} # dictionary of node->various peer nodes
    routes = [] # list of routes

    def __init__(self):
        self.nodes = []
        self.edges = []
        self.map = {}
        self.routes = []

    def add_node(self, node):
        if node not in self.nodes: # create node
            self.nodes.append(node)

    def add_edge(self,n1,n2):
        edge = Edge(n1,n2)
        if edge not in self.edges:
            self.edges.append(edge)

    def build_map(self):
        for edge in self.edges:
            if edge.node1 not in self.map:
                self.map[edge.node1] = {edge.node2}
            else:
                self.map[edge.node1].add(edge.node2)
            if edge.node2 not in self.map:
                self.map[edge.node2] = {edge.node1}
            else:
                self.map[edge.node2].add(edge.node1)

    def add_nodes_to_route(self, route, cur_node):
        for next_node in self.map[cur_node]:
            route2 = copy.deepcopy(route)

            if next_node in route2.nodes and not next_node.big:
                # if our next node is already in our list and isn't a big node
                # we won't continue
                pass
            else:
                route2.add_node(next_node)
                if route2.nodes[-1] == 'end':
                    self.routes.append(route2)
                else:
                    self.add_nodes_to_route(route2, next_node)

    def build_routes(self):
        cur_node = Node('start')
        route = Route(cur_node)
        self.add_nodes_to_route(route, cur_node)
        print(self.routes)
        

    def get_route_count(self):
        self.build_routes()
        return len(self.routes)

    def __str__(self):
        return f"Nodes: {self.nodes}\nEdges: \n{self.edges}"

    def __repr__(self):
        return f"Nodes: {self.nodes}\nEdges: \n{self.edges}"

in_file = 'test'
if len(sys.argv) > 1:
    in_file = sys.argv[1]

graph = Graph()
with open(f"./{in_file}.txt") as f:
    for line in f:
        line = line.strip()
        parts = line.split('-')
        n1 = Node(parts[0])
        n2 = Node(parts[1])
        graph.add_node(n1)
        graph.add_node(n2)
        graph.add_edge(n1,n2)
graph.build_map()
#print(graph.map)

print(graph.get_route_count())