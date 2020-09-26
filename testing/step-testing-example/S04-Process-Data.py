import math

import cauldron as cd
import numpy as np
import pandas as pd
from bokeh.plotting import Figure

# Retrieve loaded data frames
sensors = cd.shared.sensors
df_aerial = cd.shared.df_aerial


def mean_offset_rmse(df: pd.DataFrame, offset: int) -> float:
    """ Calculate the mean RMSE for a given offset index """

    if offset < 0:
        sensor_values = df['temperature'].values[:offset]
        aerial_values = df_aerial['temperature'].values[-offset:]
    elif offset > 0:
        sensor_values = df['temperature'].values[offset:]
        aerial_values = df_aerial['temperature'].values[:-offset]
    else:
        sensor_values = df['temperature']
        aerial_values = df_aerial['temperature']

    rss_values = [(s - a) ** 2 for s, a in zip(sensor_values, aerial_values)]

    return math.sqrt(sum(rss_values)) / len(rss_values)


def process(df: pd.DataFrame) -> dict:
    """
    Compute aggregate results for a given data frame and return a
    dictionary containing those results to be an entry in the results
    data frame.
    """
    if (df.empty):
        return

    sensor_index = df.iloc[0]['sensor_index']

    swing = int(0.5 * len(df))
    rmse_offsets = np.array(range(-swing, swing + 1))
    rmse_values = np.array([mean_offset_rmse(df, n) for n in rmse_offsets])
    lag = 0.25 * rmse_offsets[rmse_values.argmin()]

    figure = Figure(
        title='Mean RMSE Values for Sensor #{}'.format(int(sensor_index)),
        x_axis_label='Time Difference (Hours)',
        y_axis_label='Mean RMSE Value'
    )
    figure.line(0.25 * rmse_offsets, rmse_values)
    cd.display.bokeh(figure, 0.3)

    return dict(
        sensor_index=sensor_index,
        mean_temperature=df['temperature'].mean(),
        minimzed_mean_rmse=min(rmse_values),
        lag=lag
    )

cd.display.markdown(
    """
    # Calculate Lag

    To calculate the lag of a ground-level sensor in relation to the air
    temperature sensor, the mean RMSE is calculated with varying amounts
    temporal phase shifting between the two curves:

    $$$
        @overline{RMSE}(@delta) = @frac{1}{n} @left(
            @sum_{i=1}^N (T_{ground}(i + @delta) - T_{air}(i))^2
        @right)^{1/2}
    $$$

    The lag is then the phase shift at which the minimum mean RMSE value
    occurs. The following are the mean RMSE plots for each sensor:
    """
)

# Create combined results data frame from the processed results of each
# source data frame
df_results = pd.DataFrame([process(df) for df in sensors])

# Show results
cd.display.header('Sensor Results')
cd.display.table(df_results)

# Share for later use
cd.shared.df_results = df_results
