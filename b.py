from config import get_config

class B:
    def __init__(self):
        self.appconf = get_config()

    def print_conf(self):
        print()
        for k, v in self.appconf.config.items():
            print(f"{k}: {v}")
