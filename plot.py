import matplotlib.pyplot as plt
import matplotlib.cm as cm
from numpy import linspace

def plot_string(text):
    """plot data stored as text"""

    sensors = text.split(';')
    data = [i.split() for i in sensors]
    data_t = zip(*data)

    fig = plt.figure()
    colors = iter(cm.rainbow(linspace(0, 1, len(data_t))))

    for n,y in enumerate(data_t):
        sb_plt = fig.add_subplot(len(data_t),1,n)
        plt.scatter(range(len(y)), y, color = next(colors))
#        plt.axis([0, len(y), 0, max(int(n) for n in y)])

    plt.savefig("dino.png")
