"""empty message

Revision ID: 5310d132f1be
Revises: b2f302e7dae6
Create Date: 2024-08-26 13:06:30.496918

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5310d132f1be'
down_revision = 'b2f302e7dae6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('about_author', sa.Text(length=500), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_column('about_author')

    # ### end Alembic commands ###
