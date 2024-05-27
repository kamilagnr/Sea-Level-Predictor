import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    years = df['Year'].tolist()
    sea_lvl = df['CSIRO Adjusted Sea Level'].tolist()
    # Create scatter plot
    plt.figure()
    plt.scatter(years,sea_lvl)

    # Create first line of best fit
    stats = linregress(years, sea_lvl)
    slope = stats.slope
    intercept = stats.intercept
    new_years = range(years[0],2051)
    bfit = slope*new_years + intercept
    plt.plot(new_years,bfit,label='best fit 1')

    # Create second line of best fit
    years_from_2000 = range(2000,years[-1])
    sea_lvl_from_2000 = sea_lvl[:-len(years_from_2000)-1:-1]
    sea_lvl_from_2000.reverse()
    stats2 = linregress(years_from_2000, sea_lvl_from_2000)
    slope2 = stats2.slope
    intercept2 = stats2.intercept
    new_years_from_2000 = range(years_from_2000[0],2051)
    bfit2 = slope2*new_years_from_2000 + intercept2
    plt.plot(new_years_from_2000,bfit2,label='best fit 2')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
