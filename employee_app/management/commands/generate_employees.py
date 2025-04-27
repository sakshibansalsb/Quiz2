from django.core.management.base import BaseCommand
from employee_app.models import Employee, Department, Attendance, Performance
from faker import Faker
import random

class Command(BaseCommand):
    help = 'Generate fake employee data'

    def handle(self, *args, **kwargs):
        fake = Faker()
        departments = ['HR', 'Finance', 'IT', 'Marketing']

        for dept_name in departments:
            Department.objects.get_or_create(name=dept_name)

        for _ in range(20):
            dept = random.choice(Department.objects.all())
            employee = Employee.objects.create(
                name=fake.name(),
                email=fake.unique.email(),
                department=dept,
                position=fake.job(),
                date_joined=fake.date_this_decade(),
                salary=random.randint(30000, 100000)
            )

            for _ in range(5):
                Attendance.objects.create(
                    employee=employee,
                    date=fake.date_this_year(),
                    status=random.choice(['Present', 'Absent'])
                )

                Performance.objects.create(
                    employee=employee,
                    review_date=fake.date_this_year(),
                    score=random.randint(1, 10)
                )

        self.stdout.write(self.style.SUCCESS('Fake employees generated successfully'))
