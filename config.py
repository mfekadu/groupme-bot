from os import environ
import multiprocessing

PORT = int(environ.get("PORT", 8080))
DEBUG_MODE = int(environ.get("DEBUG_MODE", 1))

GROUPME_ACCESS_TOKEN = environ.get("GROUPME_ACCESS_TOKEN", None)
GROUPME_CALLBACK_URL = environ.get("GROUPME_CALLBACK_URL", None)
GROUPME_CLIENT_ID = environ.get("GROUPME_CLIENT_ID", None)
GROUPME_REDIRECT_URL = environ.get("GROUPME_REDIRECT_URL", None)

# Gunicorn config
bind = ":" + str(PORT)
workers = multiprocessing.cpu_count() * 2 + 1
threads = 2 * multiprocessing.cpu_count()