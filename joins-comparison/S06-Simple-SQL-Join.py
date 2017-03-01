import cauldron as cd
import pandas as pd

engine = cd.shared.sql_engine

cmd = (
    """
    SELECT * FROM attributes
    INNER JOIN performance
    ON attributes.name = performance.name
    LIMIT 10
    """
)

cd.display.header('Simple Join: SQL', 2)

cd.display.code_block(cmd, language_id='sql')

results = engine.execute(cmd)
df = pd.DataFrame([
    {k: v for k, v in r.items()}
    for r in results.fetchall()
])

cd.display.table(df)
