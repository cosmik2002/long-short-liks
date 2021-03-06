"""rename columns1

Revision ID: b17990f7bb0d
Revises: 3a36c9367b4c
Create Date: 2020-11-01 09:16:43.130175

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b17990f7bb0d'
down_revision = '3a36c9367b4c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('links', sa.Column('long_url', sa.String(length=200), nullable=True))
    op.drop_column('links', 'long_link')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('links', sa.Column('long_link', sa.VARCHAR(length=200), autoincrement=False, nullable=True))
    op.drop_column('links', 'long_url')
    # ### end Alembic commands ###
