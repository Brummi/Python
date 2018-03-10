import matplotlib.pyplot as plt
import json


json_file = json.load(open('2017-04-03.json', 'r'))
t = range(len(json_file))
s = [x['close'] for x in json_file]
fig, ax = plt.subplots()
ax.plot(t, s)
ax.set(xlabel='time (2x min)', ylabel='Aktienkurs',
       title='2017-04-03')
ax.grid()
plt.show()