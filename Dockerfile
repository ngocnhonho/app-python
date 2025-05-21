FROM python:3.12-alpine3.21

COPY ./requirements.txt /tmp

RUN pip install --no-cache-dir -r /tmp/requirements.txt

COPY ./src /src

CMD python /src/app.py