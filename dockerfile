
# we do not require a whole system image for this, we can roll with python alone
FROM python:3.8-alpine

WORKDIR /sample

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY src/app.py .

CMD [ "python", "./app.py" ]
