FROM python:3.9.0-buster

RUN \
  apt-get update && \
  DEBIAN_FRONTEND=nopt/main.pyninteractive \
    apt-get -y install --no-install-recommends \
      xinetd \
      tcpd \
  && \
  apt-get clean && \
  rm -rf /var/lib/apt/lists/

RUN useradd nssh --uid 1337

COPY app/requirements.txt /app/requirements.txt

RUN pip3 install -r /app/requirements.txt

COPY xinetd/xinetd.conf /etc/xinetd.conf
COPY xinetd/ /etc/xinetd.d

COPY app /app

WORKDIR /app

EXPOSE 2222

ENTRYPOINT [ "xinetd", "-dontfork" ]