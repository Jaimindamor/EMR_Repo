from django.apps import AppConfig


class EmrAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'EMR_App'
    
    
    def ready(self):
        import EMR_App.signals