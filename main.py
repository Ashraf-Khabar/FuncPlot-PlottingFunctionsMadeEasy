from kivy.app import App
from kivy.uix.label import Label
from kivymd.app import MDApp
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from kivymd.theming import ThemeManager
from kivymd.uix.button import MDFlatButton
from kivy_garden.graph import Graph, MeshLinePlot
import numpy as np
from MathFunctions import plot_sine, plot_exp, plot_sqrt, plot_cosine
from kivymd.uix.menu import MDDropdownMenu


class PlotWidget(Screen):
    def __init__(self, **kwargs):
        super(PlotWidget, self).__init__(**kwargs)

        self.graph = Graph(xlabel='X', ylabel='Y', x_ticks_minor=5,
                           x_ticks_major=25, y_ticks_major=1,
                           y_grid_label=True, x_grid_label=True, padding=5,
                           x_grid=True, y_grid=True, xmin=-1, xmax=15, ymin=-1, ymax=10,
                           size_hint=(.8, .8), pos_hint={'center_x': .5, 'center_y': .5},
                           font_size='14sp',
                           background_color=[0, 0, 0, 1])
        self.add_widget(self.graph)

        # Function button
        button_layout = BoxLayout(orientation='horizontal', size_hint=(1, 0.1), pos_hint={'center_x': 0.5, 'y': 0.03})
        self.sin_button = MDFlatButton(text='sin', on_press=self.plot_sine)
        button_layout.add_widget(self.sin_button)
        self.cos_button = MDFlatButton(text='cos', on_press=self.plot_cosine)
        button_layout.add_widget(self.cos_button)
        self.exp_button = MDFlatButton(text='exp', on_press=self.plot_exp)
        button_layout.add_widget(self.exp_button)
        self.sqrt_button = MDFlatButton(text='sqrt', on_press=self.plot_sqrt)
        button_layout.add_widget(self.sqrt_button)

        self.add_widget(button_layout)

        # the clear button
        self.clear_button = MDFlatButton(text='undo', on_press=self.clear_plots)
        button_layout.add_widget(self.clear_button)
        for i in range(1,4):
            label = Label(text=str(i), pos_hint={'x':0,'top':1-i/4}, font_size='12sp')
            self.add_widget(label)

    def plot_sine(self, *args):
        plot_sine(self)

    def plot_cosine(self, *args):
        plot_cosine(self)

    def plot_exp(self, *args):
        plot_exp(self)

    def plot_sqrt(self, *args):
        plot_sqrt(self)

    def clear_plots(self, *args):
        for plot in self.graph.plots:
            self.graph.remove_plot(plot)


class PlotApp(MDApp):
    theme_cls = ThemeManager()

    def build(self):
        layout = BoxLayout()
        layout.add_widget(PlotWidget())
        return layout


if __name__ == '__main__':
    app = PlotApp()
    app.run()
