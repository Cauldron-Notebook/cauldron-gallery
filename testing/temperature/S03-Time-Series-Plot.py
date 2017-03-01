import cauldron as cd
import pandas as pd
from bokeh.charts import Scatter

from _temperatures import dates

# Retrieve shared data
df_2016 = cd.shared.df_2016
df_history = cd.shared.df_history

# Add date and order columns
df_history['order'] = dates.create_order_column(df_history)
df_history['date'] = df_history.apply(dates.get_date, axis=1)

df_2016['order'] = dates.create_order_column(df_2016)
df_2016['date'] = df_2016.apply(dates.get_date, axis=1)

# Combine data sets for display
df_all = pd.concat([df_history, df_2016], ignore_index=1)

cd.display.markdown(
    """
    # Time-Series Plot

    Next we plot the complete data set (historical and 2016) as a time series
    from beginning to end. Colors are used for each year to match
    the values in the previous plot.
    """
)

cd.display.bokeh(
    Scatter(
        df_all,
        x='date',
        y='temperature',
        color='year',
        title='Average Monthly Temperatures (2006-2016)',
        xlabel='Year',
        ylabel='Temperature (Celsius)'
    ),
    scale=0.8
)
