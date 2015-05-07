import pandas as pd
import numpy as np
import prettyplotlib as ppl
import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib
matplotlib.style.use('ggplot')
from prettyplotlib import brewer2mpl
import matplotlib.cm as cm

import datetime
import pandas.io.data


df = pd.read_csv('NYPD_Motor_Vehicle_Collisions.csv', sep=',')
df_borough = df.ix[:,['BOROUGH',
                      'NUMBER OF PERSONS INJURED',
                      'NUMBER OF PERSONS KILLED',
                      'NUMBER OF PEDESTRIANS INJURED',
                      'NUMBER OF PEDESTRIANS KILLED',
                      'NUMBER OF CYCLIST INJURED',
                      'NUMBER OF CYCLIST KILLED',
                      'NUMBER OF MOTORIST INJURED',
                      'NUMBER OF MOTORIST KILLED']]

#get rid of n/a values and aggregated by Borough
df_borough = df_borough[pd.notnull(df['BOROUGH'])]
by_borough = df_borough.groupby('BOROUGH').sum()


#setting up outside of the plot
N = 5
ind = np.arange(N)
width = 0.1
error_config = {'ecolor': '0.3'}

#pull columns
total_injured = by_borough.ix[:,0]
total_killed = by_borough.ix[:,1]
pedestrians_injured = by_borough.ix[:,2]
pedestrians_killed = by_borough.ix[:,3]
cyclist_injured = by_borough.ix[:,4]
cyclist_killed = by_borough.ix[:,5]
motorist_injured = by_borough.ix[:,6]
motorist_killed = by_borough.ix[:,7]

#read in colors
#colors = iter(cm.rainbow(np.linspace(0,1)))
#for y in (0,1,2,3):

#add bars onto plot
p1 = plt.bar(ind, total_injured, width, color='c', error_kw=error_config)
p2 = plt.bar(ind + width, pedestrians_injured, width, color='m', error_kw=error_config)
p3 = plt.bar(ind + (width*2), cyclist_injured, width, color='g', error_kw=error_config)
p4 = plt.bar(ind + (width*3), motorist_injured, width, color='b', error_kw=error_config)

#chart labels
plt.title('NYPD Crash Data by number of Injuries')
plt.xticks(ind+width/2, ('BRONX', 'BROOKLYN', 'MANHATTAN', 'QUEENS', 'STATEN ISLAND'))
plt.ylabel('Number')
plt.legend( (p1[0], p2[0], p3[0], p4[0]), ('Total injured', 'Pedestrians injured', 'Cyclist injured', 'Motorist injured'), prop={'size':11} )

#print the figure to the screen
plt.show()


#add bars onto plot
p1 = plt.bar(ind, total_killed, width, color='c', error_kw=error_config)
p2 = plt.bar(ind + width, pedestrians_killed, width, color='m', error_kw=error_config)
p3 = plt.bar(ind + (width*2), cyclist_killed, width, color='g', error_kw=error_config)
p4 = plt.bar(ind + (width*3), motorist_killed, width, color='b', error_kw=error_config)

#chart labels
plt.title('NYPD Crash Data by Number of People Killed')
plt.xticks(ind+width/2, ('BRONX', 'BROOKLYN', 'MANHATTAN', 'QUEENS', 'STATEN ISLAND'))
plt.ylabel('Number')
plt.legend( (p1[0], p2[0], p3[0], p4[0]), ('Total killed', 'Pedestrians killed', 'Cyclist killed', 'Motorist killed'), prop={'size':11})

#print the figure to the screen
plt.show()
