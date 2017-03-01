import cauldron as cd
import pandas as pd
from bokeh.charts import Scatter

# Retrieve shared data
df_2016 = cd.shared.df_2016
df_history = cd.shared.df_history

# Combine historical and 2016 data for plotting everything
df_all = pd.concat([df_history, df_2016], ignore_index=True)

cd.display.markdown(
    """
    # Plot by Month

    The combined historical and 2016 data is plotted on a
    monthly basis showing the overlap between the year-over-year.
    If a warming trend exists in the data it is small enough that it
    is not easily observable when plotted in this fashion.
    """
)

cd.display.bokeh(Scatter(
    df_all,
    x='month',
    y='temperature',
    color='year',
    title='Average Monthly Temperatures (2006-2016)',
    xlabel='Month',
    ylabel='Temperature (Celsius)'
))
