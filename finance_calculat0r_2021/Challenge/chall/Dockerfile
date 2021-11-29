FROM python

RUN apt update && apt-get install -y xinetd && rm -rf /var/lib/apt/lists/*

WORKDIR /opt/

COPY requirements.txt .
RUN pip install -r requirements.txt

# challenge files
RUN useradd -m ctf
COPY main.py flag.txt ./
COPY python_svc /etc/xinetd.d/

CMD xinetd -dontfork
