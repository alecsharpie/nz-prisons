import pandas as pd
import numpy as np

def get_demo_data(col):

    df = pd.read_csv(f'data/{col}.csv')

    df = df.set_index(col).stack().to_frame(name='count').reset_index()

    df.columns = [col, 'year', 'count']

    if col != 'gender':
        df = df[df[col] != 'Unknown']

    df['count'] = df['count'].str.replace(',', '').astype(int)

    df = df.merge(df.groupby('year').sum().reset_index().rename(
        columns={'count': 'total'}),
                  on='year')

    df['pct'] = df['count'] / df['total'] * 100

    df['cumsum'] = df.groupby('year')['pct'].cumsum()

    if col == 'age':

        df[col] = df[col].map({
            '65 years and over': 'Over 60',
            '60-64': 'Over 60',
            '55-59': '50-59',
            '50-54': '50-59',
            '45-49': '40-49',
            '40-44': '40-49',
            '35-39': '30-39',
            '30-34': '30-39',
            '25-29': '20-29',
            '20-24': '20-29',
            '19 years and under': ' Under 19'
        })

    return df.sort_values(['year', 'cumsum'], ascending=[True, False])


def get_year_ticks():
    years = [1980, 1990, 2000, 2010, 2020]
    yticks = []
    for y in years[-1:0:-1]:
        yticks = yticks + [y] + ([""] * 9)
    yticks = yticks + [1980]
    return yticks[::-1]
