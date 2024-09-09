from operator import itemgetter

import flet as ft
from UI.view import View
from model.modello import Model


class Controller:
    def __init__(self, view: View, model: Model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def fillDD(self):
        self._view.ddyear.options.clear()
        self._view.ddshape.options.clear()
        anni=self._model.getDDyear()
        forme= self._model.getDDshape()
        for anno in anni:
            self._view.ddyear.options.append(ft.dropdown.Option(f"{anno}"))
        for forma in forme:
            self._view.ddshape.options.append(ft.dropdown.Option(f"{forma}"))
        self._view.update_page() #!!!!!!!!!



    def handle_graph(self, e):
        anno=self._view.ddyear.value
        forma=self._view.ddshape.value
        if anno=="" or anno==None or anno=="Anno":#== per i confronti non solo =!!!!!!!!!!!!!!!!!!
            self._view.txt_result1.clear()
            self._view.txt_result1.controls.append(ft.Text(f"Selezionare un anno"))
            self._view.update_page()
            return
        if forma=="" or forma==None or forma=="Anno":#== per i confronti non solo =!!!!!!!!!!!!!!!!!!
            self._view.txt_result1.clear()
            self._view.txt_result1.controls.append(ft.Text(f"Selezionare una forma"))
            self._view.update_page()
            return

        self._model.creaGrafo(forma,anno)

        self._view.txt_result1.controls.append(ft.Text(f"Numero nodi: {len(self._model._grafo.nodes())}"))
        self._view.txt_result1.controls.append(ft.Text(f"Numero archi: {len(self._model._grafo.edges())}"))
        listaTuple=[]
        for arco in self._model._grafo.edges(): #dove arco è tupla (nodo1, nodo2)
            listaTuple.append((arco[0], arco[1], self._model._grafo[arco[0]][arco[1]]['weight']))
        listaTuple.sort(key=itemgetter(2), reverse=True) #per ordine decrescente
        for tupla in listaTuple:
            self._view.txt_result1.controls.append(ft.Text(f"{tupla[0]} -> {tupla[1]} | weight = {tupla[2]}"))

        self._view.update_page()



    def handle_path(self, e):
        pass
