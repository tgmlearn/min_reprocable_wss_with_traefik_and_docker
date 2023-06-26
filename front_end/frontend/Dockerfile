FROM python:3.9



RUN pip install asgiref boto3 botocore Django Jinja2 jmespath MarkupSafe numpy pandas python-dateutil pytz PyYAML render s3transfer six sqlparse tzdata urllib3 asyncio websockets channels mysqlclient mysql-connector-python bcrypt python-dotenv cryptography
RUN pip install daphne


COPY . frontend


ENTRYPOINT ["python", "frontend/manage.py"]
CMD ["runserver", "0.0.0.0:8001"]
