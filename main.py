import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#determined by finding the average growth of Banner's weekly stock price over the last year
mu = 0.1630829 
sigma = 03.1821422

#creates dataframe to store simulations
sims_df = pd.DataFrame()

#generates 1000 simulations
for i in range(1000):
    #list with initial stock price (current trading price)
    vals = [54.87]
    for x in range(260): #loop runs 260 times to forecast 5 years into the future, on a weekly basis
        #appends new values to list of vals using normally distributed stochastic growth based on
        #historical growth data
        vals.append(vals[x-1]*(1 + 0.01*np.random.normal(mu, sigma)))
    #adds the simulation to the dataframe
    sims_df['Sim'+str(i+1)] = vals

#runs through the simulated values to see if, in the forecast, the target price is met or exceeded
count = 0
for i in range(1000):
    for k in range(260):
        if sims_df['Sim' + str(i+1)][k] >= 61.59:
            count += 1
            break

#print proportion of simulations in which target price is met or exceeded
print(count/1000)
