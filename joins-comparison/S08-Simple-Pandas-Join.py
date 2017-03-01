import cauldron as cd
import pandas as pd

df_attributes = cd.shared.df_attributes
df_performance = cd.shared.df_performance

cd.display.header('Simple Join: Pandas')

cd.display.code_block(
    'pd.merge(df_attributes, df_performance, on=\'name\').head(10)',
    language_id='py'
)

df = pd.merge(df_attributes, df_performance, on='name').head(10)
cd.display.table(df)
