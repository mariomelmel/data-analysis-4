import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters

register_matplotlib_converters()


def draw_line_plot(df):
    # Draw line plot
    ax = df.plot(x='date', xlabel='Date', ylabel='Page Views', kind='line',
                 title='Daily freeCodeCamp Forum Page Views 5/2016-12/2019', color='red', legend=False)
    fig = ax.get_figure()
    plt.show()

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig


def draw_bar_plot(df):
    # Copy and modify data for monthly bar plot
    df_bar = split_date(df)

    # Draw bar plot
    bar_plot = sns.barplot(x='year', y='value', hue='month', data=df_bar, ci=None,
                           hue_order=['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August',
                                      'September', 'October', 'November', 'December'])
    ax = bar_plot
    bar_plot.set(xlabel='Years', ylabel='Average Pages Views')
    fig = ax.get_figure()
    plt.show()

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig


def draw_box_plot(df):
    # Prepare data for box plots (this part is done!)
    df = split_date(df)

    # Draw box plots (using Seaborn)
    box_plot = sns.boxplot(x='year', y='value', data=df)
    ax1 = box_plot
    box_plot.set(xlabel='Year', ylabel='Pages Views', title='Year-wise Box Plot (Trend)')
    fig1 = ax1.get_figure()
    plt.show()

    box_plot = sns.boxplot(x='month', y='value', data=df,
                            order=['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August',
                                   'September', 'October', 'November', 'December'])
    ax2 = box_plot
    box_plot.set(xlabel='Month', ylabel='Pages Views', title='Month-wise Box Plot (Seasonality)')
    fig2 = ax2.get_figure()
    plt.show()

    # Save image and return fig (don't change this part)
    fig1.savefig('box_plot1.png')
    fig2.savefig('box_plot2.png')

    return fig1, fig2


def split_date(df):
    df['date'] = pd.to_datetime(df['date'])
    df['year'] = pd.DatetimeIndex(df['date']).year
    df['month'] = pd.DatetimeIndex(df['date']).month

    month_dict = {
        1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June', 7: 'July', 8: 'August',
        9: 'September', 10: 'October', 11: 'November', 12: 'December'
    }
    df['month'] = df['month'].apply(lambda x: month_dict[x])

    return df


def main():
    # Import data (Make sure to parse dates. Consider setting index column to 'date'.)
    df = pd.read_csv('fcc-forum-pageviews.csv')

    # Clean data
    df = df.drop(df[df['value'] <= df['value'].quantile(0.025)].index |
                 df[df['value'] >= df['value'].quantile(0.975)].index)

    draw_line_plot(df)
    draw_bar_plot(df)
    draw_box_plot(df)


if __name__ == "__main__":
    main()
