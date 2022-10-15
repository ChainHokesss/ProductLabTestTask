FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /asyncservice/
COPY requirements.txt /asyncservice/
RUN pip install -r requirements.txt
COPY . /asyncservice/
EXPOSE 8080