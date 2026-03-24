import os
import multiprocessing

# Server Socket
bind = os.getenv('BIND', '0.0.0.0:8000')
backlog = 2048

# Worker Processes
workers = int(os.getenv('WORKERS', multiprocessing.cpu_count() * 2 + 1))
worker_class = 'sync'
worker_connections = 1000
max_requests = 1000
max_requests_jitter = 50
timeout = 30
keepalive = 2

# Logging
accesslog = '-'
access_log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s" %(D)s'
errorlog = '-'
loglevel = 'info'

# Process Naming
proc_name = 'django_porfolio'

# Django specific
raw_env = [
    'DJANGO_SETTINGS_MODULE=django_porfolio.settings',
]
