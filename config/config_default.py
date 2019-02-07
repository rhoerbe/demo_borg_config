class AppConfigDefault():
    '''
    Global application configuration
    This class uses the Borg Pattern:
        Keep shared state in a common class (monostate vs singleton - see http://www.aleax.it/5ep.html)
        Whenever an instance is created, state is shared at the class level
    '''
    config = {}
    def __init__(self):
        self.__dict__ = self.config
        self._set_default_config()

    def _set_default_config(self):
        self.config['DATABASES'] = {
            'ENGINE': 'postgresql',
            'NAME': 'mydb',
            'USER': 'postgres',
            'PASSWORD': 'changeit',
            'HOST': 'localhost',
            'PORT': '5432',
        }
        self.config['LANGUAGE_CODE'] = 'en'
        self.config['TIME_ZONE'] = 'Europe/Vienna'
