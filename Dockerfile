FROM apache/airflow:2.9.2-python3.9

COPY requirements.txt /opt/airflow/

USER root

RUN apt-get update && apt-get install -y gcc python3-dev

USER airflow
#RUN pip install --upgrade pip

RUN pip install -r ./requirements.txt

