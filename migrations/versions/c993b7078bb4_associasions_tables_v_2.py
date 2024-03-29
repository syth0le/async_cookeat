"""associasions_tables_v.2

Revision ID: c993b7078bb4
Revises: e9c4149e8890
Create Date: 2021-05-07 23:01:34.824860

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'c993b7078bb4'
down_revision = 'e9c4149e8890'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('nutrition_to_recipe_a',
    sa.Column('ingredient_id', sa.Integer(), nullable=False),
    sa.Column('nutrition_id', sa.Integer(), nullable=False),
    sa.Column('extra_data', sa.String(length=50), nullable=True),
    sa.ForeignKeyConstraint(['ingredient_id'], ['ingredient.id'], ),
    sa.ForeignKeyConstraint(['nutrition_id'], ['nutrition.id'], ),
    sa.PrimaryKeyConstraint('ingredient_id', 'nutrition_id')
    )
    op.create_unique_constraint(None, 'equipment', ['name'])
    op.create_unique_constraint(None, 'ingredient', ['id'])
    op.add_column('recipe', sa.Column('created_date', sa.DateTime(timezone=True), nullable=True))
    op.drop_column('recipe', 'date')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('recipe', sa.Column('date', postgresql.TIMESTAMP(timezone=True), autoincrement=False, nullable=True))
    op.drop_column('recipe', 'created_date')
    op.drop_constraint(None, 'ingredient', type_='unique')
    op.drop_constraint(None, 'equipment', type_='unique')
    op.drop_table('nutrition_to_recipe_a')
    # ### end Alembic commands ###
