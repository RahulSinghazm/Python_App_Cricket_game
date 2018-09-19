from cricket_game import batscore,bowlscore

l1=[{'name':'Virat','role':'bat','runs':112,'4':10,'6':0,'balls':119,'field':0},
    {'name':'Dhoni','role':'bat','runs':120,'4':11,'6':2,'balls':112,'field':0}]

l2=[{'name':'Bhuvneshwar','role':'bowl','wkt':1,'over':10,'runs':71,'field':1},
    {'name':'Yuzvendra','role':'bowl','wkt':2,'over':10,'runs':45,'field':0},
    {'name':'Kuldeep','role':'bowl','wkt':3,'over':10,'runs':34,'field':0}]

for l in l1:
    print(batscore(l))

for l in l2:
    print(bowlscore(l))

