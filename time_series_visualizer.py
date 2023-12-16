import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv', index_col='date', parse_dates=True)

# Clean data
condition = df['value'] >= df['value'].quantile(0.025)
condition2 = df['value'] <= df['value'].quantile(0.975)
df_clean = df[condition & condition2]


def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots(figsize=(15,5))  # a figure with a single Axes
    fig=plt.plot(color='red')
    fig =sns.lineplot(df_clean)
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    fig=fig.figure
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df_clean.copy()
    df_bar=df_bar.groupby(df_bar.index.year).mean()


    # Draw bar plot
    fig, ax = plt.subplots(figsize=(15,15))  # a figure with a single Axes
    fig=sns.barplot(df_bar)
    fig=fig.figure

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





    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
