FROM python:3.6

RUN mkdir -p /app
WORKDIR /app

ADD yuqing_api /app

RUN pip3 install -r requirements.txt

EXPOSE 5000

ENTRYPOINT ["python"]
CMD ["yuqing/__init__.py"]