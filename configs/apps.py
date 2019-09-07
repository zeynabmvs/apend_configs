from django.apps import AppConfig


class ConfigsConfig(AppConfig):
    name = 'configs'

    def ready(self):
        import configs.signals