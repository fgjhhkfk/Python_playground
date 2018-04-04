import matplotlib
import matplotlib.pyplot as plt
from matplotlib import dates
import datetime
import numpy as np

plt.xkcd()
date = []
gatz = []
hjk = []
whiteSpaceRegex = "\\s";
f = open('/home/hjk/tippkick.md', 'r')
for line in f:
    date.append(line.split()[0])
    gatz.append(line.split()[3])
    hjk.append(line.split()[1])
    # print(date)
    # print(repr(line))
gatz = map(int, gatz)
hjk = map(int, hjk)

diff_wins = np.subtract(np.array(hjk), np.array(gatz))
num_games = np.add(np.array(hjk), np.array(gatz))

converted_dates = map(datetime.datetime.strptime, date, len(date)*['%y%m'])

color_gatz = '#0000ff'
color_hjk = '#ff0000'

# Meiste Siege in einem Monat
max_gatz = max(gatz)
max_hjk = max(hjk)

# Wenigste Siege in einem Monat
min_gatz = min(gatz)
min_hjk = min(hjk)

# Monate aufeinanderfolgend gewonnen
def countlist(Liste):
    max_consecutive = 0
    count = 1
    for i in range(len(Liste) - 1):
        if Liste[i]>0 and Liste[i+1]>0:
            count += 1
        elif count > max_consecutive:
            max_consecutive = count
            count = 1
        else:
            count = 1
    return max_consecutive

consecutive_hjk = countlist(diff_wins)
consecutive_gatz = countlist(diff_wins*-1)

# hoechste Monatssiege
high_win_hjk = max(diff_wins)
high_win_gatz = min(diff_wins)*-1

# durchschnittliche Siege pro Monat
average_hjk = np.round(np.mean(hjk), decimals=1)
average_gatz = np.round(np.mean(gatz), decimals=1)

# Plots

# Siege im Monat
fig = plt.figure()
ax = fig.add_subplot(211)
plt.plot_date(converted_dates, gatz, color=color_gatz, linestyle='solid', label='gatz')
plt.plot_date(converted_dates, hjk, color=color_hjk, linestyle='solid', label='hjk')
ax.xaxis.grid(linewidth=1.0)
ax.yaxis.grid(linewidth=1.0)
plt.legend(bbox_to_anchor=(0.5, 1.2),ncol=2,loc=9)

# Differenz der Siege im Monat
ax = fig.add_subplot(212)
plt.plot_date(converted_dates, diff_wins, linestyle='solid', label='hjk-gatz')
plt.fill_between(converted_dates, diff_wins, 0, where=(diff_wins<=0), interpolate=True, facecolor=color_gatz, alpha='0.7')
plt.fill_between(converted_dates, diff_wins, 0, where=(diff_wins>=0), interpolate=True, facecolor=color_hjk, alpha='0.7')
ax.xaxis.grid(linewidth=1.0)
ax.yaxis.grid(linewidth=1.0)
plt.legend(bbox_to_anchor=(0.5, 1.2),ncol=2,loc=9)
plt.grid('on')
plt.savefig('/media/web/bilder/tippkick.png', dpi=150)

# morestats
fig, ax = plt.subplots()
X = np.arange(5)
plt.barh(X, [average_hjk*-1, max_hjk*-1, min_hjk*-1, consecutive_hjk*-1, high_win_hjk*-1], facecolor=color_hjk, label='hjk')
plt.barh(X, [average_gatz, max_gatz, min_gatz, consecutive_gatz, high_win_gatz], facecolor=color_gatz, label='gatz')
ax.xaxis.set_visible(True)
ax.yaxis.set_visible(False)
plt.xlim(-15,15)
yTicks = ['{} average wins {}'.format(average_hjk, average_gatz),
          '{} max. wins {}'.format(max_hjk, max_gatz),
          '{} min. wins {}'.format(min_hjk, min_gatz),
          '{} consecutive wins {}'.format(consecutive_hjk, consecutive_gatz),
          '{} highest win {}'.format(high_win_hjk, high_win_gatz)
          ]
for y in np.arange(5):
    plt.text(0, y, yTicks[y], ha='center', va= 'center')
plt.legend(bbox_to_anchor=(0.5, 1.1),ncol=2,loc=9)

plt.savefig('/media/web/bilder/morestats.png', dpi=150)
# plt.show()


