import cauldron as cd
import pandas as pd
import numpy as np
from matplotlib import pyplot

# Retrieve shared variables for use in this step
df: pd.DataFrame = cd.shared.df
get_cylinder_histogram_data = cd.shared.get_cylinder_histogram_data

pyplot.clf()
axis = pyplot.subplot(111)

BAR_SPACING = 0.2


def create_origin_histogram(origin: int, offset: float):
    """
    This function calculates the histogram values for the specified
    column of data and returns a Plotly bar chart object for that data

    :param origin:
        The region of origin (1, 2 or 3) on which to create the histogram
    :return:
        A Plotly bar chart object to be added to the display
    """
    df_slice = df.query('origin == {}'.format(origin))
    origin_hist_data = get_cylinder_histogram_data(df_slice)

    return axis.bar(
        x=np.array(origin_hist_data[0]) - BAR_SPACING * offset,
        height=origin_hist_data[1],
        width=0.9 * BAR_SPACING
    )

# Create a list of the bar charts by origin and add them to the notebook as a
# single plot
regions = df['origin'].unique()
offsets = [i - 0.5 * len(regions) for i in range(len(regions))]
traces = [
    create_origin_histogram(origin, offsets[i])
    for i, origin in enumerate(regions)
]
    

pyplot.title('Distribution of Cylinders (Grouped by Region of Origin)')
pyplot.grid(True)
axis.set_axisbelow(True)
axis.grid(color='gray', linestyle='dashed')
axis.legend(traces, regions)

cd.display.pyplot(aspect_ratio=(12, 6))
