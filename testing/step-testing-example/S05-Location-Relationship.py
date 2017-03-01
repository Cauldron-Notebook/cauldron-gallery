import cauldron as cd
import pandas as pd
from bokeh.plotting import Figure

# Retrieve shared data
df_results = cd.shared.df_results  # type: pd.DataFrame

df_locations = pd.read_csv('data/locations.csv')
df = pd.merge(df_results, df_locations, on='sensor_index')

cd.display.markdown(
    """
    # Location Relationship

    The farmer's field is not flat. Different parts of the field face different
    directions, which can be determined from a topographical map. A
    topographical angle of zero corresponds to a Northerly pointing direction,
    and a value of +180 or -180 degrees corresponds to a Southerly pointing
    direction. Plotting the determined temperature lags versus the pointing
    direction of the field at the location of each ground sensor yields:
    """
)

figure = Figure(
    title='Ground-Level Temperature Lag versus Topographical Direction',
    x_axis_label='Ground Facing Direction (Degrees)',
    y_axis_label='Ground-Level Temperature Lag (Hours)'
)

figure.scatter(df['angle'], df['lag'], size=12)

cd.display.bokeh(figure)

cd.display.markdown(
    """
    There is an indication here of temperature lag with respect to pointing
    direction. This makes sense as the sun shines longer and more directly
    on some angles relative to others. More data would potentially allow for
    a relationship to be determined that would give the farmer a better
    understanding of the variation in temperatures in the field and allow her
    to adjust crop planting and care accordingly.
    """
)
