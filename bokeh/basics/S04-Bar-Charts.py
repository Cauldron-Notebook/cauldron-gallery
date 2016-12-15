import cauldron as cd
from bokeh.charts import Bar

# Retrieve the Auto MPG dataset's data frame from Cauldron's shared variables
# where it was placed by a previous step.
df = cd.shared.df

# Create bar chart from data frame
bar = Bar(df, label='cyl', title='Distribution of Cylinders')

# Add the bar chart to the notebook
cd.display.bokeh(bar)

# Create more advanced bar chart that groups data by region
bar_regional = Bar(
    data=df,
    label='cyl',
    values='displ',
    agg='mean',
    group='origin',
    title="Distribution of Cylinders (Grouped by Region of Origin)",
    legend='top_right'
)

# Add the bar chart to the notebook
cd.display.bokeh(bar_regional)
