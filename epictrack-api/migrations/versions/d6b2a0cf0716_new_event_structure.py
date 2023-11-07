"""new event structure

Revision ID: d6b2a0cf0716
Revises: 20a4532cabb9
Create Date: 2023-06-12 13:39:55.814884

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd6b2a0cf0716'
down_revision = '20a4532cabb9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('calendar_events',
    sa.Column('created_by', sa.String(length=255), nullable=True),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_by', sa.String(length=255), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('is_active', sa.Boolean(), server_default='t', nullable=False),
    sa.Column('is_deleted', sa.Boolean(), server_default='f', nullable=False),
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('anticipated_date', sa.DateTime(), nullable=False),
    sa.Column('actual_date', sa.DateTime(), nullable=True),
    sa.Column('number_of_days', sa.Integer(), nullable=True),
    sa.Column('link', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('event_categories',
    sa.Column('created_by', sa.String(length=255), nullable=True),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_by', sa.String(length=255), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('is_active', sa.Boolean(), server_default='t', nullable=False),
    sa.Column('is_deleted', sa.Boolean(), server_default='f', nullable=False),
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('sort_order', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('event_types',
    sa.Column('created_by', sa.String(length=255), nullable=True),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_by', sa.String(length=255), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('is_active', sa.Boolean(), server_default='t', nullable=False),
    sa.Column('is_deleted', sa.Boolean(), server_default='f', nullable=False),
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('event_category_id', sa.Integer(), nullable=False),
    sa.Column('sort_order', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['event_category_id'], ['event_categories.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('event_fields',
    sa.Column('created_by', sa.String(length=255), nullable=True),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_by', sa.String(length=255), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('is_active', sa.Boolean(), server_default='t', nullable=False),
    sa.Column('is_deleted', sa.Boolean(), server_default='f', nullable=False),
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('event_category_id', sa.Integer(), nullable=False),
    sa.Column('event_type_id', sa.Integer(), nullable=False),
    sa.Column('field_type', sa.String(), nullable=True),
    sa.Column('reference', sa.String(), nullable=True),
    sa.Column('control_label', sa.String(), nullable=True),
    sa.Column('validations', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['event_category_id'], ['event_categories.id'], ),
    sa.ForeignKeyConstraint(['event_type_id'], ['event_types.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('event_templates',
    sa.Column('created_by', sa.String(length=255), nullable=True),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_by', sa.String(length=255), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('is_active', sa.Boolean(), server_default='t', nullable=False),
    sa.Column('is_deleted', sa.Boolean(), server_default='f', nullable=False),
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('phase_id', sa.Integer(), nullable=False),
    sa.Column('event_type_id', sa.Integer(), nullable=False),
    sa.Column('start_at', sa.Integer(), nullable=False),
    sa.Column('number_of_days', sa.Integer(), nullable=False),
    sa.Column('mandatory', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['event_type_id'], ['event_types.id'], ),
    sa.ForeignKeyConstraint(['phase_id'], ['phase_codes.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('task_templates',
    sa.Column('created_by', sa.String(length=255), nullable=True),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_by', sa.String(length=255), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('is_active', sa.Boolean(), server_default='t', nullable=False),
    sa.Column('is_deleted', sa.Boolean(), server_default='f', nullable=False),
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('phase_id', sa.Integer(), nullable=False),
    sa.Column('work_type_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['phase_id'], ['phase_codes.id'], ),
    sa.ForeignKeyConstraint(['work_type_id'], ['work_types.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('tasks',
    sa.Column('created_by', sa.String(length=255), nullable=True),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_by', sa.String(length=255), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('is_active', sa.Boolean(), server_default='t', nullable=False),
    sa.Column('is_deleted', sa.Boolean(), server_default='f', nullable=False),
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('start_at', sa.Integer(), nullable=False),
    sa.Column('number_of_days', sa.Integer(), nullable=False),
    sa.Column('template_id', sa.Integer(), nullable=False),
    sa.Column('tips', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['template_id'], ['task_templates.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('task_events',
    sa.Column('created_by', sa.String(length=255), nullable=True),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_by', sa.String(length=255), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('is_active', sa.Boolean(), server_default='t', nullable=False),
    sa.Column('is_deleted', sa.Boolean(), server_default='f', nullable=False),
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('work_id', sa.Integer(), nullable=False),
    sa.Column('phase_id', sa.Integer(), nullable=False),
    sa.Column('anticipated_date', sa.DateTime(), nullable=False),
    sa.Column('actual_date', sa.DateTime(), nullable=True),
    sa.Column('start_at', sa.Integer(), nullable=False),
    sa.Column('number_of_days', sa.Integer(), nullable=False),
    sa.Column('tips', sa.String(), nullable=True),
    sa.Column('notes', sa.String(), nullable=True),
    sa.Column('responsible_entity', sa.Enum('Proponent', 'PIN', 'EAO', 'Federal Agencies', name="responsibleentityenum"), nullable=True),
    sa.Column('is_completed', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['phase_id'], ['phase_codes.id'], ),
    sa.ForeignKeyConstraint(['work_id'], ['works.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('work_calendar_events',
    sa.Column('created_by', sa.String(length=255), nullable=True),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_by', sa.String(length=255), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('is_active', sa.Boolean(), server_default='t', nullable=False),
    sa.Column('is_deleted', sa.Boolean(), server_default='f', nullable=False),
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('work_id', sa.Integer(), nullable=False),
    sa.Column('phase_id', sa.Integer(), nullable=False),
    sa.Column('calendar_event_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['calendar_event_id'], ['calendar_events.id'], ),
    sa.ForeignKeyConstraint(['phase_id'], ['phase_codes.id'], ),
    sa.ForeignKeyConstraint(['work_id'], ['works.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('event_field_values',
    sa.Column('created_by', sa.String(length=255), nullable=True),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_by', sa.String(length=255), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('is_active', sa.Boolean(), server_default='t', nullable=False),
    sa.Column('is_deleted', sa.Boolean(), server_default='f', nullable=False),
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('field_id', sa.Integer(), nullable=False),
    sa.Column('event_id', sa.Integer(), nullable=False),
    sa.Column('value', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['event_id'], ['events.id'], ),
    sa.ForeignKeyConstraint(['field_id'], ['event_fields.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('task_event_assignees',
    sa.Column('created_by', sa.String(length=255), nullable=True),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_by', sa.String(length=255), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('is_active', sa.Boolean(), server_default='t', nullable=False),
    sa.Column('is_deleted', sa.Boolean(), server_default='f', nullable=False),
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('task_event_id', sa.Integer(), nullable=False),
    sa.Column('assignee_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['assignee_id'], ['staffs.id'], ),
    sa.ForeignKeyConstraint(['task_event_id'], ['task_events.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('projects', schema=None) as batch_op:
        batch_op.alter_column('type_id',
               existing_type=sa.INTEGER(),
               nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('projects', schema=None) as batch_op:
        batch_op.alter_column('type_id',
               existing_type=sa.INTEGER(),
               nullable=True)

    op.drop_table('task_event_assignees')
    op.drop_table('event_field_values')
    op.drop_table('work_calendar_events')
    op.drop_table('task_events')
    op.drop_table('tasks')
    op.drop_table('task_templates')
    op.drop_table('event_templates')
    op.drop_table('event_fields')
    op.drop_table('event_types')
    op.drop_table('event_categories')
    op.drop_table('calendar_events')
    # ### end Alembic commands ###