FROM python:3.10-alpine
EXPOSE 8080/tcp
WORKDIR /app
COPY requirements.txt .
COPY *.py ./
COPY .env .
RUN pip3 install -r requirements.txt
RUN mkdir log
CMD ["python3", "./app.py"]