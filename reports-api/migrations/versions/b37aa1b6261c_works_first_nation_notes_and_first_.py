"""works-first_nation_notes and first_nations-pin and pip_link

Revision ID: b37aa1b6261c
Revises: 7b4040c1af9a
Create Date: 2023-10-06 11:13:47.040610

"""
from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils


# revision identifiers, used by Alembic.
revision = 'b37aa1b6261c'
down_revision = '7b4040c1af9a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('indigenous_nations', sa.Column('pip_link', sqlalchemy_utils.types.url.URLType(), nullable=True))
    op.add_column('indigenous_nations', sa.Column('pin', sa.String(length=100), nullable=True))
    op.add_column('indigenous_nations_history', sa.Column('pip_link', sqlalchemy_utils.types.url.URLType(), autoincrement=False, nullable=True))
    op.add_column('indigenous_nations_history', sa.Column('pin', sa.String(length=100), autoincrement=False, nullable=True))
    op.add_column('works', sa.Column('first_nation_notes', sa.String(), nullable=True))
    op.add_column('works_history', sa.Column('first_nation_notes', sa.String(), autoincrement=False, nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('works_history', 'first_nation_notes')
    op.drop_column('works', 'first_nation_notes')
    op.drop_column('indigenous_nations_history', 'pin')
    op.drop_column('indigenous_nations_history', 'pip_link')
    op.drop_column('indigenous_nations', 'pin')
    op.drop_column('indigenous_nations', 'pip_link')
    # ### end Alembic commands ###