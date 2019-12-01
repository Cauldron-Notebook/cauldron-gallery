import cauldron as cd
import pandas as pd
import plotly.graph_objs as go


# Retrieve the Auto MPG dataset's data frame from Cauldron's shared variables
# where it was placed by a previous step.
df = cd.shared.df


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

# Create bar chart with calculated histogram data
hist_data = get_cylinder_histogram_data(df)
bar = go.Bar(x=hist_data[0], y=hist_data[1])

# Add the bar chart to the notebook
cd.display.plotly(
    bar,
    go.Layout(
        title='Distribution of Cylinders'
    )
)

cd.display.text(
    """
    Plotly also has a built-in Histogram chart type, which we can use to
    easily create a histogram without having to do the histogram calculations
    manually. It produces a very similar output to the manually created version
    using Plotly's Bar chart.
    """
)

# Add a version using Plotly's Histogram chart type
cd.display.plotly(
    go.Histogram(x=df['cyl']),
    go.Layout(
        title='Distribution of Cylinders',
        bargap=0.1
    )
)

# Share the get_cylinder_histogram_data function so that it can be used in
# other steps
cd.shared.get_cylinder_histogram_data = get_cylinder_histogram_data
