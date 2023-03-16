import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('page-view-time-series-visualizer/fcc-forum-pageviews.csv',
                 parse_dates=True, index_col='date')

# Clean data
df = df.loc[(df['value'] <= df['value'].quantile(.975)) &
            (df['value'] >= df['value'].quantile(.025))]


def draw_line_plot():
    # Draw line
    df_line = df.copy()
    fig, ax = plt.subplots()
    ax = sns.lineplot(data=df_line, x=df_line.index, y='value', color='red')
    ax.set(xlabel='Date', ylabel='Page Views',
           title='Daily freeCodeCamp Forum Page Views 5/2016-12/2019')

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig


def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()

    # Draw bar
    df_bar['year'] = df_bar.index.year.values
    df_bar['month'] = df_bar.index.month_name()

    month_list = ['January', 'February', 'March', 'April', 'May', 'June',
                  'July', 'August', 'September', 'October', 'November', 'December']
    fig, ax = plt.subplots()
    ax = sns.barplot(x='year', y='value', hue='month',
                     hue_order=month_list, data=df_bar)
    ax.set(xlabel='Years', ylabel='Average Page Views')

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig


def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    df_box['month_sort'] = df.index.month
    df_box.sort_values('month_sort', inplace=True)
    fig, ax = plt.subplots(1, 2, figsize=(14, 8))
    sns.boxplot(y="value", x="year", data=df_box, ax=ax[0])
    ax[0].set(title='Year-wise Box Plot (Trend)',
              xlabel='Year', ylabel='Page Views')
    sns.boxplot(x="month", y="value", data=df_box, ax=ax[1])
    ax[1].set(title='Month-wise Box Plot (Seasonality)',
              xlabel='Month', ylabel='Page Views')

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
