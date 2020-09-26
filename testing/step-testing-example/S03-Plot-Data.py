import cauldron as cd

import pandas as pd
from bokeh.plotting import Figure

# Retrieve loaded data frames
sensors = cd.shared.sensors
df_aerial = cd.shared.df_aerial


def plot_sensor_data(df_sensor: pd.DataFrame):
    """
    Creates a line plot for the temperature data of the given sensor with a
    reference line for the aerial temperature.

    :param df_sensor:
        Data frame for the sensor to be plotted
    """

    figure = Figure(
        title='Temperature Data for Sensor #{}'.format(
            int(df_sensor.iloc[0]['sensor_index'])
        ),
        x_axis_label='Time of Day (Hours)',
        y_axis_label='Temperature (Celsius)'
    )

    figure.line(df_aerial['time'], df_aerial['temperature'])
    figure.line(df_sensor['time'], df_sensor['temperature'], color='red')
    cd.display.bokeh(figure, scale=0.3)


cd.display.markdown(
    """
    # Temperature Plots

    The following plots show (in red) a 24-hour cycle of temperatures for a
    ground-level sensor and (in blue) the aerial temperature sensor values as
    a reference.
    """
)

# Create a plot for each sensor
for df in sensors:
    plot_sensor_data(df)
