import importlib.util
import os
from pathlib import Path


def get_config():
    if 'APP_CONFIG_MODULE' in os.environ:
        path = Path(os.environ["APP_CONFIG_MODULE"])
        if path.is_file():
            spec = importlib.util.spec_from_file_location("config", path)
            config = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(config)
            app_config = config.AppConfig()
            return app_config
        else:
            raise Exception(f"File specified by APP_CONFIG_MODULE does not exist: {path}")
    else:
        import config
        return config.AppConfigDefault()
