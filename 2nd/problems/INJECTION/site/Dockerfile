FROM python:3.8-slim-buster

WORKDIR /app

COPY requirements.txt run.py .

RUN mkdir templates
COPY templates/ templates/

RUN python3 -m pip install -r requirements.txt

CMD ["python3", "-u", "run.py"]

