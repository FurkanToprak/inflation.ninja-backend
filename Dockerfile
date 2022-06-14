FROM python:3.10-alpine
EXPOSE 8080/tcp
WORKDIR /app
COPY requirements.txt .
COPY *.py ./
COPY .env .
RUN pip3 install -r requirements.txt
RUN mkdir log
RUN python3 -m gunicorn -b 0.0.0.0:8080 -t 0 app:app