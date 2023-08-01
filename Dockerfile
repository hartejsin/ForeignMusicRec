FROM python:3

WORKDIR /songRec

COPY requirements.txt .

RUN pip3 install -r requirements.txt

COPY . .

ENV FLASK_APP="main.py"
EXPOSE 5000

CMD ["python3","main.py"]