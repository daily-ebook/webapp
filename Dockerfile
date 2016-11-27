FROM python:3.5-slim
MAINTAINER crisbal cristian@baldi.me

WORKDIR /webapp

ADD requirements.txt .
RUN pip install -r requirements.txt

ADD . .

ENTRYPOINT ["python"]
CMD ["app.py"]