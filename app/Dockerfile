FROM ubuntu:xenial

RUN apt-get update && \
	apt-get install --yes gnupg2 software-properties-common apt-transport-https && \
	apt-key adv --keyserver keyserver.ubuntu.com --recv-keys E298A3A825C0D65DFD57CBB651716619E084DAB9 && \
	apt-get update && \
	apt-get install --yes software-properties-common apt-transport-https python3 python3-pip

ADD app.py .
ADD requirements.txt .

RUN pip3 install -r requirements.txt