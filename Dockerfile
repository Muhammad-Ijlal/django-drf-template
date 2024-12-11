# pull official base image
FROM python:3.12.4-slim-bullseye

# set work directory
WORKDIR /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


# install system dependencies
RUN apt-get update && apt-get install \
    libpq-dev python3-dev build-essential -y

# install python dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install --no-cache -r requirements.txt
RUN pip install gunicorn


# copy project
COPY . .

RUN chmod +x entrypoint.sh

# Expose the PORT
EXPOSE 8000

# Set the entrypoint
ENTRYPOINT ["bash","entrypoint.sh"]
