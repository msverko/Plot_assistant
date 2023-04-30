import configparser
import subprocess


class ChartConfig:
    def __init__(self, file_name):
        self.config = configparser.ConfigParser()
        self.config.read(file_name)
        
    def get_graph_setup(self, setup_name):
        return self.config[setup_name]

class ChartPlot:
    def __init__(self, config_file_name, graph_setup_layer):
        self.config = ChartConfig(config_file_name)
        self.graph_setup = self.config.get_graph_setup(graph_setup_layer)
        
    def plot(self):
        plot_geom = self.graph_setup['geometry']
        if plot_geom == 'Vertical Bar Chart':
            subprocess.run(['python', 'plot_bargraph_vertical.py'])

# Create chart instance and plot it
chart = ChartPlot('ChartConfig.ini', 'GraphSetup1')
chart.plot()