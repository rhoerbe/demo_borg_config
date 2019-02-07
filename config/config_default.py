from config.config_abstract import AppConfigAbstract


class AppConfigDefault(AppConfigAbstract):

    def _set_config(self):
        config = self.config['confkey']
        config.DATABASES = {
            'ENGINE': 'postgresql',
            'NAME': 'mydb',
            'USER': 'postgres',
            'PASSWORD': 'changeit',
            'HOST': 'localhost',
            'PORT': '5432',
        }
        config.LANGUAGE_CODE = 'en'
        config.TIME_ZONE = 'Europe/Vienna'
