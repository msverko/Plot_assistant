Plot assistant
Graph visualization framework as a custom feature interfaced with industrial SCADA-based HMI

This is basic showcase poroject with the very limited functionality,
providing proof of concetp for proposed graph visualization framework architecture implemented with Plotnine Python Python data visualization library 
based on the ggplot2 package from the R language.

The file CurentData.csv contains below three tags with corespondent values, provided by interfaced HMI from runtime database:
STAT_P1_WORK_HRS,STAT_P2_WORK_HRS,STAT_P3_WORK_HRS
51,102,84  

The file ChartConfig.ini contains basic parameters needed to plot cahard:
[GraphSetup1]
geometry = Vertical Bar Chart
title = Pums runtime hrs
x_label = Pums
y_label = hrs

Run select_plot.py to plot the chart form with geometry seet in ChartConfig.ini (currently only Vertical Bar Chart),
and with data from CurentData.csv

In order to be able to generate cagarts containg realtime data from the controlled industrial process,
the proveded Plot assistant must interface the HMI.
For this example the undeline HMI was Siemens WinCC, where three push-button objects (marked with a red frame) are added in
the graphics designer that performs tasks of activating the framework UI form,
reading tag names previously selected from the list box and saved in csv file,
and storing corresponding tag values read from the runtime database, to make
them available for the visualization framework.
