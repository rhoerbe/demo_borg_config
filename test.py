import os
import pytest
from pathlib import Path
from config import AppConfigAbstract, AppConfigDefault
from a import A
from b import B


def test_01_read_default_conf():
    appconf = AppConfigAbstract.get_config()
    print("\nDATABASES")
    for k, v in appconf.DATABASES.items():
        print(f"    {k}: {v}")
    print(f"LANGUAGE_CODE: {appconf.LANGUAGE_CODE}")
    print(f"TIME_ZONE: {appconf.TIME_ZONE}")


def test_02_extend_default_conf():
    appconf = AppConfigAbstract.get_config()
    appconf.LOGLEVEL = 'INFO'
    a1 = A()
    a1.print_conf()


def test_03_custom_config():
    app_conf_path = Path().cwd() / 'app_config1.py'
    assert app_conf_path.is_file(), 'missing config file ' + str(app_conf_path)
    os.environ["APP_CONFIG_MODULE"] = str(app_conf_path)
    appconf = AppConfigAbstract.get_config()
    appconf.LOGLEVEL = 'INFO'
    a2 = A()
    a2.print_conf()


def test_04_custom_in_class():
    app_conf_path = Path().cwd() / 'app_config1.py'
    assert app_conf_path.is_file(), 'missing config file ' + str(app_conf_path)
    os.environ["APP_CONFIG_MODULE"] = str(app_conf_path)
    b1 = B()
    b1.print_conf()
