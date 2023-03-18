import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


def draw_plot():
    # Read data from file
    df = pd.read_csv('sea-level-predictor/epa-sea-level.csv')

    # Create scatter plot
    fig, ax = plt.subplots()
    ax.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    result = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    ax.plot(pd.Series(range(1880, 2051)), result.intercept +
            result.slope*pd.Series(range(1880, 2051)))

    # Create second line of best fit
    mask = df.loc[df['Year'] >= 2000]
    result = linregress(mask['Year'], mask['CSIRO Adjusted Sea Level'])
    ax.plot(pd.Series(range(2000, 2051)), result.intercept +
            result.slope*pd.Series(range(2000, 2051)))

    # Add labels and title
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    ax.set_title('Rise in Sea Level')

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
