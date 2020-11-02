"""rename columns

Revision ID: 3a36c9367b4c
Revises: a808aa7b6bc4
Create Date: 2020-11-01 09:08:24.120809

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3a36c9367b4c'
down_revision = 'a808aa7b6bc4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('links', sa.Column('long_link', sa.String(length=200), nullable=True))
    op.add_column('links', sa.Column('short_postfix', sa.String(length=50), nullable=True))
    op.drop_constraint('links_short_key', 'links', type_='unique')
    op.drop_column('links', 'short')
    op.drop_column('links', 'long')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('links', sa.Column('long', sa.VARCHAR(length=200), autoincrement=False, nullable=True))
    op.add_column('links', sa.Column('short', sa.VARCHAR(length=50), autoincrement=False, nullable=True))
    op.create_unique_constraint('links_short_key', 'links', ['short'])
    op.drop_column('links', 'short_postfix')
    op.drop_column('links', 'long_link')
    # ### end Alembic commands ###
