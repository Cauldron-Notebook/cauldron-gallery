import cauldron as cd
import pandas as pd

# Retrieve the stored data DataFrame.
df: pd.DataFrame = cd.shared.df

df['total'] = df['part_one'].fillna(0) + df['part_two'].fillna(0)

# Show the DataFrame in the display.
cd.display.table(df)

# Share the updated data frame.
cd.shared.df = df
