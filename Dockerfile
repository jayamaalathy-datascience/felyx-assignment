FROM python:3.11

RUN pip install pandas mysql-connector-python

ADD main.py .

CMD ["python","./main.py"]
