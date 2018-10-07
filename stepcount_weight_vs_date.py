# -*- coding: utf-8 -*-
"""
Reads dates, step counts, and weight from a CSV file named stepcounts.csv 
(file contains header row which is discarded) & plots data for viz purposes.

Column 1: Dates (YYYY/MM/DD)
Column 2: Daily Step Count
Column 3: Weight (contains null values)
Column 4: Weight (no null values)

Lower bound for weight is 100, upper bound is max(weight)+5, lower bound for
step count is min(steps)-1000, upper bound for steps is max(steps).
"""

import matplotlib.pyplot as plt
import numpy as np
import matplotlib.dates as mdates
import csv
from datetime import datetime
from scipy.interpolate import spline

dates = []
steps = []
weight = []

with open('stepcounts.csv','r') as csvfile:
    readcsv = csv.reader(csvfile, delimiter=',')
    next(readcsv, None)
    for row in readcsv:
        dates.append(datetime.strptime(row[0], '%Y/%m/%d'))
        steps.append(float(row[1]))
        weight.append(float(row[3]))

newdates = mdates.date2num(dates)   # for use w/np.linspace()
xlist = np.linspace(newdates.min(),newdates.max(),num=830)  
xsmooth = np.linspace(newdates.min(),newdates.max(),num=75)
ysmooth = spline(xlist, steps, xsmooth)

fig = plt.figure()

ax1 = fig.add_subplot(2,1,1)    # weight
ax1.plot(dates, weight, 'o', color='#84a90e')
ax1.set_xlim([newdates.min(),newdates.max()])
ax1.set_ylim([100, (max(weight)+5)])
ax1.set_ylabel('Weight (pounds)')
ax1.set_xticks([])

ax2 = fig.add_subplot(2,1,2)    # steps
ax2.plot(dates, steps, color='#0086bf', linewidth=0.7)
ax2.plot(xsmooth, ysmooth, color='#c41e1e', linewidth=2)
ax2.set_xlim([newdates.min(),newdates.max()])
ax2.set_ylim([min(steps)-1000, max(steps)])
ax2.set_ylabel('Steps (# daily)')
ax2.set_xticklabels(ax2.xaxis.get_ticklabels(), rotation=90)
ax2.xaxis.set_major_locator(mdates.MonthLocator(interval=1))
ax2.xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))

fig.tight_layout()
fig.show()