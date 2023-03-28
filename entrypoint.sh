
# 使用 gunicorn 作为进程管理器
# 使用 uvicorn.workers.UvicornWorker 类型的工人
# gunicorn 会负责管理死进程并在需要时重新启动新的进程来保持工人的数量
gunicorn app:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000
