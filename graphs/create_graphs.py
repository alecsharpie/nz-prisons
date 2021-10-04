import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from graphs.utils import get_demo_data, get_year_ticks

def conv_rate_graph():

    cvc_df = pd.read_csv('data/conviction_rates')

    fig, ax = plt.subplots(figsize=(8, 6))
    sns.set_style("ticks")
    sns.set_palette('colorblind')
    sns.lineplot(data = cvc_df, x = 'year', y = 'rate', hue = 'ethnicity')
    plt.legend(title='Drug')
    plt.xlabel('Year')
    plt.ylabel('Conviction rate if charged (%)')
    sns.despine()

    return fig


def rate_graph():

    pop_df = pd.read_csv('data/imprisonment_per_population.csv')

    pal1 = sns.color_palette("colorblind", 6)
    sns.set_palette(pal1)

    fig, ax = plt.subplots(2, 1, figsize=(8, 6))

    ax[0].plot([0, 222], [0, 0], color='#033553', linewidth=3)
    ax[0].plot([0, 222], [0.00005, 0.00005], color='white', linewidth=1)
    ax[0].plot([74, 148, 222], [0, 0, 0],
               color='#033553',
               marker='o',
               linewidth=0,
               markersize=4)
    ax[0].plot([1, 161, 222], [0, 0, 0],
               color='#033553',
               marker='o',
               linewidth=0,
               markersize=6)
    ax[0].plot([1, 161, 222], [0, 0, 0],
               color='white',
               marker='o',
               linewidth=0,
               markersize=4)
    ax[0].annotate(text='61st highest imprisonment rate',
                   xy=(85, 0),
                   fontsize=13,
                   xytext=(85, 0.006))
    ax[0].annotate(text='NZ',
                   xy=(161, 0),
                   fontsize=13,
                   xytext=(154, 0.003),
                   arrowprops={
                       'arrowstyle': "->",
                       'color': 'grey'
                   })
    ax[0].annotate(text='Lowest imprisonment rate\n\nGuinea-Bissau',
                   xy=(1, 0),
                   fontsize=10,
                   xytext=(-19, 0.003),
                   arrowprops={
                       'arrowstyle': "->",
                       'color': 'grey'
                   })
    ax[0].annotate(text='Highest imprisonment rate\n\nUnited States',
                   xy=(222, 0),
                   fontsize=10,
                   xytext=(202, 0.003),
                   arrowprops={
                       'arrowstyle': "->",
                       'color': 'grey'
                   })
    ax[0].set_ylim((-0.01, 0.01))
    sns.despine(ax=ax[0], left=True, bottom=True)
    ax[0].set(yticklabels=[], xticklabels=[])
    ax[0].tick_params(left=False, bottom=False)

    sns.swarmplot(data=pop_df,
                  y='rate',
                  x='continent',
                  ax=ax[1],
                  s=4,
                  order=pop_df.groupby('continent').mean().sort_values(
                      'rate', ascending=False).index)
    ax[1].annotate(text='NZ',
                   xy=(2, 219),
                   fontsize=13,
                   xytext=(2.3, 255),
                   arrowprops={
                       'arrowstyle': "->",
                       'color': 'grey'
                   })
    ax[1].set_title('Prisoners per 100,000 Population', loc = 'left', fontsize = 14)
    ax[1].set_ylabel('')
    ax[1].set_xlabel('')
    sns.despine(ax=ax[1])

    return fig


def drugs_graph():

    conviction_count = pd.read_csv('data/drug_conviction_count.csv')

    pal1 = sns.color_palette("colorblind", 6)
    sns.set_palette(pal1)

    fig, ax = plt.subplots(figsize=(8, 6))

    sns.lineplot(data=conviction_count, hue='drug', x='year', y='count', ax=ax)
    plt.legend(title='Drug')
    plt.xlabel('Year')
    plt.ylabel('Number of Offences')
    sns.despine()

    return fig

def demo_graph():

    age_df = get_demo_data('age')

    fig, ax = plt.subplots(3, 1, figsize=(8, 12))

    sns.barplot(x = 'year', y = 'cumsum', data = age_df, hue = 'age', dodge = False, palette = 'colorblind', ci = None, ax = ax[0])
    sns.despine(ax = ax[0])
    ax[0].legend(loc = 'lower left', framealpha = 0.9)
    ax[0].set_ylim((0, 100))
    ax[0].set_title('Age', loc = 'left', fontsize = 14)
    ax[0].set_ylabel('% of Total Convictions')
    ax[0].set_xlabel('Year')
    ax[0].set_xticks(range(len(list(age_df.year.unique()))))
    ax[0].set_xticklabels(get_year_ticks())

    gender_df = get_demo_data('gender')
    sns.barplot(x = 'year', y = 'cumsum', data = gender_df, hue = 'gender', dodge = False, palette = 'colorblind', ci = None, ax = ax[1])
    sns.despine(ax = ax[1])
    ax[1].legend(loc = 'lower left', framealpha = 0.9)
    ax[1].set_ylim((0, 100))
    ax[1].set_title('Gender', loc = 'left', fontsize = 14)
    ax[1].set_ylabel('% of Total Convictions')
    ax[1].set_xlabel('Year')
    ax[1].set_xticks(range(len(list(gender_df.year.unique()))))
    ax[1].set_xticklabels(get_year_ticks())

    eth_df = get_demo_data('ethnicity')
    sns.barplot(x = 'year', y = 'cumsum', data = eth_df, hue = 'ethnicity', dodge = False, palette = 'colorblind', ci = None, ax = ax[2])
    sns.despine(ax = ax[2])
    ax[2].legend(loc = 'lower left', framealpha = 0.9)
    ax[2].set_ylim((0, 100))
    ax[2].set_title('Ethnicity', loc = 'left', fontsize = 14)
    ax[2].set_ylabel('% of Total Convictions')
    ax[2].set_xlabel('Year')
    ax[2].set_xticks(range(len(list(eth_df.year.unique()))))
    ax[2].set_xticklabels(get_year_ticks())

    plt.tight_layout()

    return fig

def staff_graph():
    svp_df = pd.read_csv("data/staff_v_prisoner.csv")
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.set_style("ticks")
    sns.set_palette('colorblind')
    sns.barplot(data=svp_df,
                y='role',
                x='cumsum',
                hue='ethnicity',
                palette='colorblind',
                dodge=False,
                ax=ax)
    plt.legend(title='Ethnicity')
    plt.xlabel('% who identify with each ethnicity')
    plt.ylabel('')
    sns.despine()
    return fig


def reimprisonment_graph():
    reimp_df = pd.read_csv('data/reimprisonment.csv').set_index('sentence_length')

    fig, ax = plt.subplots(figsize=(8, 6))
    sns.set_style("ticks")
    sns.set_palette('colorblind')
    ax = sns.heatmap(reimp_df, linewidth=0.5, cmap = 'OrRd', cbar_kws={'label': '% Reimprisonment'})
    plt.yticks(rotation=0)
    plt.xlabel('Months since release')
    plt.ylabel('Previous sentence length')
    return fig
