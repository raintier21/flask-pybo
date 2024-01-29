"""empty message

Revision ID: 9257861f0e61
Revises: 402b0c5cf90f
Create Date: 2024-01-24 17:01:19.909933

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9257861f0e61'
down_revision = '402b0c5cf90f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=150), nullable=False),
    sa.Column('password', sa.String(length=200), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    # ### end Alembic commands ###
