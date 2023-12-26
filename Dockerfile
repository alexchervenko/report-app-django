FROM python:3.9-slim

WORKDIR /opt/app/test_report_app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY . .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN python manage.py migrate

EXPOSE 8182

CMD ["gunicorn", "test_report.wsgi", "--bind", ":8182"]