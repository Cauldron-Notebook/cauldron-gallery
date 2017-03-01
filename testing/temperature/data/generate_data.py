import random
import pandas as pd

monthly_bounds = [
    [4,	22,	-41, 59],
    [12, 29, -33, 64],
    [23, 41, -32, 83],
    [36, 57, 2, 95],
    [48, 70, 18, 106],
    [58, 79, 34, 104],
    [63, 83, 43, 108],
    [61, 80, 39, 103],
    [51, 71, 26, 104],
    [39, 58, 10, 90],
    [25, 40, -25, 77],
    [11, 26, -39, 68]
]


def create_temperature(bounds, delta=0):
    fahrenheit = random.gauss(
        mu=bounds[1] + delta,
        sigma=0.1 * (bounds[-1] - bounds[-2])
    )
    return int(round(5 / 9 * fahrenheit - 32))


def create_temperatures(bounds, deltas):
    return [create_temperature(bounds, delta) for delta in deltas]


def create_monthly_history(month_index: int) -> list:
    deltas = [-1, 2, -3, 0, 1, 1, 0, 2, -3, 2]
    bounds = monthly_bounds[month_index]

    return [
        {'year': 2015 - index, 'month': month_index + 1, 'temperature': temp}
        for index, temp in enumerate(create_temperatures(bounds, deltas))
    ]


def create_historical_temps():
    return pd.DataFrame([
        entry
        for month_index in range(12)
        for entry in create_monthly_history(month_index)
    ]).sort_values(by='year', ascending=True)


def create_current_temps():
    temps = [
        create_temperature(monthly_bounds[month_index], 3)
        for month_index in range(12)
    ]

    return pd.DataFrame([
        {'year': 2016, 'month': month_index + 1, 'temperature': temp}
        for month_index, temp in enumerate(temps)
    ])

create_historical_temps().to_csv('historical_temperatures.csv', index=False)
create_current_temps().to_csv('temperatures.csv', index=False)
