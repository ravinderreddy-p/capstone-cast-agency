"""empty message

Revision ID: 674036d6e7cc
Revises: 
Create Date: 2020-03-14 11:14:37.997966

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, us
revision = '674036d6e7cc'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('actors')
    op.drop_table('movies')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('movies',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('release_date', sa.DATE(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='movies_pkey')
    )
    op.create_table('actors',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('age', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('gender', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='actors_pkey')
    )
    # ### end Alembic commands ###
