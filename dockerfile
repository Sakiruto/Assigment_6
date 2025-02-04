FROM apache/airflow:latest

USER root
RUN apt-get update && \
    apt-get -y install git && \
    apt-get clean

RUN python -m venv pyairbyte-venv && source pyairbyte-venv/bin/activate &&\
    pip install airbyte && deactivate

USER airflow