FROM python:3.8

ADD . /app

WORKDIR /app

RUN pip install -r r.txt

EXPOSE 6000

CMD ["python", "apps.py"]
