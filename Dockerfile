FROM python:3.9.15

ADD file.py .

RUN apt-get update -y

RUN apt install ufw -y

RUN ufw allow 9001

RUN pip install --upgrade pip

RUN pip install asyncio uvloop gmqtt

CMD ["python","./file.py"]