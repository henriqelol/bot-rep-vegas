SIMPLE_SETTINGS = {
    'OVERRIDE_BY_ENV': True,
    # https://github.com/drgarcia1986/simple-settings#required-settings-types
    'REQUIRED_SETTINGS_TYPES': {
        'POSTGRESQL_URL': 'str',
        'SQL_DEBUG_MODE': 'str',
        'SQL_POOL_RECYCLE': 'int',
    },
}

POSTGRESQL_URL = ''
SQL_POOL_RECYCLE = 300
SQL_POOL_PRE_PING = False
