#!/usr/bin/env python3


class Graph(object):

    def __init__(self, vertices=set(), edges=set()):
        self.vertices = vertices
        self.edges = edges

    def add_vertex(self, v):
        self.vertices.add(v)

    def add_edge(self, e):
        self.vertices.add(e[0])
        self.vertices.add(e[1])
        self.edges.add(e)


class DeBruijn(Graph):

    def __init__(self, kmerset):
        super().__init__(kmerset)
        # Dict is simpler than set if graph is directed and vertex degrees == 1.
        self._directed_edges = dict()
        for i in self.vertices:
            for j in self.vertices:
                if i == j:
                    continue
                if i[1:] == j[:-1]:
                    self.add_edge((i, j))
                    self._directed_edges[i] = j
    
    def get_cyclic_superstring(self):
        """Returns shortest possible cyclic superstring.
        Assumes/requires that the graph consists of a single cycle.
        """
        startvertex = list(self.vertices)[0]
        superstring = startvertex[-1]
        nextvertex = self._directed_edges[startvertex]
        
        while nextvertex != startvertex:
            superstring += nextvertex[-1]
            nextvertex = self._directed_edges[nextvertex]
        
        return superstring


def main():
    kmers = {'ATTAC', 'TACAG', 'GATTA', 'ACAGA', 'CAGAT', 'TTACA', 'AGATT'}
    dbgraph = DeBruijn(kmers)
    print(dbgraph.get_cyclic_superstring())

if __name__ == '__main__':
    main()
