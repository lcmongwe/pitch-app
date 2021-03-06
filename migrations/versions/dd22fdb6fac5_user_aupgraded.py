"""user aupgraded

Revision ID: dd22fdb6fac5
Revises: 318549c3dc0d
Create Date: 2022-05-10 14:19:54.431084

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dd22fdb6fac5'
down_revision = '318549c3dc0d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('id1', sa.Integer(), nullable=False))
    op.add_column('user', sa.Column('email1', sa.String(length=255), nullable=True))
    op.add_column('user', sa.Column('pass_secure1', sa.String(length=255), nullable=True))
    op.add_column('user', sa.Column('username1', sa.String(length=255), nullable=True))
    op.create_unique_constraint(None, 'user', ['email1'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'user', type_='unique')
    op.drop_column('user', 'username1')
    op.drop_column('user', 'pass_secure1')
    op.drop_column('user', 'email1')
    op.drop_column('user', 'id1')
    # ### end Alembic commands ###
