import cauldron as cd
import pandas as pd

# Load the CSV file from the project folder. Cauldron always sets the current
# directory to the project folder when loading a project making it easy to
# reference files relative to the root project folder.
df = pd.read_csv('autompg.csv')

# Start with some information about this step using markdown rendering with
# Jinja2 template variable substitution to print out the shape of the data
# frame containing the MPG dataset.
cd.display.markdown(
    """
    # Auto MPG Dataset

    The dataset was loaded from a CSV file stored in the notebook's project
    folder. It contains __{{ shape[0] }} rows__ and __{{ shape[1] }} columns__
    and is displayed in its entirety in the following table.
    """,
    shape=df.shape
)

# Display the dataset as a table in the notebook. The second argument of 0.4
# specified that we want the table height to be 40% the height of the notebook
# window.
cd.display.table(df, 0.4)

# Share the data frame with other steps in this notebook
cd.shared.df = df
