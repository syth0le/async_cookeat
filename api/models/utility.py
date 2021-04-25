from sqlalchemy import Table, Column, Integer, String

category = Table(
    'category',
    # metadata,
    Column('id', Integer, primary_key=True),  # creator_id
    Column('name', String, unique=True, nullable=False),
)
