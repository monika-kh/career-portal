import datetime
from datetime import date, timedelta
from decimal import Decimal

from django.test import TestCase

from jobs.models import Apply, Jobs, Subscribers, TechnicalSkills


class TestModels(TestCase):
    """
        Testcase for models.
        """

    def setUp(self):

        self.skill_name = "test"
        self.description = "test code"
        self.skill_public_id = 1001
        self.technical_skills = TechnicalSkills.objects.create(
            name=self.skill_name,
            description=self.description,
            public_id=self.skill_public_id,
        )
        self.job_public_id = 1
        self.job_name = "test job"
        self.job_description = "test coder"
        self.tag = "backend"
        self.min_exp = "0.00"
        self.max_exp = "0.05"
        self.active = True
        self.start_date = datetime.date.today()
        self.end_date = datetime.date.today() + datetime.timedelta(days=2)

        self.job = Jobs.objects.create(
            public_id=self.job_public_id,
            job_name=self.job_name,
            job_description=self.job_description,
            tag=self.tag,
            max_exp=self.max_exp,
            min_exp=self.min_exp,
            active=self.active,
            start_date=self.start_date,
            end_date=self.end_date,
            skill=self.technical_skills,
        )
        self.subscriber_public_id = 1
        self.subscriber_name = "test"
        self.email = "test@test.com"
        self.location = "indore"
        self.status = True

        self.subscriber = Subscribers.objects.create(
            public_id=self.subscriber_public_id,
            name=self.subscriber_name,
            email=self.email,
            location=self.location,
            status=self.status,
        )

        self.apply_public_id = 1
        self.user_name = "test_name"
        self.resume = "media/test.pdf"
        self.skills = self.technical_skills

    def test_technical_skills(self):
        skills = TechnicalSkills.objects.get(
            name=self.skill_name,
            description=self.description,
            public_id=self.skill_public_id,
        )
        assert skills.name == self.skill_name
        assert skills.description == self.description
        assert skills.public_id == self.skill_public_id

    def test_jobs(self):
        test_jobs = Jobs.objects.get(
            public_id=self.job_public_id,
            job_name=self.job_name,
            job_description=self.job_description,
            tag=self.tag,
            max_exp=self.max_exp,
            min_exp=self.min_exp,
            active=self.active,
            start_date=self.start_date,
            end_date=self.end_date,
            skill=self.technical_skills,
        )

        assert test_jobs.public_id == self.job_public_id
        assert test_jobs.job_name == self.job_name
        assert test_jobs.job_description == self.job_description
        assert test_jobs.tag == self.tag
        assert test_jobs.max_exp == Decimal(self.max_exp)
        assert test_jobs.min_exp == Decimal(self.min_exp)
        assert test_jobs.active == self.active
        assert test_jobs.start_date == self.start_date
        assert test_jobs.end_date == self.end_date
        assert test_jobs.skill == self.technical_skills

    def test_subscriber(self):
        subscriber_create = Subscribers.objects.get(
            public_id=self.subscriber_public_id,
            name=self.subscriber_name,
            email=self.email,
            location=self.location,
            status=self.status,
        )

        assert subscriber_create.public_id == self.subscriber_public_id
        assert subscriber_create.name == self.subscriber_name
        assert subscriber_create.email == self.email
        assert subscriber_create.location == self.location
        assert subscriber_create.status== self.status

    def test_apply(self):
        apply = Apply.objects.create(
            public_id=self.apply_public_id,
            name=self.user_name,
            email=self.email,
            resume=self.resume,
        )
        apply.skill.add(self.skills.id)
        assert apply.public_id == self.apply_public_id
        assert apply.name == self.user_name
        assert apply.email == self.email
        assert apply.resume == self.resume
