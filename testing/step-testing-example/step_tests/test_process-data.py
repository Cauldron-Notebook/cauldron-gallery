import cauldron as cd
from cauldron.steptest import StepTestCase
import pandas as pd


class TestProcessData(StepTestCase):
    """ Class for testing the process data step """

    def test_empty_df(self):
        """ should not fail when a data frame is empty """

        # Manually assign data frames, which would normally be loaded in
        # the first step. Assign a single empty data frame for this test.
        cd.shared.sensors = [pd.DataFrame([])]
        cd.shared.df_aerial = pd.read_csv('data/aerial.csv')

        # Run the step using the run_step test method
        result = self.run_step('S04-Process-Data.py')

        # Confirm that the step ran successfully without error
        self.assertTrue(result.success)

    def test_identical_temps(self):
        """ should have zero lag if temperature curves are identical """

        # Manually assign the aerial temperature sensor data
        cd.shared.df_aerial = pd.read_csv('data/aerial.csv')

        # Use the same aerial temperature sensor data as a ground-level sensor
        # but add a fake sensor_index column as needed by ground-level sensor
        # data frames
        df_sensor = pd.read_csv('data/aerial.csv')
        df_sensor['sensor_index'] = 0
        cd.shared.sensors = [df_sensor]

        # Run the step using the run_step test method
        result = self.run_step('S04-Process-Data.py')

        # Confirm that the step ran successfully without error
        self.assertTrue(result.success)

        # Retrieve the results data frame now that the step has run
        df_results = cd.shared.df_results

        # The results data frame should have exactly one entry because that is
        # the number of sensor data frames we supplied in this test
        self.assertEqual(len(df_results), 1)

        # The lag should be zero because the ground sensor data is identical
        # to the aerial sensor data
        self.assertEqual(df_results.iloc[0]['lag'], 0)
