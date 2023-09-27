"""initial migration

Revision ID: a9830c39cb90
Revises: 
Create Date: 2023-09-27 16:47:03.845179

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a9830c39cb90'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('order',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('status', sa.String(), nullable=False),
    sa.Column('created', sa.DateTime(), nullable=True),
    sa.Column('schedule_id', sa.String(), nullable=True),
    sa.Column('delivery_id', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_order'))
    )
    op.create_table('order_item',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('order_id', sa.String(), nullable=True),
    sa.Column('product', sa.String(), nullable=False),
    sa.Column('size', sa.String(), nullable=False),
    sa.Column('quantity', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['order_id'], ['order.id'], name=op.f('fk_order_item_order_id_order')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_order_item'))
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('order_item')
    op.drop_table('order')
    # ### end Alembic commands ###
