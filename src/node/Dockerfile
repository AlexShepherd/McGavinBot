# Dockerfile, Image, Container
FROM python:3.9

ADD shooterbot.py .
ADD .env .

RUN pip install discord psycopg2 python-dotenv
CMD ["python", "./shooterbot.py"]
