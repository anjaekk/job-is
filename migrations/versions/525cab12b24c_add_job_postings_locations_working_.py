"""Add job_postings, locations, working_hours, and job_seeker_postings tables

Revision ID: 525cab12b24c
Revises: 
Create Date: 2023-06-08 03:23:24.087401

"""
from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime, Boolean, Enum
from sqlalchemy.orm import relationship
from alembic import op
import sqlalchemy as sa
from datetime import datetime

# revision identifiers, used by Alembic.
revision = '525cab12b24c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "job_postings",
        Column("id", Integer(), nullable=False),
        Column("title", String(length=256), nullable=False),
        Column("content", Text(), nullable=False),
        Column("location_id", Integer(), nullable=False),
        Column("salary_month", Integer(), nullable=True),
        Column("salary_year", Integer(), nullable=True),
        Column("views", Integer(), nullable=False, default=0),
        Column("created_at", DateTime(), nullable=False, default=datetime.now),
        Column("updated_at", DateTime(), nullable=False, default=datetime.now),
        Column("deleted_at", DateTime(), nullable=True),
        Column("is_deleted", Boolean(), nullable=False, default=False),
        sa.PrimaryKeyConstraint("id"),
    )

    op.create_table(
        "locations",
        Column("id", Integer(), nullable=False),
        Column("name", String(length=150), nullable=True),
        Column("parent_id", Integer(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
        sa.ForeignKeyConstraint(["parent_id"], ["locations.id"], name="fk_location_parent"),
    )

    op.create_table(
        "working_hours",
        Column("id", Integer(), nullable=False),
        Column("day", String(length=10), nullable=False),
        Column("start_time", String(length=10), nullable=False),
        Column("end_time", String(length=10), nullable=False),
        Column("job_posting_id", Integer(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
        sa.ForeignKeyConstraint(
            ["job_posting_id"], ["job_postings.id"], name="fk_working_hours_job_posting"
        ),
        Column("created_at", DateTime(), nullable=False, default=datetime.now),
        Column("updated_at", DateTime(), nullable=False, default=datetime.now),
    )

    op.create_table(
        "job_seeker_postings",
        Column("id", Integer(), nullable=False),
        Column("title", String(length=256), nullable=False),
        Column("content", Text(), nullable=False),
        Column("job_type", String(length=10), nullable=False),
        Column("nationality", Enum("한국", "중국", "필리핀", "베트남", "캄보디아", "기타"), nullable=True),
        Column("visa", String(length=50), nullable=True),
        Column("contract", String(length=50), nullable=False),
        Column("views", Integer(), nullable=False, default=0),
        Column("created_at", DateTime(), nullable=False, default=datetime.now),
        Column("updated_at", DateTime(), nullable=False, default=datetime.now),
        Column("deleted_at", DateTime(), nullable=True),
        Column("is_deleted", Boolean(), nullable=False, default=False),
        sa.PrimaryKeyConstraint("id"),
    )


def downgrade():
    op.drop_table("job_seeker_postings")
    op.drop_table("working_hours")
    op.drop_table("locations")
    op.drop_table("job_postings")