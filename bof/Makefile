CC=gcc
#CFLAGS=-m32 -std=c99 -Wall -fno-stack-protector	# for x64
CFLAGS=-std=c99 -Wall -fno-stack-protector -z execstack

all: bof

bof: bof.o
	$(CC) $(CFLAGS) -o $@ $^
	sudo chown 0:0 $@
	sudo chmod u+s $@

bof.o: bof.c

clean:
	rm bof.o bof
