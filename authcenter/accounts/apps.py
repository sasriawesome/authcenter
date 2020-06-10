from django.apps import AppConfig as BaseAppConfig

class AppConfig(BaseAppConfig):
    name = 'authcenter.accounts'
    label = 'authcenter_accounts'