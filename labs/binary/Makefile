CC ?= gcc
VULN = -fno-stack-protector -no-pie -z execstack
HARD = -fstack-protector-strong -fPIE -pie -Wl,-z,relro,-z,now

all: stack-vuln stack-hard fmt uaf integer

stack-vuln: stack.c
	$(CC) $(VULN) -o $@ $<

stack-hard: stack.c
	$(CC) $(HARD) -D_FORTIFY_SOURCE=2 -O2 -o $@ $<

fmt: fmt.c
	$(CC) $(VULN) -o $@ $<

uaf: uaf.c
	$(CC) $(VULN) -o $@ $<

integer: integer.c
	$(CC) $(VULN) -o $@ $<

integer-asan: integer.c
	$(CC) -fsanitize=address,undefined -g -O1 -o $@ $<

clean:
	rm -f stack-vuln stack-hard fmt uaf integer integer-asan

.PHONY: all clean
