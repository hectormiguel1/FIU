import pandas as pd
import numpy as np
from sklearn.manifold import TSNE
from sklearn.decomposition import PCA
import matplotlib.pyplot as plot
import seaborn as sns
import sys
import os.path


def visualizeTSNE(x, y):
    print('Starting TSNE visualization')
    label = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    tsne = TSNE(n_components=2, verbose=1, perplexity=15, n_iter=1000)

    tsne_results = tsne.fit_transform(x)
    df_t = pd.DataFrame(data=tsne_results, columns=['tSNE1', 'tSNE2'])

    j = 0
    for i in label:
        y = y.replace(j, i)
        j += 1

    df_t['digit'] = y
    sns.lmplot(x='tSNE1', y='tSNE2', data=df_t, hue='digit', fit_reg=False, legend=1, size=6)
    plot.show()

# Handle visualizing PCA

def visualizePCA(x):
    print('Starting PCA visualization')
    pca = PCA(n_components=2)
    pca.fit(x)
    PCAX = pca.transform(x)

    start = 0
    end = 100
    count = 0

    while count < 9:
        # print('Start: ', + start, ' End: ', end)
        plot.scatter(PCAX[start:end, 0], PCAX[start:end, 1])
        start += 100
        end += 100
        count += 1
    plot.show()


# Method display image from the given range.

def showDigits(x):
    fig, plots = plot.subplots(3, 4)
    start = 0
    end = 1
    plotx = 0
    ploty = 0
    while end < 1000:
        if plotx == 3:
            plotx = 0
            ploty += 1
        print(f'Adding Image to Plot {plotx},{ploty}')
        img = np.array(x[start:end]).reshape(28, 28) / 255
        plots[plotx, ploty].imshow(img)
        start += 100
        end += 100
        plotx += 1
    plot.show()


# Method handles processing of the data from CSV

def processData(data):
    print('Start processing data....')
    y = data.iloc[:, 0]
    x = data.drop('label', axis=1)
    showDigits(x)
    visualizePCA(x)
    visualizeTSNE(x, y)


# Accept data as argument to application.

def initialize():
    if len(sys.argv) <= 1:
        print('No Arguments provided')
        exit(1)
    else:
        filePath = sys.argv[1]
        print('Loading MIST CSV from ' + filePath)
        if os.path.isfile(filePath):
            data = pd.read_csv(filePath)
            processData(data)
        else:
            print('Provided File ' + filePath + ' does not exits')


if __name__ == "__main__":
    initialize()
