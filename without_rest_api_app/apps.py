from django.apps import AppConfig


class WithoutRestApiAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'without_rest_api_app'
