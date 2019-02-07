import os
import pytest
from pathlib import Path
from config import get_config, AppConfigDefault
from a import A
from b import B


def test_01_read_default_conf():
    appconf = get_config()
    print()
    for k, v in appconf.config.items():
        print(f"{k}: {v}")


def test_02_extend_default_conf():
    appconf = get_config()
    appconf.config['LOGLEVEL'] = 'INFO'
    a = A()
    a.print_conf()


def test_03_custom_config():
    app_conf_path = Path().cwd() / 'app_config1.py'
    assert app_conf_path.is_file(), 'missing config file ' + str(app_conf_path)
    os.environ["APP_CONFIG_MODULE"] = str(app_conf_path)
    appconf = get_config()
    appconf.config['LOGLEVEL'] = 'INFO'
    b = B()
    b.print_conf()
