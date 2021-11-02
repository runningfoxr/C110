import plotly.figure_factory as ff
import statistics
import random
import pandas as pd
import csv

df=pd.read_csv("newdata.csv")
data=df["average"].tolist()

def randomsetofmeans(counter):
    dataset=[]
    for i in range(0,counter):
        randomindex=random.randint(0,len(data)-1)
        value=data[randomindex]
        dataset.append(value)
    mean=statistics.mean(dataset)
    return mean

def showfigure(meanlist):
    df=meanlist
    figure=ff.create_distplot([df],["average"],show_hist=False)
    figure.show()
    
def setup():
    meanlist=[]
    for i in range(0,1000):
        setofmeans=randomsetofmeans(100)
        meanlist.append(setofmeans)
    showfigure(meanlist)

setup()