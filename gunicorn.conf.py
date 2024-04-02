# Gunicorn configuration file
import multiprocessing

max_requests = 1000
max_requests_jitter = 50

log_file = "-"

bind = "0.0.0.0:8000"

worker_class = "uvicorn.workers.UvicornWorker"
workers = min((multiprocessing.cpu_count() * 2) + 1, 4)  # Max workers = 4, as currently we load the index in memory
timeout = 120