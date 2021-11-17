FROM python:3.6

WORKDIR /app
COPY . ./app
RUN pip install flask uwsgi mysql-connector-python-rf

CMD [ "python", "/app/python/run.py" ]