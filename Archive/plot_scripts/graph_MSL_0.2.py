import matplotlib
# matplotlib.use('Qt5Agg')
from matplotlib import pyplot as plt
from matplotlib.dates import date2num, DateFormatter
import pandas as pd
import datetime as dt


# load data
file_loc = r'C:\Users\Ayush Jain\Documents\MSL\1255 - Assemblie 2 (MARSIM-2)\Data\1255-GLUEDASSEMBLIES-P3.xlsx'

df = pd.read_excel(file_loc, usecols=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17])

row_skip = 6

raw_date = df.iloc[row_skip:, 0]
raw_time = df.iloc[row_skip:, 1]
datetime = []

# print (raw_date, raw_time)

for m, n in zip(raw_date, raw_time):
    value = dt.datetime.combine(m.date(), n)
    datetime.append(date2num(value))

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

#plotting 
fig = plt.figure()
ax1 = fig.add_subplot(111)

ax1.plot(datetime, data_col1, label='SA1')
ax1.plot(datetime, data_col2, label='SA2')
ax1.plot(datetime, data_col3, label='SA5')
ax1.plot(datetime, data_col4, label='SB1')
ax1.plot(datetime, data_col5, label='SB3')
ax1.plot(datetime, data_col6, label='SB5')
ax1.plot(datetime, data_col15, label='AVG (TRP)')
ax1.plot(datetime, data_col16, label='TCR')

ax1.plot(datetime, data_col7, label='CP Rear')
ax1.plot(datetime, data_col8, label='CP Front')

# ax1.plot(datetime, data_col9, label='Pressure (V)')
# ax1.plot(datetime, data_col10, label='Pressure (mbar)')

# #limits
ax1.plot(datetime, data_col11, color='red')
ax1.plot(datetime, data_col12, color='red')
ax1.plot(datetime, data_col13, color='red')
ax1.plot(datetime, data_col14, color='red')

#ticks formatting for datetime
ticksSkip = len(datetime)//200
ticksUsed = datetime[::ticksSkip]
tickLabel = [ i for i in ticksUsed]
ax1.set_xticks(ticksUsed)
ax1.set_xticklabels(tickLabel)


fig.autofmt_xdate()
ax1.xaxis.set_major_formatter(DateFormatter('%m/%d %H:%M'))
ax1.set_title('PROBA-3 Glued Assemblies( MARSIM-2 ) \n Mechanical System Laboratory')
ax1.set_xlabel('date/time')
ax1.set_ylabel('Temperature Change Rate (°C/min)')
# ax1.set_ylim([-1.5, 1.5])
ax1.grid()
ax1.legend()

plt.show()
