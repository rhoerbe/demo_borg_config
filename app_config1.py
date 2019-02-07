class AppConfig():
    ''' Pattern: Keep shared state in a common class (monostate vs singleton - see http://www.aleax.it/5ep.html)
        Whenever an instance is created, state is shared at the class level
    '''
    config = {}
    def __init__(self):
        self.__dict__ = self.config
        self._set_default_config()

    def _set_default_config(self):
        self.config['DATABASES'] = {
            'default': {
                'ENGINE': 'backends.postgresql',
                'NAME': 'mydb1',
                'USER': 'postgres',
                'PASSWORD': 'blah',
                'HOST': 'mydbhost',
                'PORT': '5432',
            },
        }
        self.config['LANGUAGE_CODE'] = 'de'
        self.config['TIME_ZONE'] = 'Europe/Vienna'
