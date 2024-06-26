from .common import *  # noqa

# DJANGO-BROWSER-RELOAD

INSTALLED_APPS += [
    # DEVELOPMENT APPS
    "django_browser_reload",
    "django_tailwind_cli",
    "debug_toolbar",
]


MIDDLEWARE += [
    "django_browser_reload.middleware.BrowserReloadMiddleware",
    "debug_toolbar.middleware.DebugToolbarMiddleware",
]

# MAIL

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

# DEBUG TOOLBAR

INTERNAL_IPS = [
    "127.0.0.1",
]
