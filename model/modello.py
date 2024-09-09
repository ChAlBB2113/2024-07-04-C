from database.DAO import DAO
import networkx as nx

class Model:
    def __init__(self):
        self._nodi=[]
        self._archi=[]
        self._grafo=nx.DiGraph()

    def getDDyear(self):
        return DAO.getAnni()
    def getDDshape(self):
        return DAO.getForme()
    def creaGrafo(self, forma, anno):
        self._nodi.clear()
        self._archi.clear()
        self._grafo.clear()

        self._nodi= DAO.getNodi(forma, anno)
        self._archi= DAO.getDizArcoLongitudini(forma, anno)
        self._grafo.add_nodes_from(self._nodi)
        for chiave in self._archi:
            if self._archi[chiave][0]<self._archi[chiave][1]:
                self._grafo.add_edge(chiave[0], chiave[1], weight=self._archi[chiave][1]-self._archi[chiave][0])
            else:
                self._grafo.add_edge(chiave[1], chiave[0], weight=self._archi[chiave][0]-self._archi[chiave][1])






