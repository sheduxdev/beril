#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char **argv) {
    uint32_t count = argc > 1 ? (uint32_t)strtoul(argv[1], NULL, 10) : 65536;
    uint32_t size = argc > 2 ? (uint32_t)strtoul(argv[2], NULL, 10) : 65536;
    uint32_t total = count * size;  /* wraps to 0 for 65536 * 65536 */
    printf("count=%u size=%u total=%u\n", count, size, total);

    unsigned char *buf = malloc(total ? total : 1);
    if (!buf) return 1;
    size_t got = fread(buf, 1, 4096, stdin);
    printf("read %zu bytes into %u\n", got, total);
    free(buf);
    return 0;
}
