FROM ubuntu:20.04

RUN apt-get update && apt-get install -y socat qemu-system-x86 openssl
RUN useradd -UM chall

COPY . /app

WORKDIR /app

RUN chown -R chall:chall .

CMD /app/socat.sh
