import cauldron as cd
from cauldron.steptest import StepTestCase
import pandas as pd
import numpy as np


class TestNotebook(StepTestCase):
    """ Test class containing step unit tests for the notebook """

    def test_missing_values(self):
        """ should not have NaN values in the total column """

        # Assign to the shared df variable a fictional data frame with only
        # a single row and the part_one column value will is missing
        cd.shared.df = pd.DataFrame(dict(
            part_one=[None],
            part_two=[12]
        ))

        # Run the step
        self.run_step('S02-Create-Total.py')

        # Retrieve the modified data frame from the shared variables
        df = cd.shared.df

        # Confirm that the total column value is not NaN
        self.assertFalse(np.isnan(df['total'].values[0]))
