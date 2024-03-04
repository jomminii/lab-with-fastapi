# uvicorn app.main:app --reload --host localhost --port 8001
# uvicorn app.main:app --workers 2 --reload --host localhost --port 8001
# gunicorn app.main:app --workers 2 --reload --host localhost --port 8001
gunicorn app.main:app --reload --bind 0.0.0.0:8001 --workers 1 --worker-class uvicorn.workers.UvicornWorker