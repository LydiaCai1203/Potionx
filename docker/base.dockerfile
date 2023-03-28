FROM python:3.10.4-alpine3.15

WORKDIR /app

RUN sed -i "s/dl-cdn.alpinelinux.org/mirrors.aliyun.com/g" /etc/apk/repositories && \
    apk update && apk add build-base linux-headers postgresql-dev gcc g++ swig patchelf python3-dev musl-dev postgresql-libs postgresql-client

RUN pip install --default-timeout=120 --upgrade pip -i https://mirrors.aliyun.com/pypi/simple

COPY ./requirements.txt /app

RUN pip install --no-cache-dir -r requirements.txt \
    && rm -f requirements.txt

RUN apk del build-base linux-headers gcc g++ swig patchelf musl-dev python3-dev

ADD . /app

EXPOSE 5555

CMD ["python", "main.py"]
