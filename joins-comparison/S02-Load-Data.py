import cauldron as cd
import pandas as pd

# Load the auto-mpg data set
df = pd.read_csv('auto-mpg.csv')


# Break the data set into two separate data frames, one for attributes and
# one for performance
df_attributes = df[['name', 'cyl', 'displ', 'hp', 'weight', 'yr', 'origin']]
df_performance = df[['name', 'mpg', 'accel']]

cd.display.markdown(
    """
    ## Auto MPG Data Set

    We load the AutoMPG data set from CSV using pandas and then break the
    complete table into separate **attributes** and **performance** data
    frames.
    """
)

cd.display.markdown('The **attributes** table looks like:')
cd.display.table(df_attributes.head())

cd.display.markdown('The **performance** table looks like:')
cd.display.table(df_performance.head())

# Share two data frames
cd.shared.df_attributes = df_attributes
cd.shared.df_performance = df_performance
