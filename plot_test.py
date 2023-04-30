from plotnine import *
from statistics import *
import pandas as pd

'''
# create two arrays of random data
x = [1, 2, 3, 4, 5]
y = [10, 20, 30, 40, 50]

# create a dataframe from the arrays
df = pd.DataFrame({'x': x, 'y': y})

# create a scatter plot using plotnine
plot = ggplot(df, aes(x='x', y='y')) + \
       geom_point() + \
       geom_smooth(method='lm', se=False)

# show the plot
print(plot)
'''

# From tutorial  - and added an extra line (must declare separate group) to test if layers of graphic are supported:
# https://coderzcolumn.com/tutorials/data-science/plotnine-simple-guide-to-create-charts-using-grammar-of-graphics
'''
from plotnine.data import mpg
chart = ggplot(data=mpg, mapping=aes(x="manufacturer", fill="factor(cyl)"))
bars = geom_bar()
line = geom_line(mapping=aes(x="manufacturer", y="cty", group=1), stat="summary", fun_y=mean, size=1.7, color="green")
labels = labs(x="Manufacturer", y="Model Counts", title="Model Counts per Manufacturer colored by Cylinder")
theme_grammer = theme(figure_size=(11,5))

plot = chart + bars + line + labels + texts + theme_grammer

print(plot)
'''

# Example of chart with two layers of graphic (bar and line)
x = ["A", "B", "C", "D"]
y1 = [10, 15, 20, 25]
y2 = [5, 10, 15, 20]

# Combine data into a data frame
data = {"x": x, "y1": y1, "y2": y2}
df = pd.DataFrame(data)

# Create the bar chart
chart = ggplot(df, aes(x="x", y="y1")) + geom_bar(stat="identity", fill="#4C72B0")

# Add lines for each array
chart += geom_line(df, aes(x="x", y="y2", group=1), color="#C44E52", size=1.5)

# Add labels to the lines
chart += geom_text(df, aes(x="x", y="y2", label="y2"), color="#C44E52", size=10, nudge_y=1)

# Add a static title for the line
chart += annotate("text", x="C", y=15, label="Line Title", color="#C44E52", size=12, ha="center")

# Add axis labels and title
chart += labs(x="X Axis Label", y="Y Axis Label", title="Bar chart with lines, labels, and title")

# Set the figure size
chart += theme(figure_size=(8, 6))

# Display the chart
print(chart)

