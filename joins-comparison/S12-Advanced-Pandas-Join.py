import cauldron as cd
import pandas as pd

df_attributes = cd.shared.df_attributes
df_performance = cd.shared.df_performance

cd.display.header('Advanced Join: Pandas')

cd.display.code_block(
    """
    df = pd.merge(
        df_attributes[df_attributes.hp > 200],
        df_performance[df_performance.mpg > 20],
        on='name'
    ).head(10)
    """,
    language_id='py'
)

df = pd.merge(
    df_attributes[df_attributes.hp > 200],
    df_performance[df_performance.mpg > 15],
    on='name'
).head(10)
cd.display.table(df)
