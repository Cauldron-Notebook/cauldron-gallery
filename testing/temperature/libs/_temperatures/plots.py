import pandas as pd
from bokeh.plotting import Figure

from _temperatures import arima


def create_arima_plot(
        df_history: pd.DataFrame,
        model_data: arima.MODEL_DATA
) -> Figure:
    """
    Plot the fitting data for the specified model

    :param df_history:
        The historical data that was fitted by the ARIMA model
    :param model_data:
        The MODEL_DATA instance to plot
    """

    results = model_data.results

    figure = Figure()
    figure.xaxis.axis_label = 'Year'
    figure.yaxis.axis_label = 'Temperature (Celsius)'

    df = df_history.sort_values(by='order')
    order = df['order']
    add_to_arima_plot(
        figure,
        order,
        df['temperature'].values,
        'Data',
        'blue'
    )

    add_to_arima_plot(
        figure,
        order,
        results.fittedvalues,
        'Model',
        'red'
    )

    figure.title = '({p}, {d}, {q}) RMSE: {rmse:0.4f}'.format(
        **model_data._asdict()
    )

    figure.legend.location = 'bottom_left'

    return figure


def add_to_arima_plot(
        figure: Figure,
        order,
        values,
        legend: str,
        color: str
):
    year = 0.01 * order.values
    delta = len(order) - len(values)
    figure.line(year[delta:], values, legend=legend, color=color)
    return figure.scatter(year[delta:], values, legend=legend, color=color)
