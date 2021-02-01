FROM python:3.7-alpine
WORKDIR /code

RUN apk update && apk add build-base \
    python3-dev \
    gcc \
    libc-dev
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 8000

COPY . .

CMD ["python", "server.py"]