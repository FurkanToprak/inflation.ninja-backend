FROM python:3.10-alpine
# EXPOSE 8080
WORKDIR /app
COPY requirements.txt .
RUN pip3 install -r requirements.txt
COPY *.py ./
COPY .env .
COPY boot_gunicorn.sh .
RUN mkdir log
ENTRYPOINT ["./boot_gunicorn.sh"]