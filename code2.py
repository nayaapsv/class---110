from re import X
import pandas as pd
import csv
import plotly_express as px
import statistics
import random
import plotly.figure_factory as ff
import plotly.graph_objects as go

df = pd.read_csv('data.csv')
data = df['claps'].to_list()

mean = statistics.mean(data)
std = statistics.stdev(data)

print(mean)
print(std)

def setup():
    meanlist = []
    for i in range(0,1000):
        mean = randomNumbers(100)
        meanlist.append(mean)

    showFig(meanlist)
    mean_sample = statistics.mean(meanlist)
    print(mean_sample)

def randomNumbers(counter):
    dataSet = []

    for i in range (0,counter):
        index = random.randint(0,len(data)-1)   
        value = data[index]
        dataSet.append(value)
        
    mean = statistics.mean(dataSet)
    return mean

def showFig(meanlist):
    df = meanlist
    mean = statistics.mean(df)
    fig = ff.create_distplot([df],['Data'],show_hist=False)    
    fig.add_trace(go.Scatter(x=[mean,mean],y=[0,1],mode = 'lines'))
    fig.show()
        
setup()