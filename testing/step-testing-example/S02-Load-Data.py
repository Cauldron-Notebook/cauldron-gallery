import cauldron as cd
import pandas as pd


def load_sensor_data(index: int) -> pd.DataFrame:
    """
    Loads the CSV file for the given sensor index and returns a DataFrame
    """

    path = 'data/sensor-{}.csv'.format(index)
    df = pd.read_csv(path)
    df['sensor_index'] = index
    return df


# Load data frames and share them for use in the next step
cd.shared.sensors = [load_sensor_data(index) for index in range(10)]
cd.shared.df_aerial = pd.read_csv('data/aerial.csv')

# Show the data in the display.

# Ground Sensor Data
cd.display.markdown(
    """
    # Ground Sensor Data
    """
)

for idx, sensor_data in enumerate(cd.shared.sensors):
    cd.display.header('Sensor {}'.format(idx))
    cd.display.table(sensor_data)

# Aerial Sensor Data
cd.display.markdown(
    """
    # Aerial Sensor Data
    """
)

cd.display.table(cd.shared.df_aerial)
