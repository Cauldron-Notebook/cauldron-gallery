import cauldron as cd
from matplotlib import pyplot

# Retrieve the data frame from the shared module where
# it was stored by a previous step
df = cd.shared.df

pyplot.clf()

# Create the Scatter object
pyplot.scatter(x=df['hp'], y=df['mpg'])

pyplot.title('Fuel Efficiency versus Horsepower')
pyplot.grid(True)
pyplot.gca().set_axisbelow(True)
pyplot.gca().grid(color='gray', linestyle='dashed')

pyplot.gca().set_xlabel('Horsepower')
pyplot.gca().set_ylabel('Miles Per Gallon')

# Add the scatter plot to the display
cd.display.pyplot(aspect_ratio=(12, 6))


def create_scatter_plot(shared_axis, origin: int):
    """
    Returns a Scatter plot for data that has the specified region of origin

    :param origin:
        The region of origin (1, 2 or 3) for which to create a Scatter plot
    :return:
        The Scatter plot object for that region
    """
    df_slice = df.query('origin == {}'.format(origin))
    return shared_axis.scatter(x=df_slice['hp'], y=df_slice['mpg'])

# Create a list of Scatter plots for each region
axis = pyplot.subplot(111)

origins = df['origin'].unique()
traces = [create_scatter_plot(axis, origin) for origin in origins]
axis.legend(traces, origins)

pyplot.title('Fuel Efficiency versus Horsepower (Colorized)')
axis.grid(True)
axis.set_axisbelow(True)
axis.grid(color='gray', linestyle='dashed')

axis.set_xlabel('Horsepower')
axis.set_ylabel('Miles Per Gallon')

cd.display.pyplot(aspect_ratio=(12, 6))
