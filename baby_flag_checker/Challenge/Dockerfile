FROM ubuntu:20.04

RUN apt-get update && apt-get -y upgrade && apt-get -y --no-install-recommends install xinetd

COPY ./xinetd_chall /etc/xinetd.d/xinetd_chall

RUN useradd -m ctf
WORKDIR /home/ctf
ADD run.sh chall ./

RUN chown -R root:ctf /home/ctf
RUN chmod 750 /home/ctf
RUN chmod 550 /home/ctf/chall
RUN chmod 550 /home/ctf/run.sh

CMD ["/usr/sbin/xinetd", "-dontfork"]
