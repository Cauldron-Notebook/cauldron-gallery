import cauldron as cd
import plotly.graph_objs as go

# Retrieve the data frame from the shared module where
# it was stored by a previous step
df = cd.shared.df

# Create the Scatter object
scatter = go.Scatter(
    x=df['hp'],
    y=df['mpg'],
    mode='markers'
)

# Create the layout object for the plot
scatter_layout = go.Layout(
    title='Fuel Efficiency versus Horsepower',
    xaxis=go.XAxis(title='Horsepower'),
    yaxis=go.YAxis(title='Miles Per Gallon')
)

# Add the scatter plot to the display
cd.display.plotly(scatter, scatter_layout)


def create_scatter_plot(origin: int):
    """
    Returns a Scatter plot for data that has the specified region of origin

    :param origin:
        The region of origin (1, 2 or 3) for which to create a Scatter plot
    :return:
        The Scatter plot object for that region
    """

    df_slice = df.query('origin == {}'.format(origin))

    return go.Scatter(
        x=df_slice['hp'],
        y=df_slice['mpg'],
        mode='markers',
        name=origin
    )

# Create a list of Scatter plots for each region
scatters = [
    create_scatter_plot(origin)
    for origin in df['origin'].unique()
]

# Add the scatter plots together as a single Plotly plot
cd.display.plotly(
    scatters,
    go.Layout(
        title='Fuel Efficiency versus Horsepower (Colorized)',
        xaxis=go.XAxis(title='Horsepower'),
        yaxis=go.YAxis(title='Miles Per Gallon')
    )
)
