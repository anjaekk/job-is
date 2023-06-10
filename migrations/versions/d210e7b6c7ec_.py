"""empty message

Revision ID: d210e7b6c7ec
Revises: 525cab12b24c
Create Date: 2023-06-10 09:48:31.798685

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'd210e7b6c7ec'
down_revision = '525cab12b24c'
branch_labels = None
depends_on = None


def upgrade():
    op.rename_table("job_seeker_postings", "resume_postings")


def downgrade():
    op.rename_table("resume_postings", "job_seeker_postings")