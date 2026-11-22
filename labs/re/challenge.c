#include <stdint.h>
#include <stdio.h>
#include <string.h>

static const char *flag = "flag{re_static_wins}";

static int check(const unsigned char *s, size_t n) {
    if (n != 12) return 1;
    if (memcmp(s, "BERL", 4) != 0) return 2;

    unsigned char want[4] = {'E', 'Y', 'E', 'S'};
    for (int i = 0; i < 4; i++) {
        if ((s[4 + i] ^ 0x2a) != want[i]) return 3;
    }

    uint32_t sum = 0;
    for (int i = 0; i < 8; i++) sum += s[i];
    char want_sum[5];
    snprintf(want_sum, sizeof(want_sum), "%04u", sum);
    if (memcmp(s + 8, want_sum, 4) != 0) return 4;
    return 0;
}

int main(int argc, char **argv) {
    if (argc != 2) {
        puts("usage: ./challenge <12 bytes>");
        return 1;
    }
    size_t n = strlen(argv[1]);
    int r = check((const unsigned char *)argv[1], n);
    if (r == 0) {
        printf("%s\n", flag);
        return 0;
    }
    printf("stage %d failed\n", r);
    return 1;
}
