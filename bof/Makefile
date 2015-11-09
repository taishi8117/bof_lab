CC=gcc
CFLAGS=-m32 -std=c99 -Wall -fno-stack-protector

all: bof

bof: bof.o
	$(CC) $(CFLAGS) -o $@ $^
	sudo chown 0:0 $@
	sudo chmod u+s $@

bof.o: bof.c

clean:
	rm bof.o bof
