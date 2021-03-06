"""
Name:           Brian Nguyen
Class:          EE 381 - Probability & Stats
Start Date:     3/15/19
End Date:       3/20/19
"""

import numpy as np
import matplotlib.pyplot as plt


# Generate the values of the RV X
def central_limit(nbooks):
    N = 100000
    a = 1
    b = 4
    mu_x = (a + b) / 2
    sig_x = np.sqrt((b - a) ** 2 / 12)
    X = np.zeros((N, 1))
    for k in range(0, N):
        x = np.random.uniform(a, b, nbooks)
        w = np.sum(x)
        X[k] = w
    # Create bins and histogram
    nbins = 30  # Number of bins
    edgecolor = 'w'  # Color separating bars in the bargraph
    #
    bins = [float(x) for x in np.linspace(nbooks * a, nbooks * b, nbins + 1)]
    h1, bin_edges = np.histogram(X, bins, density=True)
    # Define points on the horizontal axis
    be1 = bin_edges[0:np.size(bin_edges) - 1]
    be2 = bin_edges[1:np.size(bin_edges)]
    b1 = (be1 + be2) / 2
    barwidth = b1[1] - b1[0]  # Width of bars in the bargraph
    plt.close('all')

    # PLOT THE BAR GRAPH AND CALCULATE THE MEAN AND STANDARD DEVIATION
    fig1 = plt.figure(1)
    plt.bar(b1, h1, width=barwidth, edgecolor=edgecolor)
    if nbooks == 1:
        f = unif_pdf(a, b, b1)
        mu_x = np.mean(x)
        sig_x = np.std(x)
    else:
        f = gaussian(mu_x * nbooks, sig_x * np.sqrt(nbooks), b1)
        mu_x = np.mean(x) * nbooks
        sig_x = np.std(x) * np.sqrt(nbooks)
    plt.plot(b1, f, 'r')
    plt.show()

    print('---------------\nnbooks = ', nbooks)
    print('mu_x = ', mu_x)
    print('sig_x = ', sig_x)


# PLOT THE GAUSSIAN FUNCTION
def gaussian(mu, sig, z):
    f = np.exp(-(z - mu) ** 2 / (2 * sig ** 2)) / (sig * np.sqrt(2 * np.pi))
    return f


# PLOT THE UNIFORM PDF
def unif_pdf(a,b,x):
    f = (1/abs(b-a))*np.ones(np.size(x))
    return f


def main():
    central_limit(1)
    central_limit(5)
    central_limit(15)


main()
