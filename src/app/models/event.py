from sqlalchemy import Column, Date, Integer, String, Time, ForeignKey
from sqlalchemy.orm import relationship

from src.app.database import Base
from src.app.models.timestamp import TimestampMixin


class Event(Base, TimestampMixin):
    __tablename__ = 'events'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String)
    image_url = Column(String)
    google_maps_url = Column(String)
    contact_number = Column(String)
    mail = Column(String)
    date = Column(Date)
    time = Column(Time)
    city_id = Column(Integer, ForeignKey('cities.id', ondelete='SET NULL'))
    landmark_id = Column(Integer, ForeignKey('landmarks.id', ondelete='SET NULL'))

    # relationships
    city = relationship('City', back_populates='events')
    landmark = relationship('Landmark', back_populates='events')
    social_medias = relationship('EventSocialMedia', back_populates='event')

    def __str__(self):
        return (f"<Event(id={self.id}, name={self.name}, description={self.description}, "
                f"image_url={self.image_url}, google_maps_url={self.google_maps_url}, "
                f"contact_number={self.contact_number}, mail={self.mail}, date={self.date}, time={self.time}, "
                f"city_id={self.city_id}, landmark_id={self.landmark_id}, social_medias={self.social_medias})>")

    def __repr__(self):
        return (f"Event(id={self.id},name={self.name},description={self.description},"
                f"image_url={self.image_url},google_maps_url={self.google_maps_url},"
                f"contact_number={self.contact_number},mail={self.mail},date={self.date},time={self.time},"
                f"city_id={self.city_id},landmark_id={self.landmark_id})")
