import os

import sentry_sdk

def setup_sentry():
    sentry_sdk.init(os.getenv('SENTRY_DSN'))
