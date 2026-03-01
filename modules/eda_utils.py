import matplotlib.pyplot as plt
import pandas as pd


def plot_distribution(df, column):
    plt.figure(figsize=(6,4))
    df[column].hist(bins=50)
    plt.title(f'Distribution of {column}')
    plt.xlabel(column)
    plt.ylabel('Frequency')
    plt.show()


def plot_day_of_week(df):
    median_cases = df.groupby('day_of_week')['daily_cases_clean'].median()

    plt.figure(figsize=(6,4))
    median_cases.plot(kind='bar')
    plt.title('Median Daily COVID Cases by Day of Week')
    plt.xlabel('Day of Week (0=Mon)')
    plt.ylabel('Median Daily Cases')
    plt.show()


def plot_weekend_box(df):
    plt.figure(figsize=(6,4))
    df.boxplot(column='daily_cases_clean', by='is_weekend')
    plt.title('Weekend vs Weekday COVID Cases')
    plt.suptitle('')
    plt.xlabel('Weekend (1=True)')
    plt.ylabel('Daily Cases')
    plt.show()


def plot_relationship(df, mobility_col):
    plt.figure(figsize=(6,4))
    plt.scatter(df[mobility_col], df['daily_cases_clean'], alpha=0.2)
    plt.title(f'{mobility_col} vs Daily COVID Cases')
    plt.xlabel(mobility_col)
    plt.ylabel('Daily Cases')
    plt.show()


def plot_time_trend(df):
    daily_avg = df.groupby('date')['daily_cases_clean'].mean()

    plt.figure(figsize=(10,4))
    daily_avg.rolling(7).mean().plot()
    plt.title('7-Day Rolling Average COVID Cases')
    plt.ylabel('Average Daily Cases')
    plt.show()