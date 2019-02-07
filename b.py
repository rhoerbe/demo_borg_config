from config import AppConfigAbstract

class B:
    def __init__(self):
        self.appconf = AppConfigAbstract.get_config()
        self.appconf.LOGLEVEL = 'INFO'

    def print_conf(self):
        print("\nDATABASES")
        for k, v in self.appconf.DATABASES.items():
            print(f"    {k}: {v}")
        print(f"LANGUAGE_CODE: {self.appconf.LANGUAGE_CODE}")
        print(f"TIME_ZONE: {self.appconf.TIME_ZONE}")
        print(f"LOGLEVEL: {self.appconf.LOGLEVEL}")
