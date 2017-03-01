import cauldron as cd
from sqlalchemy import create_engine
from sqlalchemy.pool import StaticPool

df_attributes = cd.shared.df_attributes
df_performance = cd.shared.df_performance

# Create an in-memory SQLite database and populate tables from data frames
# The extra arguments make it possible for the connection to function in a
# multi-threaded notebook environment.
engine = create_engine(
    'sqlite://',
    connect_args={'check_same_thread': False},
    poolclass=StaticPool
)

df_attributes.to_sql('attributes', engine)
df_performance.to_sql('performance', engine)

cd.display.markdown(
    """
    ## Create SQL In-Memory Database

    We load the data frames shown above into an in-memory SQLite database as
    tables for the raw SQL and SQLAlchemy comparisons. To confirm this works
    we execute two SQL statements:
    """
)


def execute_statement(statement):
    cd.display.code_block(statement, language_id='sql')

    results = engine.execute(statement)

    for r in results:
        print(r)


execute_statement('SELECT * FROM attributes LIMIT 5')
execute_statement('SELECT * FROM performance LIMIT 5')

cd.shared.sql_engine = engine
