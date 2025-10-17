from django.apps import AppConfig


class AttendanceModuleConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'attendance_module'

    def ready(self): 
        import attendance_module.signals 
