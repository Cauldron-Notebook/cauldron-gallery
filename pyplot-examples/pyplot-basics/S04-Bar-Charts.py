import cauldron as cd
import pandas as pd
from matplotlib import pyplot


# Retrieve the Auto MPG dataset's data frame from Cauldron's shared variables
# where it was placed by a previous step.
df: pd.DataFrame = cd.shared.df


def get_cylinder_histogram_data(data_frame: pd.DataFrame):
    """
    Returns the counts for each cylinder value

    :param data_frame:
        The source data frame on which to calculate cylinder counts
    :return:
        A list containing the cylinder counts for each cylinder value
    """
    cylinder_values = list(df['cyl'].unique())
    cylinder_counts = [
        data_frame
            .query('cyl == {}'.format(cylinder))
            .shape[0]
        for cylinder in cylinder_values
    ]

    return cylinder_values, cylinder_counts

# Clear all existing figures first so nothing created historically
# will interfere with the current plotting operations.
pyplot.clf()

# Create bar chart with calculated histogram data
hist_data = get_cylinder_histogram_data(df)

bar = pyplot.bar(x=hist_data[0], height=hist_data[1])
pyplot.title('Distribution of Cylinders')
pyplot.grid(True)
pyplot.gca().set_axisbelow(True)
pyplot.gca().grid(color='gray', linestyle='dashed')

# Add the bar chart to the notebook
cd.display.pyplot(aspect_ratio=(12, 6))

cd.display.text(
    """
    PyPlot also has a built-in Histogram chart type, which we can use to
    easily create a histogram without having to do the histogram calculations
    manually. It produces a very similar output to the manually created version
    using PyPlot's Bar chart.
    """
)

# Add a version using PyPlot's Histogram chart type
pyplot.hist(df['cyl'], align='left')
pyplot.title('Distribution of Cylinders')
pyplot.grid(True)
pyplot.gca().set_axisbelow(True)
pyplot.gca().grid(color='gray', linestyle='dashed')

cd.display.pyplot(aspect_ratio=(12, 6))

# Share the get_cylinder_histogram_data function so that it can be used in
# other steps
cd.shared.get_cylinder_histogram_data = get_cylinder_histogram_data
