FROM python:latest
RUN apt-get update && apt-get install -y python3-pip
COPY . .
RUN pip3 install -r requirements.txt
EXPOSE 5002
ENTRYPOINT [ "python3", "app.py" ]