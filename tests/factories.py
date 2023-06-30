from datetime import datetime
from sqlalchemy.orm import scoped_session, sessionmaker
from factory import (
    LazyAttribute,
    LazyFunction,
    Sequence,
    SubFactory,
    post_generation,
    SelfAttribute,
)
from factory.alchemy import SQLAlchemyModelFactory
from factory.fuzzy import FuzzyChoice, FuzzyDateTime, FuzzyInteger, FuzzyText
from faker import Faker
from faker.providers import misc
from pytz import UTC

from src.job.models import JobPosting, Location, WorkingHours
from src.job.enums import JobPostingStatusEnum, JobCategoryEnum
from .session import Session


fake = Faker()
fake.add_provider(misc)


class BaseFactory(SQLAlchemyModelFactory):
    class Meta:
        abstract = True
        sqlalchemy_session_persistence = "commit"


class TimeStampBaseFactory(BaseFactory):
    created_at = fake.date_time_between(start_date="-1y", end_date="now", tzinfo=UTC)
    updated_at = FuzzyDateTime(datetime(2023, 1, 1, tzinfo=UTC))


class LocationFactory(BaseFactory):
    class Meta:
        model = Location
        sqlalchemy_session = Session

    name = "서울"
    parent_id = None



class JobPostingFactory(TimeStampBaseFactory):
    class Meta:
        model = JobPosting
        sqlalchemy_session = Session
        
    title = fake.sentence()
    content = FuzzyText()
    category = FuzzyChoice(list(JobCategoryEnum))
    location_id = fake.pyint(min_value=1, max_value=2)
    salary = {"시급": fake.pyint(min_value=10_000, max_value=100_000)}

