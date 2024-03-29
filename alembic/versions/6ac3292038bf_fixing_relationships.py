"""Fixing relationships

Revision ID: 6ac3292038bf
Revises: ff9dedcec1a4
Create Date: 2022-02-28 02:00:40.008538

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6ac3292038bf'
down_revision = 'ff9dedcec1a4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('history', sa.Column('collection_id', sa.Integer(), nullable=True))
    op.drop_constraint('history_collection_fkey', 'history', type_='foreignkey')
    op.create_foreign_key(None, 'history', 'collection', ['collection_id'], ['id'])
    op.drop_column('history', 'collection')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('history', sa.Column('collection', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'history', type_='foreignkey')
    op.create_foreign_key('history_collection_fkey', 'history', 'collection', ['collection'], ['id'])
    op.drop_column('history', 'collection_id')
    # ### end Alembic commands ###
