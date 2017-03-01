import cauldron as cd
import pandas as pd

# Load the city shared variable. If not set, default to chicago
city = cd.shared.fetch('city', 'chicago')  # type: str

# Load the historical and 2016 temperature data sets for the specified
# city
df_2016 = pd.read_csv('data/{}/temperatures.csv'.format(city))
df_history = pd.read_csv('data/{}/historical_temperatures.csv'.format(city))

cd.display.header('{} Temperatures (2016)'.format(city.capitalize()))
cd.display.table(df_2016)

cd.display.header('{} Temperatures (2006-2015)'.format(city.capitalize()))
cd.display.table(df_history, 0.3)

# Share loaded data with other steps
cd.shared.put(
    df_2016=df_2016,
    df_history=df_history
)
