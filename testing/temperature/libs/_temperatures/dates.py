from datetime import datetime

import pandas as pd


def create_order_column(df: pd.DataFrame) -> pd.Series:
    """
    Returns a column calculated from the month and year values in the
    source data frame. The order is determined as:

    order = 100 * (year + month / 12)

    such that the date: 6/2010 -> 201050

    :param df:
        Source data frame for which to calculate order values. Expects
        that the data frame has 'year' and 'month' columns
    :return:
        A new column with the order values for each row in the source
        data frame.
    """

    orders = 100 * (df['year'] + (df['month'] - 1) / 12)  # type: pd.Series
    return orders.round().astype(int)


def get_date(row: pd.Series) -> datetime:
    """
    Returns a datetime object for a given data frame row

    :param row:
        The row from which the date should be created.
    :return:
        A datetime value for the specified row.
    """

    return datetime(year=int(row['year']), month=int(row['month']), day=1)