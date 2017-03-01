import cauldron as cd
import pandas as pd
import sqlalchemy as sa

engine = cd.shared.sql_engine
attributes = cd.shared.attributes_table
performance = cd.shared.performance_table

high_power = (
    sa.sql.select([attributes])
    .where(attributes.c.hp > 200)
    .alias()
)

high_performance = (
    sa.sql.select([performance])
    .where(performance.c.mpg > 15)
    .alias()
)

join = high_power.join(
    high_performance,
    high_power.c.name == high_performance.c.name
)

cmd = (
    sa.sql
    .select([high_power, high_performance])
    .select_from(join)
    .reduce_columns()
    .limit(10)
)

cd.display.header('Advanced Join: SQLAlchemy', 2)

cd.display.code_block(
    """
    high_power = (
        select([attributes])
        .where(attributes.c.hp > 200)
        .alias()
    )

    high_performance = (
        select([performance])
        .where(performance.c.mpg > 15)
        .alias()
    )

    join = high_power.join(
        high_performance,
        high_power.c.name == high_performance.c.name
    )

    cmd = (
        select([high_power, high_performance])
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
