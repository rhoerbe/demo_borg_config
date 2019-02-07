from config.config_abstract import AppConfigAbstract


class AppConfig(AppConfigAbstract):

    def _set_config(self):
        config = self.config['confkey']
        config.DATABASES = {
            'ENGINE': 'postgresql',
            'NAME': 'customdb',
            'USER': 'postgres',
            'PASSWORD': 'blahblah',
            'HOST': 'pghost',
            'PORT': '5432',
        }
        config.LANGUAGE_CODE = 'de'
        config.TIME_ZONE = 'Europe/Berlin'
