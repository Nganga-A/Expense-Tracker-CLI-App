"""alter column date data type in expenses and add column hashed password in users

Revision ID: 10ff95032519
Revises: 8f3852ba9aa2
Create Date: 2023-09-07 04:00:31.822455

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy import text, Table, MetaData,Column, Integer, Date, Text, Float
from sqlalchemy.engine.reflection import Inspector

# revision identifiers, used by Alembic.
revision: str = '10ff95032519'
down_revision: Union[str, None] = '8f3852ba9aa2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    conn = op.get_bind()
    
    # Create a Table object for the 'temp_expenses' table
    metadata = MetaData()
    temp_expenses = Table(
        'temp_expenses', metadata,
        Column('id', Integer, primary_key=True),
        Column('date', Date),
        Column('description', Text),
        Column('amount', Float)
    )

    inspector = Inspector.from_engine(conn)

    if 'temp_expenses' not in inspector.get_table_names():
        # The table doesn't exist, so create it
        stmt = text("""
            CREATE TABLE temp_expenses (
                id INTEGER PRIMARY KEY,
                date DATE,
                description TEXT,
                amount REAL
            )
        """)
        
        conn.execute(stmt)
    
        # Copy data from the original table to the temporary table
        conn.execute("INSERT INTO temp_expenses SELECT * FROM expenses")

        # Drop the original table
        conn.execute("DROP TABLE expenses")

        # Rename the temporary table to the original table name
        conn.execute("ALTER TABLE temp_expenses RENAME TO expenses")



def downgrade() -> None:
    # No automated downgrade provided, handle manually if necessary
    pass
