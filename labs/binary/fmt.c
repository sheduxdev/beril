#include <stdio.h>
#include <string.h>

static char secret[] = "flag{format_string_leak}";

int main(void) {
    char buf[256];
    if (!fgets(buf, sizeof(buf), stdin)) return 1;
    buf[strcspn(buf, "\n")] = 0;
    printf(buf);
    putchar('\n');
    return 0;
}
