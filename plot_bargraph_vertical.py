from plotnine import *
import pandas as pd
import configparser

# Read data from CSV file
df = pd.read_csv('CurrentData.csv')
df_long = pd.melt(df, var_name='Variable', value_name='Value')

# Read configuration from INI file
config = configparser.ConfigParser()
config.read('ChartConfig.ini')

# Read chart title, X-axis label, and Y-axis label from [GraphSetup1] section
chart_title = config.get('GraphSetup1', 'title')
x_label = config.get('GraphSetup1', 'x_label')
y_label = config.get('GraphSetup1', 'y_label')


chart = ggplot(df_long, aes(x='Variable', y='Value', fill='Variable'))
bars = geom_col()
labels = labs(title=chart_title, x=x_label, y=y_label, fill='Variable')
legend = theme(legend_position=[0.9,0.8], legend_direction='vertical')
size = theme(figure_size=(11,5.5))
bars_text = geom_text(mapping=aes(label='Value'), format_string='{:.2f}', va='bottom')

plot = chart + bars + labels + legend + size + bars_text

print(plot)


