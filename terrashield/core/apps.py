from django.apps import AppConfig

class CoreConfig(AppConfig):
    name = 'core'

    def ready(self):
        import core.signals  # This ensures signals are imported and ready to use