class Problem():
    def __init__(self):
        # self.graph = self.getGraph()
        self.graph = {
            'a' : [(1, 'b1'), (2, 'b2'), (3, 'b3')],
            'b1' : [(2, 'c1')],
            'b2' : [(2, 'c2')]
        }

    def getGraph(self):
        print("getGraph Called...")




p1 = Problem()