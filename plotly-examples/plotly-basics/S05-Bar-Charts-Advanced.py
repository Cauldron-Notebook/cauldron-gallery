import cauldron as cd
import pandas as pd
import plotly.graph_objs as go

# Retrieve shared variables for use in this step
df = cd.shared.df  # type: pd.DataFrame
get_cylinder_histogram_data = cd.shared.get_cylinder_histogram_data


def create_origin_histogram(origin: int) -> dict:
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

    return go.Bar(
        x=origin_hist_data[0],
        y=origin_hist_data[1],
        name=origin
    )

# Create a list of the bar charts by origin and add them to the notebook as a
# single plot
cd.display.plotly(
    data=[create_origin_histogram(origin) for origin in df['origin'].unique()],
    layout=go.Layout(
        title='Distribution of Cylinders (Grouped by Region of Origin)',
        barmode='group',
        bargap=0.1,
        bargroupgap=0.1
    )
)
