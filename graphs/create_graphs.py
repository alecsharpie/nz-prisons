import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def rate_graph():

    pop_df = pd.read_csv('data/imprisonment_per_population.csv')

    fig, ax = plt.subplots(2, 1, figsize=(8, 6))
    sns.set_style("ticks")
    sns.set_palette('colorblind')

    sns.swarmplot(data=pop_df,
                  y='rate',
                  x='continent',
                  ax=ax[0],
                  s=4,
                  order=pop_df.groupby('continent').mean().sort_values(
                      'rate', ascending=False).index)
    ax[0].annotate(text='NZ',
                   xy=(2, 219),
                   fontsize=13,
                   xytext=(2.3, 255),
                   arrowprops={
                       'arrowstyle': "->",
                       'color': 'grey'
                   })
    ax[0].set_title('Prisoners per 100,000 Population', loc = 'left', fontsize = 14)
    ax[0].set_ylabel('')
    ax[0].set_xlabel('')
    sns.despine(ax=ax[0])

    ax[1].plot([0, 222], [0, 0], color='#033553', linewidth=3)
    ax[1].plot([0, 222], [0.00005, 0.00005], color='white', linewidth=1)
    ax[1].plot([1, 61, 222], [0, 0, 0],
               color='#033553',
               marker='o',
               linewidth=0,
               markersize=6)
    ax[1].plot([1, 61, 222], [0, 0, 0],
               color='white',
               marker='o',
               linewidth=0,
               markersize=4)
    ax[1].annotate(text='NZ',
                   xy=(61, 0),
                   fontsize=13,
                   xytext=(53, 0.003),
                   arrowprops={
                       'arrowstyle': "->",
                       'color': 'grey'
                   })
    ax[1].annotate(text='Guinea-Bissau',
                   xy=(222, 0),
                   fontsize=10,
                   xytext=(202, 0.003),
                   arrowprops={
                       'arrowstyle': "->",
                       'color': 'grey'
                   })
    ax[1].annotate(text='United States',
                   xy=(1, 0),
                   fontsize=10,
                   xytext=(-19, 0.003),
                   arrowprops={
                       'arrowstyle': "->",
                       'color': 'grey'
                   })
    plt.ylim((-0.01, 0.01))
    sns.despine(ax=ax[1], left=True, bottom=True)
    ax[1].set(yticklabels=[], xticklabels=[])
    ax[1].tick_params(left=False, bottom=False)

    return fig


def drugs_graph():

    conviction_count = pd.read_csv('data/drug_conviction_count.csv')


    fig, ax = plt.subplots(figsize=(8, 6))
    sns.set_style("ticks")
    sns.set_palette('colorblind')
    sns.lineplot(data=conviction_count, hue='drug', x='year', y='count', ax=ax)
    plt.legend(title='Drug')
    plt.xlabel('Year')
    plt.ylabel('Number of Offences')
    sns.despine()

    return fig
