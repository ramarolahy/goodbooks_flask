"""empty message

Revision ID: 31bd41e3de92
Revises: 8c146bd32c10
Create Date: 2019-03-04 10:49:49.251711

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '31bd41e3de92'
down_revision = '8c146bd32c10'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_books_author', table_name='books')
    op.drop_index('ix_books_isbn', table_name='books')
    op.drop_index('ix_books_title', table_name='books')
    op.create_unique_constraint(None, 'books', ['isbn'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'books', type_='unique')
    op.create_index('ix_books_title', 'books', ['title'], unique=False)
    op.create_index('ix_books_isbn', 'books', ['isbn'], unique=True)
    op.create_index('ix_books_author', 'books', ['author'], unique=False)
    # ### end Alembic commands ###
