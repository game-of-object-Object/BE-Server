"""empty message

Revision ID: 5ce9a277b3ef
Revises: 
Create Date: 2020-04-28 18:27:57.175850

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5ce9a277b3ef'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('NPC',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=20), nullable=True),
    sa.Column('description', sa.String(length=1024), nullable=True),
    sa.Column('items', sa.String(length=1024), nullable=True),
    sa.Column('gold', sa.Integer(), nullable=True),
    sa.Column('HP', sa.Integer(), nullable=True),
    sa.Column('isHostile', sa.Boolean(), nullable=True),
    sa.Column('attack', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('merchant',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=20), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('room',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=20), nullable=True),
    sa.Column('description', sa.String(length=1024), nullable=True),
    sa.Column('items', sa.String(length=1024), nullable=True),
    sa.Column('NPCs', sa.String(length=1024), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('title')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=100), nullable=True),
    sa.Column('password', sa.String(length=100), nullable=True),
    sa.Column('character_name', sa.String(length=100), nullable=True),
    sa.Column('character_type', sa.String(length=100), nullable=True),
    sa.Column('portrait', sa.String(length=1024), nullable=True),
    sa.Column('HP', sa.Integer(), nullable=True),
    sa.Column('MP', sa.Integer(), nullable=True),
    sa.Column('attack', sa.Integer(), nullable=True),
    sa.Column('gold', sa.Integer(), nullable=True),
    sa.Column('encounter_cd', sa.Integer(), nullable=True),
    sa.Column('current_room', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('username')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    op.drop_table('room')
    op.drop_table('merchant')
    op.drop_table('NPC')
    # ### end Alembic commands ###
