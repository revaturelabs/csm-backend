FROM python:3
COPY ./requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install -r requirements.txt
COPY ./src /app/src
CMD ["flask","run","--host=0.0.0.0"]