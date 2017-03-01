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
