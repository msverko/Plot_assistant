from typing import List
import tkinter as tk
from tkinter import *
from tkinter import ttk
import csv
from typing import List
from configparser import ConfigParser


class CSVHandler:
    @staticmethod
    def read_tags_from_csv(filename: str) -> List[str]:
        with open(filename, "r") as csv_file:
            csv_reader = csv.reader(csv_file)
            next(csv_reader) # Skip the first row
            tags = [row[0] for row in csv_reader]
        return tags

    @staticmethod
    def write_selected_tags_to_csv(filename: str, tags: List[str]) -> None:
        with open(filename, "w", newline="") as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(tags)

class INIHandler:
    @staticmethod
    def write_chart_config_to_ini(filename: str, section_name: str, geometry: str, title: str, x_label: str, y_label: str) -> None:
        config = ConfigParser()
        config[section_name] = {"Geometry": geometry, "title": title, "x_label": x_label, "y_label": y_label}
        with open(filename, "w") as config_file:
            config.write(config_file)

class FileManager:
    @staticmethod
    def write_to_files(selected_tags: List[str], section_name: str, chart_geometry: str, title: str, x_label: str, y_label: str) -> None:
        CSVHandler.write_selected_tags_to_csv("OutputTagList.csv", selected_tags)
        INIHandler.write_chart_config_to_ini("ChartConfig.ini", section_name, chart_geometry, title, x_label, y_label)


class ChartSetup:
    def __init__(self, window: tk.Tk) -> None:
        # Read tags from CSV file
        self.csvHandler = CSVHandler()
        self.tags = self.csvHandler.read_tags_from_csv("InputTagList.csv")

        # Main window
        self.window  = tk.Tk()
        self.window.geometry("400x350")
        self.window.title("Chart Setup")

        # Label for the list box
        self.label = Label(self.window, text="Tag selection")
        self.label.grid(row=0, column=2, pady=0)

        # Select tags
        self.listbox_tags = Listbox(self.window, selectmode=MULTIPLE, width=30)
        for tag in self.tags:
            self.listbox_tags.insert(END, tag)
        self.listbox_tags.grid(row=1, column=2, rowspan=11, padx=10, pady=0, sticky='nsew')

        # Chart type selection combo box
        self.combo_type_label = Label(self.window, text="Select a chart type")
        self.combo_type_label.grid(row=0, column=1, pady=0)
        self.chart_geometrys = ["Scatter Chart", "Horizontal Bar Chart", "Vertical Bar Chart", "Stacked Bar Chart", "Grouped Bar Chart", "Line Chart", "Area Chart", "Histogram", "Boxplot", "Heatmap"]
        self.combo_type = ttk.Combobox(self.window, values=self.chart_geometrys)
        self.combo_type.grid(row=1, column=1, pady=0)

        # Chart layers selection combo box
        self.combo_layer_label = Label(self.window, text="Select a layer")
        self.combo_layer_label.grid(row=2, column=1, pady=0)
        self.numbers = [1, 2, 3]
        self.combo_layer = ttk.Combobox(self.window, values=self.numbers)
        self.combo_layer.grid(row=3, column=1, pady=0)

        # Chart Title
        self.chart_title_label = Label(self.window, text="Enter chart title:")
        self.chart_title_label.grid(row=4, column=1, pady=0)
        self.chart_title_field = Entry(self.window)
        self.chart_title_field.grid(row=5, column=1, pady=0) 

        # X-label
        self.x_label = Label(self.window, text="Enter x-label:")
        self.x_label.grid(row=6, column=1, pady=0) 
        self.x_field = Entry(self.window)
        self.x_field.grid(row=7, column=1, pady=0) 

        # Y-label
        self.y_label = Label(self.window, text="Enter y-label:")
        self.y_label.grid(row=8, column=1, pady=0) 
        self.y_field = Entry(self.window)
        self.y_field.grid(row=9, column=1, pady=0) 

        # button object
        self.button_save = Button(self.window, text="Write to files", command=self.button_callback)
        self.button_save.grid(row=10, column=1, pady=10)

    def button_callback(self) -> None:
        selected_tags = [self.listbox_tags.get(idx) for idx in self.listbox_tags.curselection()]
        chart_geometry = self.combo_type.get()
        graph_layer = self.combo_layer.get()
        chart_title = self.chart_title_field.get()
        x_label = self.x_field.get()
        y_label = self.y_field.get()
        section_name = "GraphSetup" + str(graph_layer)
        self.fileManager = FileManager()
        self.fileManager.write_to_files(selected_tags, section_name, chart_geometry, chart_title, x_label, y_label)
        

    def start(self) -> None:
        # Start the main loop
        self.window.mainloop()

if __name__ == "__main__":
    chart_setup = ChartSetup("InputTagList.csv")
    chart_setup.start()