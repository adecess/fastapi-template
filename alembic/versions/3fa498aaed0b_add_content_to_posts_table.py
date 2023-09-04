"""add content to posts table

Revision ID: 3fa498aaed0b
Revises: 2007fb74cb92
Create Date: 2023-08-26 15:42:57.223868

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3fa498aaed0b'
down_revision: Union[str, None] = '2007fb74cb92'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
