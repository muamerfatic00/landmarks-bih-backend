"""Added accomodation, restaurant, event and social_medias tables. Added their relationships. Added social_media_type enum.

Revision ID: 791eb9b7052f
Revises: a399817151fd
Create Date: 2025-04-23 11:51:38.114771

"""
from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = '791eb9b7052f'
down_revision: Union[str, None] = 'a399817151fd'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # command for creating social media type enum
    social_media_type=sa.Enum('WEBPAGE', 'BOOKING', 'FACEBOOK', 'INSTAGRAM', 'YOUTUBE', name='socialmediatype')

    # commands for creating accommodations table
    op.create_table('accommodations',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('image_url', sa.String(), nullable=True),
    sa.Column('google_maps_url', sa.String(), nullable=True),
    sa.Column('contact_number', sa.String(), nullable=True),
    sa.Column('mail', sa.String(), nullable=True),
    sa.Column('city_id', sa.Integer(), nullable=True),
    sa.Column('landmark_id', sa.Integer(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['city_id'], ['cities.id'], ),
    sa.ForeignKeyConstraint(['landmark_id'], ['landmarks.id'], ),
    sa.PrimaryKeyConstraint('id')
    )

    # commands for creating events table
    op.create_table('events',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('image_url', sa.String(), nullable=True),
    sa.Column('google_maps_url', sa.String(), nullable=True),
    sa.Column('contact_number', sa.String(), nullable=True),
    sa.Column('mail', sa.String(), nullable=True),
    sa.Column('date', sa.Date(), nullable=True),
    sa.Column('time', sa.Time(), nullable=True),
    sa.Column('city_id', sa.Integer(), nullable=True),
    sa.Column('landmark_id', sa.Integer(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['city_id'], ['cities.id'], ),
    sa.ForeignKeyConstraint(['landmark_id'], ['landmarks.id'], ),
    sa.PrimaryKeyConstraint('id')
    )

    # commands for creating restaurants table
    op.create_table('restaurants',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('image_url', sa.String(), nullable=True),
    sa.Column('google_maps_url', sa.String(), nullable=True),
    sa.Column('contact_number', sa.String(), nullable=True),
    sa.Column('mail', sa.String(), nullable=True),
    sa.Column('menu_url', sa.String(), nullable=True),
    sa.Column('city_id', sa.Integer(), nullable=True),
    sa.Column('landmark_id', sa.Integer(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['city_id'], ['cities.id'], ),
    sa.ForeignKeyConstraint(['landmark_id'], ['landmarks.id'], ),
    sa.PrimaryKeyConstraint('id')
    )

    # commands for creating accommodations_social_medias table
    op.create_table('accommodations_social_medias',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('type', social_media_type, nullable=False),
    sa.Column('url', sa.String(), nullable=False),
    sa.Column('accommodation_id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['accommodation_id'], ['accommodations.id'], ),
    sa.PrimaryKeyConstraint('id')
    )

    # commands for creating events_social_medias table
    op.create_table('events_social_medias',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('type', social_media_type, nullable=False),
    sa.Column('url', sa.String(), nullable=False),
    sa.Column('event_id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['event_id'], ['events.id'], ),
    sa.PrimaryKeyConstraint('id')
    )

    # commands for creating events_social_medias table
    op.create_table('restaurants_social_medias',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('type',social_media_type, nullable=False),
    sa.Column('url', sa.String(), nullable=False),
    sa.Column('restaurant_id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['restaurant_id'], ['restaurants.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table('restaurants_social_medias')
    op.drop_table('events_social_medias')
    op.drop_table('accommodations_social_medias')
    op.drop_table('restaurants')
    op.drop_table('events')
    op.drop_table('accommodations')
    # ### end Alembic commands ###
