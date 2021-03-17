from matplotlib import pyplot as plt
from matplotlib.dates import date2num, DateFormatter
import pandas as pd
import datetime as dt


# load data
file_loc = r'UEG_LGN2_RAWDATA.xlsx'

df = pd.read_excel(file_loc, usecols=[0,1,2,3,4,5,6,7,8,9,10])

row_skip = 6

raw_date = df.iloc[row_skip:, 0]
raw_time = df.iloc[row_skip:, 1]
datetime = []

# print (raw_date, raw_time)

for m, n in zip(raw_date, raw_time):
    value = dt.datetime.combine(m.date(), n)
    datetime.append(date2num(value))

#loading data into lists
Shroud1 = df.iloc[row_skip:, 2]
Shroud2 = df.iloc[row_skip:, 3]
channel_11 = df.iloc[row_skip:, row_skip]
channel_12 = df.iloc[row_skip:, 5]
channel_13 = df.iloc[row_skip:, 6]
channel_26 = df.iloc[row_skip:, 7]
channel_27 = df.iloc[row_skip:, 8]
channel_28 = df.iloc[row_skip:, 9]
channel_29 = df.iloc[row_skip:, 10]

#plotting 
fig = plt.figure()
ax1 = fig.add_subplot(111)

ax1.plot(datetime, Shroud1, label='Shroud')
ax1.plot(datetime, Shroud2, label='Shroud2')
ax1.plot(datetime, channel_11, label='ch11')
ax1.plot(datetime, channel_12, label='ch12')
ax1.plot(datetime, channel_13, label='ch13')

#limits
ax1.plot(datetime, channel_26, label='LIMIT', color='red')
ax1.plot(datetime, channel_27, label='LIMIT', color='red')
ax1.plot(datetime, channel_28, label='LIMIT', color='red')
ax1.plot(datetime, channel_29, label='LIMIT', color='red')

#ticks formatting for datetime
ticksSkip = len(datetime)//30
ticksUsed = datetime[::ticksSkip]
tickLabel = [ i for i in ticksUsed]
ax1.set_xticks(ticksUsed)
ax1.set_xticklabels(tickLabel)


fig.autofmt_xdate()
ax1.xaxis.set_major_formatter(DateFormatter('%m/%d %H:%M'))
ax1.grid()
ax1.legend()

plt.show()
