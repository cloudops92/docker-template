FROM python:3.7

# Setting workdir
WORKDIR /usr/src/app

# Installing python dependancies using pip
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY src/ .

ENTRYPOINT ["python", "main.py"]