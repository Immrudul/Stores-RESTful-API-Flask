"""empty message

Revision ID: 59a53b0bc88c
Revises: 44758fe0b65f
Create Date: 2024-05-13 22:09:09.583441

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '59a53b0bc88c'
down_revision = '44758fe0b65f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('items', sa.Column('description', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('items', 'description')
    # ### end Alembic commands ###
