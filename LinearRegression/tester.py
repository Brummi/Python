import matplotlib.pyplot as pyplot
import json
import numpy
import LinearRegression.linear_regression as l_r

#sample = numpy.genfromtxt('sample.csv', delimiter=",")
json_file = json.load(open('2017-04-03.json', 'r'))
sample = []
i = 0
for l in json_file:
    sample.append([i, l["close"]])
    i += 1

x_data = [x[0] for x in sample]
y_data = [x[1] for x in sample]

x_start = [0, 0]

pyplot.ion()

fig = pyplot.figure()

line_plt = fig.add_subplot(111)
sample_plt = fig.add_subplot(111)
sample_plt.plot(x_data, y_data, "o")
line_plt.plot([0, len(x_data)-1], [x_start[1], x_start[0]*len(x_data)+x_start[1]],  "r")

pyplot.grid(True)


pyplot.show()

A, b = l_r.calculate_A_b(sample)

for i in range(20):
    pyplot.pause(0.5)
    x_start = l_r.steepest_descent_step(x_start, A, b)
    line_plt.clear()
    pyplot.grid(True)
    sample_plt.plot(x_data, y_data, "o")
    line_plt.plot([0, len(x_data)-1], [x_start[1], x_start[0]*len(x_data)+x_start[1]],  "r")
    print("Step: ", i)