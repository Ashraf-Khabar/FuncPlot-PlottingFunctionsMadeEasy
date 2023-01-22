from kivy.app import App
from kivymd.app import MDApp
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from kivymd.theming import ThemeManager
from kivymd.uix.button import MDFlatButton
from kivy_garden.graph import Graph, MeshLinePlot
import numpy as np


class PlotWidget(Screen):
    def __init__(self, **kwargs):
        super(PlotWidget, self).__init__(**kwargs)
        self.graph = Graph(xlabel='X', ylabel='Y', x_ticks_minor=5,
                           x_ticks_major=25, y_ticks_major=1,
                           y_grid_label=True, x_grid_label=True, padding=5,
                           x_grid=True, y_grid=True, xmin=-0, xmax=10, ymin=-1, ymax=1)

        self.sin_button = MDFlatButton(text='sin', pos_hint={"center_x": 0.5, "center_y": .03}, on_press=self.plot_sine)
        self.cos_button = MDFlatButton(text='cos', pos_hint={"center_x": 0.7, "center_y": .03},
                                       on_press=self.plot_cosine)
        self.sqrt_button = MDFlatButton(text='sqrt', pos_hint={"center_x": 0.3, "center_y": .03},
                                        on_press=self.plot_sqrt)
        self.exp_button = MDFlatButton(text='exp', pos_hint={"center_x": 0.9, "center_y": .03},
                                        on_press=self.plot_sqrt)
        self.add_widget(self.graph)
        self.add_widget(self.sin_button)
        self.add_widget(self.cos_button)
        self.add_widget(self.sqrt_button)
        self.add_widget(self.exp_button)

    def plot_cosine(self, *args):
        x = np.linspace(0, 2 * np.pi, 500)
        y = np.cos(x)

        plot = MeshLinePlot(color=[0, 1, 0, 1])
        plot.points = [(i, j) for i, j in zip(x, y)]
        self.graph.add_plot(plot)

    def plot_sqrt(self, *args):
        x = np.linspace(0, 10, 500)
        y = np.sqrt(x)

        plot = MeshLinePlot(color=[0, 0, 1, 1])
        plot.points = [(i, j) for i, j in zip(x, y)]
        self.graph.add_plot(plot)

    def plot_sine(self, *args):
        x = np.linspace(0, 10, 550)
        y = np.sin(x)

        plot = MeshLinePlot(color=[0, 0, 1, 1])
        plot.points = [(i, j) for i, j in zip(x, y)]
        self.graph.add_plot(plot)


class PlotApp(MDApp):
    theme_cls = ThemeManager()

    def build(self):
        layout = BoxLayout()
        layout.add_widget(PlotWidget())
        return layout


if __name__ == '__main__':
    app = PlotApp()
    app.run()