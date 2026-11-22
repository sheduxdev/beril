#include <stdio.h>
#include <string.h>

void win(void) {
    puts("flag{stack_overflow_101}");
}

void greet(char *name) {
    char buf[64];
    strcpy(buf, name);
    printf("hello %s\n", buf);
}

int main(int argc, char **argv) {
    char input[512] = {0};
    if (argc > 1) {
        snprintf(input, sizeof(input), "%s", argv[1]);
    } else {
        if (!fgets(input, sizeof(input), stdin)) return 1;
        input[strcspn(input, "\n")] = 0;
    }
    greet(input);
    return 0;
}
