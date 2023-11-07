# Copyright © 2019 Province of British Columbia
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Model to handle all operations related to Event Template."""
import enum
import sqlalchemy as sa
from sqlalchemy.orm import relationship

from .base_model import BaseModelVersioned
from .db import db


class EventPositionEnum(enum.Enum):
    """Event position enum"""

    START = "START"
    INTERMEDIATE = "INTERMEDIATE"
    END = "END"


class EventTemplate(BaseModelVersioned):
    """Model class for Event Template."""

    __tablename__ = "event_templates"

    id = sa.Column(
        sa.Integer, primary_key=True, autoincrement=True
    )  # TODO check how it can be inherited from parent
    name = sa.Column(sa.String)
    parent_id = sa.Column(sa.Integer, nullable=True)
    phase_id = sa.Column(sa.ForeignKey("phase_codes.id"), nullable=False)
    event_type_id = sa.Column(sa.ForeignKey("event_types.id"), nullable=False)
    event_position = sa.Column(sa.Enum(EventPositionEnum))
    multiple_days = sa.Column(sa.Boolean, default=False)
    event_category_id = sa.Column(sa.ForeignKey("event_categories.id"), nullable=False)
    start_at = sa.Column(sa.String, nullable=True)
    number_of_days = sa.Column(sa.Integer, default=0, nullable=False)
    mandatory = sa.Column(sa.Boolean, default=False)
    sort_order = sa.Column(sa.Integer, nullable=False)

    phase = relationship("PhaseCode", foreign_keys=[phase_id], lazy="select")
    event_type = relationship("EventType", foreign_keys=[event_type_id], lazy="select")
    event_category = relationship(
        "EventCategory", foreign_keys=[event_category_id], lazy="select"
    )

    @classmethod
    def find_by_phase_id(cls, _phase_id):
        """Returns the event configurations based on phase id"""
        events = (
            db.session.query(EventTemplate)
            .filter_by(phase_id=_phase_id, is_active=True)
            .order_by(EventTemplate.sort_order.asc())
            .all()
        )  # pylint: disable=no-member
        return events

    @classmethod
    def find_by_phase_ids(cls, _phase_ids):
        """Returns the event configurations based on phase ids"""
        events = (
            db.session.query(EventTemplate)
            .filter(
                EventTemplate.phase_id.in_(_phase_ids),
                EventTemplate.is_active.is_(True),
            )
            .order_by(EventTemplate.sort_order.asc())
            .all()
        )  # pylint: disable=no-member
        return events