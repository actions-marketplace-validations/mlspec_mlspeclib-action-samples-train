FROM mlspec/mlspeclib-action-docker@sha256:c13eac93072c5d7f5582bd89bef72d0ef9518a3f263489514e146bca3a9e612d

RUN apt-get -y update && apt-get -y install python3-all python3-pip

COPY requirements.txt /requirements.txt

ARG FIRSTCACHEBUST=1

RUN python3 -m pip install -U pip
RUN python3 -m pip install --no-cache-dir -r /requirements.txt

COPY .parameters/schemas /src/parameters
COPY integration/.parameters/schemas /src/parameters/test_schemas
COPY step_execution.py /src
COPY integration/container_debugging.sh /src

ENTRYPOINT ["./entrypoint.sh"]
