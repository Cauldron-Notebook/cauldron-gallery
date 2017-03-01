import math

import cauldron as cd

from _temperatures import plots

# Retrieve shared data
df_2016 = cd.shared.df_2016
df_history = cd.shared.df_history
models = cd.shared.models


def predict(model_data):
    prediction = model_data.results.predict(
        start=len(df_history),
        end=len(df_history) + 11
    )
    return model_data, prediction

predictions = [predict(md) for md in models]


def plot_prediction(model_data, prediction):
    figure = plots.create_arima_plot(df_history, model_data)

    temps = df_2016['temperature'].values
    rss_predict = sum([(x - y) ** 2 for x, y in zip(temps, prediction)])
    rmse_predict = math.sqrt(rss_predict) / len(temps)

    plots.add_to_arima_plot(
        figure,
        df_2016['order'],
        df_2016['temperature'],
        legend='Actual',
        color='#999999'
    )

    plots.add_to_arima_plot(
        figure,
        df_2016['order'],
        prediction,
        legend='Prediction',
        color='orange'
    )

    figure.title = ' '.join([
        '({p}, {d}, {q})',
        'RMSE: {rmse:0.4f}',
        '[Forecast RMSE: {rmse_predict:0.4f}]'
    ]).format(
        rmse_predict=rmse_predict,
        **model_data._asdict()
    )

    cd.display.bokeh(figure)


[plot_prediction(*prediction) for prediction in predictions]
