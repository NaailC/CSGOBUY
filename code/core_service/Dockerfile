FROM python:latest
ARG APP_VERSION
RUN apt-get update && apt-get install -y python3-pip
COPY . .
RUN pip3 install -r requirements.txt
EXPOSE 5000
ENTRYPOINT [ "python3", "app.py" ]