import os

# App settings
PORT = int(os.getenv("PORT", 0)) or 5000
LOG_FORMAT = os.getenv("LOG_FORMAT", "%(asctime)s %(filename)s %(lineno)s %(process)d %(levelname)s: %(message)s")
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
LOG_FILENAME = os.getenv("LOG_FILENAME", "/tmp/myapp.log")

# Tornado settings
TORNADO_SETTINGS = {"template_path": "templates", "static_path": "static"}
