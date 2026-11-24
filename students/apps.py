from django.apps import AppConfig


class StudentsConfig(AppConfig):
    name = 'students'


    def ready(self):
        import students.signals  # Load our signals when Django starts