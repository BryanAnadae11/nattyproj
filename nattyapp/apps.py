from django.apps import AppConfig


class NattyappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'nattyapp'

    def ready(self):
    	import nattyapp.signals
