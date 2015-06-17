import matplotlib.pyplot as plt
import matplotlib.cm as cm
import argparse as ap
from numpy import linspace

def plot_string(text, do_multi=False):
    """plot data stored as text"""

    sensors = text.split(';')
    data = [i.split() for i in sensors]
    data_t = list(zip(*data))

    fig = plt.figure()
    colors = iter(cm.rainbow(linspace(0, 1, len(data_t))))

    for n,y in enumerate(data_t):
        if do_multi:
            sb_plt = fig.add_subplot(len(data_t),1,n+1)
        plt.plot(range(len(y)), y, color = next(colors))
#        plt.axis([0, len(y), 0, max(int(n) for n in y)])

    plt.savefig("dino.png")

if __name__ == "__main__":
    parser = ap.ArgumentParser(description='Process some integers.')
    parser.add_argument('file', metavar='F', type=str, nargs='?',
                   help='file to read')

    args = parser.parse_args()

    f = open(args.file)
    text = f.readline()

    plot_string(text, True)
