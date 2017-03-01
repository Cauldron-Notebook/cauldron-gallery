import cauldron as cd
import numpy as np
from statsmodels.tsa.stattools import acf, pacf
from bokeh.plotting import Figure

df_history = cd.shared.df_history

temperatures = df_history['temperature'].values
acf_result = acf(temperatures, nlags=24)
pacf_result = pacf(temperatures, nlags=24, method='ols')


def make_correlation_figure(correlation_values, title):
    """
    Creates a correlation function plot with confidence intervals for
    determining the ARIMA ordering

    :param correlation_values:
        The computed correlation function values
    :param title:
        Tile for the plot
    :return:
        A Bokeh figure populated with traces for the correlation function
        display
    """

    count = len(correlation_values)

    figure = Figure(title=title)
    figure.line(x=[0, count], y=-1.96/np.sqrt(len(temperatures)), color='black')
    figure.line(x=[0, count], y=1.96/np.sqrt(len(temperatures)), color='black')
    figure.line(x=list(range(count)), y=correlation_values)
    figure.scatter(x=list(range(count)), y=correlation_values, size=6)

    return figure


cd.display.bokeh(make_correlation_figure(
    acf_result,
    'Autocorrelation Function'
))

cd.display.bokeh(make_correlation_figure(
    pacf_result,
    'Partial Autocorrelation Function'
))
