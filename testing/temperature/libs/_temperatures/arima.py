import math
import typing
from collections import namedtuple

import pandas as pd
from statsmodels.tsa.arima_model import ARIMA

# A data structure to store ARIMA models
MODEL_DATA = namedtuple(
    'MODEL_DATA',
    ['p', 'd', 'q', 'model', 'results', 'rmse']
)


def run(
        df: pd.DataFrame,
        p: int,
        d: int,
        q: int
) -> typing.Union[MODEL_DATA, None]:
    """
    Runs an ARIMA model on the temperature data in the specified data frame
    with the specified p (AR), d (I) and q (MA) ordering and returns a
    MODEL_DATA instance with the results if the ARIMA found a solution or None
    if it failed.

    :param df:
        Source data frame
    :param p:
        AR order
    :param d:
        I order
    :param q:
        MA order
    :return:
        Model results if one was successfully fit
    """

    temperatures = df['temperature'].astype(float).values

    try:
        model = ARIMA(temperatures, dates=df['date'], order=(p, d, q))
        results = model.fit(disp=-1)
        fit_values = results.fittedvalues
        delta = len(temperatures) - len(fit_values)
        rss = sum((fit_values - temperatures[delta:]) ** 2)
        rmse = math.sqrt(rss) / len(temperatures)
        return MODEL_DATA(p, d, q, model, results, rmse)
    except Exception:
        return None
