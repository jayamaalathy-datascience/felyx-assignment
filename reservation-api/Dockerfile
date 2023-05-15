FROM python:3.11

RUN pip install shapely pandas fastapi-pagination pymysql fastapi uvicorn sqlalchemy

ADD ./ .

CMD ["uvicorn","main:app","--host", "0.0.0.0"]
