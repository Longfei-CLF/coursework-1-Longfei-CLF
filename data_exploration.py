# Start to use pandas
import numpy as np
from numpy.lib.function_base import append
import pandas as pd
import matplotlib.pyplot as plt

def xaxis_generation():
    """
    Generate the common used xaxis for the following three diagrams
    return: A list of year from 1700 to 2021
    rtype: List
    """
    xaxis = []
    for i in range (1700, 2021):
        xaxis.append(i)
    return xaxis

def Number_Eruptions(df, xaxis):
    """
    Show the trend of number of eruptions verus time
    param: df Dataframe the prepared data, xaxis used for plotting
    return: Line plot of number of eruptions over time
    rtype: Graph
    """
    NumErup = []
    for i in xaxis:
        count = 0
        for x in df['Start Year']:
            if i == x:
                count = count + 1
        NumErup.append(count)

    plt.cla()
    plt.plot(xaxis, NumErup)
    plt.xlabel("Eruption Start Year")
    plt.ylabel("Number of Eruptions")
    plt.title("The relationship between Year and Number of Eruptions")
    plt.savefig('images/Number of Eruptions over Year.png')
    
def Eruption_Duration(df, xaxis):
    """
    Show the trend of eruptions duration verus time
    param: df Dataframe the prepared data, xaxis used for plotting
    return: Line plot of eruptions duration over time
    rtype: Graph
    """
    ErupDur_with_Outliner = []
    ErupDur_without_Outliner = []
    for i in xaxis:
        dur_with_Outliner = []
        dur_without_Outliner = []
        row = 0
        for x in df['Start Year']:
            if i == x:
                day = df.loc[row,'Eruption Duration (d)']
                if day < 10000:
                    dur_with_Outliner.append(day)
                    dur_without_Outliner.append(day)
                else:
                    dur_with_Outliner.append(day)
            row = row + 1
        if sum(dur_with_Outliner) == 0: ErupDur_with_Outliner.append(0)
        else: ErupDur_with_Outliner.append(np.mean(dur_with_Outliner))
        if sum(dur_without_Outliner) == 0: ErupDur_without_Outliner.append(0)
        else: ErupDur_without_Outliner.append(np.mean(dur_without_Outliner))        

    plt.cla()
    plt.plot(xaxis, ErupDur_with_Outliner)
    plt.xlabel("Eruption Start Year")
    plt.ylabel("Eruption Durations (d)")
    plt.title("The relationship between Year and Eruption Durations (with outliners)")
    plt.savefig('images/Eruptions Durations over Year with outliners.png')

    plt.cla()
    plt.plot(xaxis, ErupDur_without_Outliner)
    plt.xlabel("Eruption Start Year")
    plt.ylabel("Eruption Durations (d)")
    plt.title("The relationship between Year and Eruption Durations (without outliners)")
    plt.savefig('images/Eruptions Durations over Year without outliners.png')

def VEI(df, xaxis):
    """
    Show the trend of volcano eruption index (VEI) verus time
    param: df Dataframe the prepared data, xaxis used for plotting
    return: Line plot of VEI over time
    rtype: Graph
    """
    VEI = []
    for i in xaxis:
        index = []
        row = 0

        for x in df['Start Year']:
            if i == x:
                index.append(df.loc[row,'Volcano Eruption Index (VEI)'])
            row = row + 1
        if sum(index) == 0: VEI.append(0)
        else: VEI.append(np.mean(index))

    plt.cla()
    plt.plot(xaxis, VEI)
    plt.xlabel("Eruption Start Year")
    plt.ylabel("Volcano Eruption Index (VEI)")
    plt.title("The relationship between Year and VEI")
    plt.savefig('images/VEI over Year.png')

if __name__ == '__main__':
    cleaned_file = "Cleaned_GVP_Eruption_Results.xlsx"
    df = pd.read_excel(cleaned_file)
    df.rename(columns={'Sta_yr':'Start Year', 'Erup_dur': 'Eruption Duration (d)',
        'VEI': 'Volcano Eruption Index (VEI)'}, inplace=True)
    #Basic stat
    print(df.describe())
    # Outliners
    df.plot.box(subplots=True)
    plt.show()
    print(df.loc[df['Eruption Duration (d)'] > 10000]) # No need to drop, reasonable outliners
    # Plot graph to anwer the three questions
    Year = xaxis_generation()
    Number_Eruptions(df, Year)
    Eruption_Duration(df, Year)
    VEI(df, Year)
