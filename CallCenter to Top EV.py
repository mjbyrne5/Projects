# Designed for use as a virtual call center to mimic real world use

import random
import pandas as pd
import numpy as np

df = pd.read_csv("/Users/michaelbyrne/Desktop/Career/ProjectTestData.csv")

N11 = ['Null Grade Day 1 Attempt 1']
B12 = ['B Through High Fico Leads Day 1 Attempt 1']
C11 = ['C Leads Day 1 Attempt 1']
SH = ['Super Hot Lead']
N22 = ['Null Grade Day 2 Attempt 2']
B51 = ['B Through High Fico Leads Day 5 Attempt 1']
SHT = ['Super Hot Third Party Leads']
B11 = ['B Through High Fico Leads Day 1 Attempt 1']
SH2 = ['Super Hot Second Pass']
B21 = ['B Through High Fico Leads Day 2 Attempt 1']
B22 = ['B Through High Fico Leads Day 2 Attempt 2']
C21 = ['C Leads Day 2 Attempt 1']
C22 = ['C Leads Day 2 Attempt 2']
N21 = ['Null Grade Day 2 Attempt 1']
C12 = ['C Leads Day 1 Attempt 2']
N12 = ['Null Grade Day 1 Attempt 2']
zeros = ['0']

calls = N11*120 + B12*119 + C11*79 + SH*1297 + N22*15 + B51*15 + SHT*47 + B11*309 + SH2*373 + B21*143 + B22*64 + C21*41\
        + C22*9 + N21*70 + C12*20 + N12*60 + zeros*26019


# Real World Data
agents = df['FIRSTEMPLOYEENAME'].tolist()
StrategyName = df['STRATEGYNAME'].tolist()
value = df['EVOFCALL'].tolist()
callsTotal = df['CALLSTOTAL'].tolist()

# Simulation Data
busy = np.zeros(len(agents))  # tracks available agents relative to avg sale time
saleTime = df['AVGSALETIME'].tolist()

total = 0

while len(calls) > 0:
    currentEV = 0
    currentAgent = 'null'
    currentCall = random.choice(calls)
    calls.remove(currentCall)
    if currentCall != '0':
        for i in range(0, len(agents)):
            if currentCall == StrategyName[i] and busy[i] == 0 and callsTotal[i] > 99:
                if value[i] != 'Null':
                    if float(value[i]) > float(currentEV):
                        currentAgent = agents[i]
                        currentEV = float(value[i])
        print(currentCall)
        print(currentAgent)
        print(currentEV)
        for i in range(0, len(busy)):
            if agents[i] == currentAgent:
                busy[i] = round(saleTime[i]) + 16
        total += currentEV

    for i in range(0, len(busy)):
        if busy[i] > 0:
            busy[i] -= 1

print(total)
