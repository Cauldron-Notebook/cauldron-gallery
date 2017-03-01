import cauldron as cd
import sqlalchemy as sa

engine = cd.shared.sql_engine
catalog = sa.MetaData()

attributes = sa.Table(
    'attributes',
    catalog,
    sa.Column('name', sa.String),
    sa.Column('cyl', sa.Integer),
    sa.Column('displ', sa.Integer),
    sa.Column('weight', sa.Integer),
    sa.Column('hp', sa.Integer),
    sa.Column('yr', sa.Integer),
    sa.Column('origin', sa.Integer)
)

performance = sa.Table(
    'performance',
    catalog,
    sa.Column('name', sa.String),
    sa.Column('mpg', sa.Integer),
    sa.Column('accel', sa.Float)
)

cd.display.markdown(
    """
    # Create Table Definitions

    Now that we have a functioning database, we want to take advantage of
    sqlalchemy's Expression Language, which allows us to write more concise
    and readable queries. However, for that to work, we need to create
    definitions for the **attributes** and **performance** tables like so:
    """
)

cd.display.code_block(
    """
    import sqlalchemy as sa

    catalog = sa.MetaData()

    # Create attributes table definition. Not all columns need to be defined.
    # Only the ones you are interested in using should be included.
    attributes = sa.Table(
        'attributes',
        catalog,
        sa.Column('name', sa.String),
        sa.Column('cyl', sa.Integer),
        sa.Column('displ', sa.Integer),
        sa.Column('weight', sa.Integer),
        sa.Column('hp', sa.Integer),
        sa.Column('yr', sa.Integer),
        sa.Column('origin', sa.Integer)
    )
    """
)

cd.display.markdown(
    """
    We can then carry out the same queries as we did in the previous step,
    but this time using the SQLAlchemy Expression Language syntax instead
    of raw SQL:
    """
)

def execute_statement(table):
    cmd = (sa.sql
        .select([attributes])
        .limit(5)
    )

    cmd_string = 'select([{}]).limit(5)'.format(table.name)
    cd.display.code_block(cmd_string, language_id='py')

    results = engine.execute(cmd)
    for r in results:
        print(r)


execute_statement(attributes)
execute_statement(performance)


cd.shared.put(
    database_catalog=catalog,
    attributes_table=attributes,
    performance_table=performance
)
