from sqlalchemy import Table, Column, Integer, String

creators = Table(
    'creators',
    # metadata,
    Column('id', Integer, primary_key=True),  # creator_id
    Column('name', String, unique=True, nullable=False),
    Column('photo', String, unique=True, nullable=False),
    Column('description', String, unique=True, nullable=False)
)
