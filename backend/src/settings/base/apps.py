DEFAULT_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.humanize",
    "rest_framework",
    "constance",
    "constance.backends.database",
    "ckeditor",
    "ckeditor_uploader",
]

PROJECT_APPS = [
    "apps.services",
    "apps.users",
    "apps.products",
    "apps.orders",
    "apps.warehouse",
]

DEVELOPER_APPS = [
    *DEFAULT_APPS,
    *PROJECT_APPS,
    "debug_toolbar",
]

PRODUCTION_APPS = [*DEFAULT_APPS, *PROJECT_APPS]
