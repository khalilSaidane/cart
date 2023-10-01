"""test

Revision ID: 428cf2735563
Revises: 7237f3b14847
Create Date: 2023-10-01 12:09:24.472957

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '428cf2735563'
down_revision = '7237f3b14847'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('carts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('creation_date', sa.DateTime(), nullable=False),
    sa.Column('status', sa.Enum('OPEN', 'CHECKOUT', 'CLOSED', 'REMOVED', name='cartstatus'), nullable=False),
    sa.Column('last_updated_at', sa.DateTime(), nullable=True),
    sa.Column('test_column', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('cart_items',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('cart_id', sa.Integer(), nullable=False),
    sa.Column('product_id', sa.Integer(), nullable=False),
    sa.Column('quantity', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['cart_id'], ['carts.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('cart_items')
    op.drop_table('carts')
    # ### end Alembic commands ###