CC = clang
CFLAGS ?= -g -O1 -fsanitize=fuzzer,address,undefined

all: fuzz

fuzz: fuzz.c parser.c
	$(CC) $(CFLAGS) -o $@ $^

run: fuzz
	./fuzz corpus -max_total_time=60 -artifact_prefix=artifacts/ -max_len=512

clean:
	rm -rf fuzz artifacts crash-* leak-* timeout-*

.PHONY: all run clean
