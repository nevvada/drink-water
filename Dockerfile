FROM python:3.9

ADD main.py .
ADD .env .

RUN pip install twilio

CMD ["python", "main.py"]
