FROM python:3.9

WORKDIR /compapp

COPY . .

RUN pip install -r requirements.txt

CMD ["python", "app.py"]

