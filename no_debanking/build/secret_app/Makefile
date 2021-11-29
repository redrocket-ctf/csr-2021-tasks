CC = gcc
CFLAGS  = -static

all: secret_app

secret_app: main.c
	$(CC) $(CFLAGS) -o secret_app main.c
clean:
	$(RM) secret_app