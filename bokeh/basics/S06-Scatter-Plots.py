import cauldron as cd
from bokeh.charts import Scatter

# Retrieve the data frame from the shared module where
# it was stored by a previous step
df = cd.shared.df

scatter = Scatter(
    data=df,
    x='hp',
    y='mpg',
    title='Fuel Efficiency versus Horsepower',
    xlabel='Horsepower',
    ylabel='Miles Per Gallon',
    legend='top_right'
)

cd.display.bokeh(scatter)


scatter_colored = Scatter(
    data=df,
    x='hp',
    y='mpg',
    color='origin',
    marker='cyl',
    title='Fuel Efficiency versus Horsepower (Colorized)',
    xlabel='Horsepower',
    ylabel='Miles Per Gallon',
    legend='top_right'
)

cd.display.bokeh(scatter_colored)
