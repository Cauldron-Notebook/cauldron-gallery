import cauldron as cd
from cauldron import steptest
import pandas as pd
import numpy as np

test_fixture = steptest.create_test_fixture(__file__)


def test_missing_values(tester: steptest.CauldronTest):
    """ should not have NaN values in the total column """

    # Assign to the shared df variable a fictional data frame with only
    # a single row and the part_one column value will is missing
    cd.shared.df = pd.DataFrame(dict(
        part_one=[None],
        part_two=[12]
    ))

    # Run the step
    tester.run_step('S02-Create-Total.py')

    # Retrieve the modified data frame from the shared variables
    df = cd.shared.df

    # Confirm that the total column value is not NaN
    assert not np.isnan(df['total'].values[0])
