<h2>Plot assistant - Graph visualization framework for the industrial control systems</h2> <br />

**Graph visualization framework as a custom feature interfaced with industrial SCADA-based HMI**

This is a basic showcase poroject with the very limited functionality,
providing proof of concept for proposed graph visualization framework architecture implemented with Plotnine Python data visualization library 
based on the ggplot2 package from the R language.

The file **CurentData.csv** contains below three tags with coresponding values, provided by interfaced HMI from runtime database:
STAT_P1_WORK_HRS,STAT_P2_WORK_HRS,STAT_P3_WORK_HRS
51,102,84  

The file **ChartConfig.ini** contains basic parameters needed to plot the chart:
[GraphSetup1]
geometry = Vertical Bar Chart
title = Pums runtime hrs
x_label = Pums
y_label = hrs

Run **select_plot.py** to plot the chart form with geometry set in ChartConfig.ini (currently only Vertical Bar Chart),
and with data from CurentData.csv

The file **plot_assistant.py** contains UI (that can be activated) where tags can be selected and parameters set and saved to files, but runtime values cannot be provided without connection to HMI.

In order to be able to generate charts containing realtime data from the controlled industrial process,
the provided Plot assistant must interface the HMI.
For this example the undeline HMI was Siemens WinCC, where three push-button objects were added in
the graphics designer that performs tasks of activating the framework UI form, reading tag names previously selected from the list box and saved in csv file,
and storing corresponding tag values read from the runtime database, to make them available for the visualization framework.

Following functionality is implemented on the HMI side as a minimal integration requirenments:

**Select Chart button:**
Sub OnClick(ByVal Item)                    
Dim guiPth
guiPth = HMIRuntime.ActiveProject.Path & "\PlotAssistant\gui.lnk"
Dim objWshShell
Set objWshShell = CreateObject("Wscript.Shell")
objWshShell.Run guiPth, 1
End Sub

**Load values button:**
Sub OnClick(ByVal Item)                             
Dim TagListPth, CurrentData, objFSO, objFile, strLine, arrTags, i, arrTagValues()
TagListPth = HMIRuntime.ActiveProject.Path & "\PlotAssistant\OutputTagList.csv"
CurrentData = HMIRuntime.ActiveProject.Path & "\PlotAssistant\CurrentData.csv"
'Input file
Const ForReading = 1
Set objFSO = CreateObject("Scripting.FileSystemObject")
Set objFile = objFSO.OpenTextFile(TagListPth, ForReading)
strLine = objFile.ReadLine()
arrTags = Split(strLine, ",")
objFile.Close
'Get tag values
Redim arrTagValues(UBound(arrTags))
For i = 0 To UBound(arrTags)
	 arrTagValues(i)= GetTag(arrTags(i)) 
Next
'Output file
Set objFile = objFSO.CreateTextFile(CurrentData, True)
objFile.WriteLine Join(arrTags, ",")
objFile.WriteLine Join(arrTagValues, ",")
objFile.Close
End Sub

**Show chart button:**
Sub OnClick(ByVal Item)                              
Dim objWshShell, pth
pth = HMIRuntime.ActiveProject.Path & "\PlotAssistant\SelectPlot.lnk"
Set objWshShell = CreateObject("Wscript.Shell")
objWshShell.Run pth, 1
End Sub


