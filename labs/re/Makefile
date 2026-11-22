CC ?= gcc
CFLAGS = -O0 -g -fno-stack-protector -no-pie

all: challenge

challenge: challenge.c
	$(CC) $(CFLAGS) -o $@ $<
	strip $@

clean:
	rm -f challenge

.PHONY: all clean
