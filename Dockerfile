FROM python:2.7.15

WORKDIR /usr/src/release-deployment-history

RUN pip install flask 

COPY . .
EXPOSE 3005

ENTRYPOINT python app.py
