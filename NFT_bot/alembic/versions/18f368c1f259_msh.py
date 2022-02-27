"""msh

Revision ID: 18f368c1f259
Revises: 9172e3560a5f
Create Date: 2022-02-27 20:16:50.628365

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '18f368c1f259'
down_revision = '9172e3560a5f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('collection', 'count',
               existing_type=sa.REAL(),
               nullable=False)
    op.add_column('history_collection', sa.Column('response_json', postgresql_json.JSON(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('history_collection', 'response_json')
    op.alter_column('collection', 'count',
               existing_type=sa.REAL(),
               nullable=True)
    # ### end Alembic commands ###