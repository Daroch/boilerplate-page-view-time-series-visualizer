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
    fig =plt.plot(df_clean.index, df_clean['value'], color='red')
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')
    # Save image and return fig (don't change this part)
    plt.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df_clean.copy()
    df_bar['month'] = df_bar.index.month
    df_bar['year'] = df_bar.index.year
    df_bar =df_bar.groupby([df_bar["year"],df_bar["month"]]).mean()


    # Draw bar plot
    fig, ax = plt.subplots(figsize=(7,7))  # a figure with a single Axes
    fig=sns.barplot(x="year",y="value",hue="month",data=df_bar, legend='full',palette='bright',hue_order=[1,2,3,4,5,6,7,8,9,10,11,12])
    fig=plt.legend(title='Months')
    fig=fig.figure
    ax.set_title('Daily freeCodeCamp Average Views by month 5/2016-12/2019')
    ax.set_xlabel('Years')
    ax.set_ylabel('Average Page Views')

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df_clean.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    fig, axs = plt.subplots(1, 2, figsize=(9,3))  # a figure with a single Axes
    axs[0].set_title('Year-wise Box Plot (Trend)')
    axs[1].set_title('Month-wise Box Plot (Seasonality)')
    fig = sns.boxplot(x=df_box['year'], hue=df_box['year'],legend=False, y=df_box['value'], ax=axs[0],palette='bright',)
    fig = sns.boxplot(x=df_box['month'], hue=df_box['month'], legend=False, y=df_box['value'], ax=axs[1], palette='muted',order=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'])
    fig=fig.figure
    axs[0].set_xlabel('Year')
    axs[0].set_ylabel('Page Views')
    axs[1].set_xlabel('Month')
    axs[1].set_ylabel('Page Views')






    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
