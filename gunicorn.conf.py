import os

# Railway assigns the port at runtime, so it has to be read here rather than baked
# into a command line.
bind = f"0.0.0.0:{os.environ.get('PORT', '8080')}"
workers = int(os.environ.get("WEB_CONCURRENCY", "2"))
accesslog = "-"
errorlog = "-"
