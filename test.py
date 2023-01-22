from kivy.app import App
from kivy.uix.label import Label
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
                           x_grid=True, y_grid=True, xmin=-0, xmax=10, ymin=-1, ymax=1,
                           size_hint=(.8, .8), pos_hint={'center_x': .5, 'center_y': .5},
                           font_size='14sp',
                           background_color=[0, 0, 0, 1])
        self.add_widget(self.graph)

        button_layout = BoxLayout(orientation='horizontal', size_hint=(1, 0.1), pos_hint={'center_x': 0.5, 'y': 0.03})
        self.sin_button = MDFlatButton(text='sin', on_press=self.plot_sine)
        button_layout.add_widget(self.sin_button)
        self.cos_button = MDFlatButton(text='cos', on_press=self.plot_cosine)
        button_layout.add_widget(self.cos_button)
        self.add_widget(button_layout)

        for i in range(1,4):
            label = Label(text=str(i), pos_hint={'x':0,'top':1-i/4}, font_size='12sp')
            self.add_widget(label)

    def plot_sine(self, *args):
        x = np.linspace(0, 10, 550)
        y = np.sin(x)

        plot = MeshLinePlot(color=[0, 0, 1, 1])
        plot.points = [(i, j) for i, j in zip(x, y)]
        self.graph.add_plot(plot)

    def plot_cosine(self, *args):
        x = np.linspace(0, 10, 550)
        y = np.cos(x)

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
