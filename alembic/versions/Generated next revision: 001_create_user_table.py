"""create user table

Revision ID: Generated next revision: 001
Revises:
Create Date: 2023-08-30 00:39:37.191181

"""
import uuid
from datetime import datetime

import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

from alembic import op

# revision identifiers, used by Alembic.
revision = "Generated next revision: 001"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    tasks = op.create_table(
        "tasks",
        sa.Column("id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("username", sa.String(), nullable=False),
        sa.Column("last_keep", sa.DateTime(), nullable=False),
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.Column("updated_at", sa.DateTime(), nullable=True),
        sa.Column("deleted_at", sa.DateTime(), nullable=True),
    )

    op.bulk_insert(
        tasks,
        [
            {
                "id": uuid.uuid4(),
                "name": "Mato",
                "username": "henriqelol",
                "last_keep": datetime.utcnow(),
                "created_at": datetime.utcnow(),
            },
            {
                "id": uuid.uuid4(),
                "name": "Marcola",
                "username": "marcola",
                "last_keep": datetime.utcnow(),
                "created_at": datetime.utcnow(),
            },
            {
                "id": uuid.uuid4(),
                "name": "Kubo",
                "username": "kubo",
                "last_keep": datetime.utcnow(),
                "created_at": datetime.utcnow(),
            },
        ],
    )


def downgrade():
    op.drop_table("tasks")
