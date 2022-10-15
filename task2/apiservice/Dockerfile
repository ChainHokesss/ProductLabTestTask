FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /apiservice/
COPY requirements.txt /apiservice/
RUN pip install -r requirements.txt
COPY . /apiservice/
EXPOSE 8000