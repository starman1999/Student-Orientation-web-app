"""empty message

Revision ID: 4e72f7bf0cc8
Revises: 5c6e30dce8f6
Create Date: 2021-06-24 18:20:41.270608

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4e72f7bf0cc8'
down_revision = '5c6e30dce8f6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('moyenne',
    sa.Column('etudiant_id', sa.Integer(), nullable=False),
    sa.Column('module_id', sa.Integer(), nullable=False),
    sa.Column('moyenne', sa.Float(), nullable=True),
    sa.ForeignKeyConstraint(['etudiant_id'], ['etudiants.id'], ),
    sa.ForeignKeyConstraint(['module_id'], ['modules.id'], ),
    sa.PrimaryKeyConstraint('etudiant_id', 'module_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('moyenne')
    # ### end Alembic commands ###
