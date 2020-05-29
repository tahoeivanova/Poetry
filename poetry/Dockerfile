FROM python:3.8.0-alpine

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /code

# Copy project
COPY . /code/

RUN pip install --upgrade pip

# Install psycopg2 dependencies
RUN apk add build-base
RUN apk add postgresql-dev
RUN apk add --no-cache jpeg-dev zlib-dev

RUN pip install -r requirements.txt
