from kivy.app import App
from kivymd.app import MDApp
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from kivymd.theming import ThemeManager
from kivymd.uix.button import MDFlatButton
from kivy_garden.graph import Graph, MeshLinePlot
import numpy as np


def plot_cosine(self, *args):
    x = np.linspace(0, 10, 550)
    y = np.cos(x)

    plot = MeshLinePlot(color=[0, 0, 1, 1])
    plot.points = [(i, j) for i, j in zip(x, y)]
    self.graph.add_plot(plot)


def plot_sine(self, *args):
    x = np.linspace(0, 10, 550)
    y = np.sin(x)

    plot = MeshLinePlot(color=[0, 0, 1, 1])
    plot.points = [(i, j) for i, j in zip(x, y)]
    self.graph.add_plot(plot)



