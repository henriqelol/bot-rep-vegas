import os

_settings = None


def get_settings():
    global _settings

    if _settings is None:
        """
        Dependency to provide app settings
        """
        os.environ.setdefault('SIMPLE_SETTINGS', __name__ + '.development')
        # Do the import in here to avoid circular dependency between
        # `simple_settings` and the settings modules defined in this package:
        from simple_settings import settings

        _settings = settings

    assert _settings is not None
    return _settings
