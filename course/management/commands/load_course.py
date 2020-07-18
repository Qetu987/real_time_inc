from django.core.management.base import BaseCommand, CommandError
from course.models import Course
from shop.settings import DATA_DIR
from course.course_loader import CourseLoader


class Command(BaseCommand):
  
    def handle(self, *args, **options):
        print('Start course %s' %DATA_DIR)
        for d in CourseLoader.get_active_courses_dirs():
            print(d)
            course = CourseLoader(d)
            course.process()