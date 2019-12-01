import cauldron as cd
import pandas as pd

# Load the CSV data into a DataFrame.
df: pd.DataFrame = pd.read_csv('data.csv')

# Show the DataFrame in the display.
cd.display.table(df)

# Store the DataFrame in shared variables for other steps
# to access.
cd.shared.df = df
