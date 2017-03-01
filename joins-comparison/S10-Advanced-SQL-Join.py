import cauldron as cd
import pandas as pd

engine = cd.shared.sql_engine

cmd = (
    """
    SELECT *
    FROM (
        SELECT *
        FROM attributes
        WHERE attributes.hp > 200
    ) AS high_power
    INNER JOIN (
        SELECT *
        FROM performance
        WHERE performance.mpg > 15
    ) AS high_performance
    ON high_power.name = high_performance.name
    LIMIT 10
    """
)

cd.display.header('Advanced Join: SQL', 2)

cd.display.code_block(cmd, language_id='sql')

results = engine.execute(cmd)
df = pd.DataFrame([
    {k: v for k, v in r.items()}
    for r in results.fetchall()
])

cd.display.table(df)
