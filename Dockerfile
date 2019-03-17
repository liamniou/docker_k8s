FROM python:3
RUN mkdir -p /app
WORKDIR /app
COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8081
CMD ["/bin/sh", "-c", "python main.py > /app/flask.log 2>&1"]