import numpy as np
from matplotlib import pyplot as plt

c=['#e41a1c', '#377eb8', '#4daf4a', '#984ea3']
plt.style.use('seaborn-talk')
plt.style.use('seaborn-ticks')


def plot_data(data, c = c):
    n_samples = data.shape[1]
    n_subj = data.shape[0]
    one = np.ones(n_samples)
    noise = np.random.rand((n_samples))-0.5

    fig, ax = plt.subplots(1,3, figsize=(15,5))
    for i in range(n_subj):
        s = i+1
        ax[0].scatter(one*s+noise, data[i,:], color=c[i], label= f"subject {s}")
    ax[0].legend()
    ax[0].set_title("subject data")
    ax[0].spines['top'].set_visible(False)
    ax[0].spines['right'].set_visible(False)
    ax[0].spines['bottom'].set_visible(False)

    ax[1].scatter(np.arange(1,n_subj+1), data.mean(axis=1), color=c)
    ax[1].errorbar(np.arange(1,n_subj+1), data.mean(axis=1), yerr=data.std(axis=1), capsize=4, ecolor="black", fmt='none')
    ax[1].scatter(np.arange(1,n_subj+1), data.mean(axis=1), color=c)
    ax[1].set_title("error by subject")
    ax[1].spines['top'].set_visible(False)
    ax[1].spines['right'].set_visible(False)
    ax[1].spines['bottom'].set_visible(False)

    ax[2].errorbar(1, data.mean(), yerr=data.std(), capsize=4, ecolor="black", fmt='o', marker='s', mfc='yellow', mec='black', ms=20, mew=4)
    ax[2].set_title("overall error bar")
    ax[2].set_xticklabels([])
    ax[2].spines['top'].set_visible(False)
    ax[2].spines['bottom'].set_visible(False)
    ax[2].spines['right'].set_visible(False)
    ax[2].set_xticks([])
    return fig, ax