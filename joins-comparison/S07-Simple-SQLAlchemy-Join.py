import cauldron as cd
import pandas as pd
import sqlalchemy as sa

engine = cd.shared.sql_engine
attributes = cd.shared.attributes_table
performance = cd.shared.performance_table

join = attributes.join(performance, attributes.c.name == performance.c.name)
cmd = (
    sa.sql
    .select([attributes, performance])
    .select_from(join)
    .reduce_columns()
    .limit(10)
)

cd.display.header('Simple Join: SQLAlchemy', 2)

cd.display.code_block(
    """
    join = attributes.join(performance, attributes.c.name == performance.c.name)
    cmd = (
        select([attributes, performance])
        .select_from(join)
        .reduce_columns()
        .limit(10)
    )
    """,
    language_id='py'
)

results = engine.execute(cmd)
df = pd.DataFrame([
    {k: v for k, v in r.items()}
    for r in results.fetchall()
])

cd.display.table(df)
