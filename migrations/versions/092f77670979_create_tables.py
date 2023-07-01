"""Create tables

Revision ID: 092f77670979
Revises: 
Create Date: 2023-06-30 06:34:25.973890

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '092f77670979'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('locations',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=150), nullable=True),
    sa.Column('parent_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['parent_id'], ['locations.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('resume_postings',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=255), nullable=False),
    sa.Column('content', sa.Text(), nullable=False),
    sa.Column('job_type', sa.Enum('FULLTIME', 'PARTTIME', 'CONTRACT', name='jobtypeenum'), nullable=True),
    sa.Column('nationality', sa.Enum('KOREA', 'CHINA', 'PHILIPPINES', 'VIETNAM', 'CAMBODIA', 'OTHER', 'UNKNOWN', name='countryenum'), nullable=True),
    sa.Column('visa', sa.String(length=50), nullable=True),
    sa.Column('contact', sa.String(length=50), nullable=False),
    sa.Column('views', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.Column('deleted_at', sa.DateTime(), nullable=True),
    sa.Column('is_deleted', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('job_postings',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=255), nullable=False),
    sa.Column('content', sa.Text(), nullable=False),
    sa.Column('category', sa.Enum('FOOD_SERVICE', 'SALE', 'MANUFACTURING', 'TRANSPORTATION', 'AGRICULTURE', 'EDUCATION', 'CONSTRUNCTION', 'OFFICE_WORK', 'CONSULTING', 'OTHER', name='jobcategoryenum'), nullable=False),
    sa.Column('location_id', sa.Integer(), nullable=False),
    sa.Column('salary', sa.JSON(), nullable=True),
    sa.Column('views', sa.Integer(), nullable=False),
    sa.Column('status', sa.Enum('PUBLISHED', 'DELETED', 'EXPIRED', name='jobpostingstatusenum'), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('renewaled_at', sa.DateTime(), nullable=False),
    sa.Column('deadline', sa.DateTime(timezone=True), nullable=True),
    sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('deleted_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['location_id'], ['locations.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('working_hours',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('day', sa.String(length=10), nullable=False),
    sa.Column('start_time', sa.String(length=10), nullable=False),
    sa.Column('end_time', sa.String(length=10), nullable=False),
    sa.Column('job_posting_id', sa.Integer(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['job_posting_id'], ['job_postings.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('working_hours')
    op.drop_table('job_postings')
    op.drop_table('resume_postings')
    op.drop_table('locations')
    # ### end Alembic commands ###
