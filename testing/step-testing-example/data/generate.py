import numpy as np
import pandas as pd
from random import randint
from scipy.interpolate import interp1d

SENSOR_COUNT = 10

angles = [randint(-180, 180) for i in range(SENSOR_COUNT)]

x_sources = [-8, -4, 0, 4, 8, 12, 16, 20, 24, 28, 32]
y_sources = [17, 13, 10, 8, 9, 11, 18, 14, 11, 8, 10]

interp_func = interp1d(x_sources, y_sources, kind='cubic')


def lag_from_angle(angle: int):
    angle_interp_func = interp1d([-180, -90, 0, 90, 180], [0, 0.75, 2, 1.25, 0])
    lag = 4 * int(round(float(angle_interp_func(angle))))
    return 0.25 * max(0, lag + randint(-1, 1))


def randomize(index: int) -> np.array:
    angle = angles[index]
    lag = lag_from_angle(angle)
    print('[{}]: ANGLE {} -> LAG {}'.format(index, angle, lag))
    x_values = np.arange(0 - lag, 23.75 - lag, 0.25)
    return np.array([y + 0.25 * randint(-4, 4) for y in interp_func(x_values)])


def create_data(index: int, make_random: bool = True) -> pd.DataFrame:
    x_values = np.arange(0, 23.75, 0.25)
    return pd.DataFrame(dict(
        time=x_values,
        temperature=randomize(index) if make_random else interp_func(x_values)
    ))


for i in range(SENSOR_COUNT):
    create_data(i, True).to_csv('sensor-{}.csv'.format(i), index=False)
    print('Created: {}'.format(i))

create_data(-1, False).to_csv('aerial.csv', index=False)
print('Created: aerial.csv')

df_location = pd.DataFrame(dict(
    sensor_index=list(range(SENSOR_COUNT)),
    angle=angles
))
df_location.to_csv('locations.csv', index=False)
print('Created: locations.csv')

print('Data creation operation complete')
