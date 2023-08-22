FROM python:latest

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir redis

COPY *.py ./

CMD [ "python", "main.py"]