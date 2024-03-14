FROM python:3.7
COPY . /Boston_prediction 
WORKDIR /Boston_prediction
RUN pip install -r requirements.txt
EXPOSE $PORT
CMD gunicorn --workers=4 --bind 0.0.0.0:$PORT Boston_prediction.wsgi