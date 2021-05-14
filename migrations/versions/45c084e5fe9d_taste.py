"""taste

Revision ID: 45c084e5fe9d
Revises: 4798de992a71
Create Date: 2021-05-12 00:18:25.242548

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '45c084e5fe9d'
down_revision = '4798de992a71'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('recipe', sa.Column('bitterness', sa.Float(), nullable=True))
    op.add_column('recipe', sa.Column('fattiness', sa.Float(), nullable=True))
    op.add_column('recipe', sa.Column('saltiness', sa.Float(), nullable=True))
    op.add_column('recipe', sa.Column('savoriness', sa.Float(), nullable=True))
    op.add_column('recipe', sa.Column('sourness', sa.Float(), nullable=True))
    op.add_column('recipe', sa.Column('spiciness', sa.Float(), nullable=True))
    op.add_column('recipe', sa.Column('sweetness', sa.Float(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('recipe', 'sweetness')
    op.drop_column('recipe', 'spiciness')
    op.drop_column('recipe', 'sourness')
    op.drop_column('recipe', 'savoriness')
    op.drop_column('recipe', 'saltiness')
    op.drop_column('recipe', 'fattiness')
    op.drop_column('recipe', 'bitterness')
    # ### end Alembic commands ###