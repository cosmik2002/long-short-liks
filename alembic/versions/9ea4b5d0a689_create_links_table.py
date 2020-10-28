"""create links table

Revision ID: 9ea4b5d0a689
Revises: 
Create Date: 2020-10-28 09:41:48.682224

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9ea4b5d0a689'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'links',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('short', sa.Unicode(50), nullable=False),
        sa.Column('long', sa.Unicode(200)),
        sa.Column('count', sa.Integer),
    )
    pass


def downgrade():
    op.drop_table('account')
    pass
