import sys
import os.path
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plot


def initialize():
    if len(sys.argv) <= 1:
        print('No path to Tips CSV Provided')
        exit(1)
    else:
        if os.path.isfile(sys.argv[1]):
            print('Reading ' + sys.argv[1] + '....')
            df = pd.read_csv(sys.argv[1])
            currentColumn = 0
            fig, plots = plot.subplots(2, 7)
            plotx = 0
            ploty = 0
            while currentColumn < len(df.columns):
                if plotx == 2:
                    plotx = 0
                    ploty += 1
                print(f'Plotting violin plot on location {plotx}, {ploty}')
                plots[plotx, ploty].set_title(f'C{currentColumn + 1} of housing data')
                sns.violinplot(data=df[df.columns[currentColumn]], ax=plots[plotx, ploty], )
                currentColumn += 1
                plotx += 1
            plot.show()
        else :
            print('File ' + sys.argv[1] + ' not found!')


if __name__ == '__main__':
    initialize()
