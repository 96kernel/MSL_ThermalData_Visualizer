import matplotlib
import argparse 
# matplotlib.use('Qt5Agg')
from matplotlib import pyplot as plt
from matplotlib.dates import date2num, DateFormatter
import pandas as pd
import datetime as dt
import time


st = time.time()
parser = argparse.ArgumentParser()

parser.add_argument('-i', '--infile', type=str)
args = parser.parse_args()

if not args.infile:
    file_loc = r'UEG_LGN2.txt'

else:
    file_loc = args.infile

df = pd.read_csv(file_loc, header = 3, usecols=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17], skiprows = [6], encoding = 'iso8859-1')

row_skip = 0

raw_date = df.iloc[row_skip:, 0]
raw_time = df.iloc[row_skip:, 1]
date_time = []

# print (raw_date, raw_time)

for m, n in zip(raw_date, raw_time):
    value = dt.datetime.strptime(m + n, '%d/%m/%Y%H:%M:%S')
    date_time.append(date2num(value))

listName = list(df.columns)
print(listName)
#loading data into lists
data_col1 = df.iloc[row_skip:, 2]
data_col2 = df.iloc[row_skip:, 3]
data_col3 = df.iloc[row_skip:, 4]
data_col4 = df.iloc[row_skip:, 5]
data_col5 = df.iloc[row_skip:, 6]
data_col6 = df.iloc[row_skip:, 7]
data_col7 = df.iloc[row_skip:, 8]
data_col8 = df.iloc[row_skip:, 9]
data_col9 = df.iloc[row_skip:, 10]
data_col10 = df.iloc[row_skip:, 11]
data_col11 = df.iloc[row_skip:, 12]
data_col12 = df.iloc[row_skip:, 13]
data_col13 = df.iloc[row_skip:, 14]
data_col14 = df.iloc[row_skip:, 15]
data_col15 = df.iloc[row_skip:, 16]
data_col16 = df.iloc[row_skip:, 17]

print('data read time (s):', time.time()-st)

#setting size of plot
plt.rcParams["figure.figsize"] = (12,8) 

#plotting 
fig = plt.figure()
ax1 = fig.add_subplot(111)

ax1.plot(date_time, data_col1, label='TRP UEG front')
ax1.plot(date_time, data_col2, label='CP back')
ax1.plot(date_time, data_col3, label='UEG top')
ax1.plot(date_time, data_col4, label='CP front')
ax1.plot(date_time, data_col5, label='UEG back')
ax1.plot(date_time, data_col6, label='TRP red')
ax1.plot(date_time, data_col7, label='UEG left')
ax1.plot(date_time, data_col8, label='UEG bottom right')
ax1.plot(date_time, data_col9, label='UEG middle right')
ax1.plot(date_time, data_col10, label='UEG top right')

# ax1.plot(date_time, data_col11, label='TCR (TRP)')
# ax1.plot(date_time, data_col10, label='Pressure (mbar)')

#limits
ax1.plot(date_time, data_col12, color='red')
ax1.plot(date_time, data_col13, color='red')
ax1.plot(date_time, data_col14, color='red')
ax1.plot(date_time, data_col15, color='red')

#ticks formatting for datetime
ticksSkip = len(date_time)//20   
ticksUsed = date_time[::ticksSkip]
tickLabel = [ i for i in ticksUsed]
ax1.set_xticks(ticksUsed)
ax1.set_xticklabels(tickLabel)


print('tick format time (s):', time.time()-st)

fig.autofmt_xdate()
ax1.xaxis.set_major_formatter(DateFormatter('%m/%d %H:%M'))
ax1.set_title('UEG (LgN2) \n Mechanical System Laboratory')
ax1.set_xlabel('date/time')
ax1.set_ylabel('Temperature Change Rate (°C/min)')
# ax1.set_ylim([-40, 90])
ax1.grid()
ax1.legend()

print('plot format time (s):', time.time()-st)

plt.show()
