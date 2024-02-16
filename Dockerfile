# Dockerfile, Image, Container
FROM python:3.9

ADD shooterbot.py .

RUN pip install discord psycopg2

CMD ["python", "./shooterbot.py"]
