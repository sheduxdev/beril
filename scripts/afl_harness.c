/* Minimal AFL++ file harness. Replace parse() with the target function.
 * Build: afl-clang-fast -g -O1 harness.c parser.c -o fuzz_target
 * Run:   afl-fuzz -i in -o out -m none -t 1000+ -- ./fuzz_target @@
 */
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

int parse(const uint8_t *data, size_t size);  /* target */

int main(int argc, char **argv) {
    if (argc < 2) return 1;
    FILE *f = fopen(argv[1], "rb");
    if (!f) return 1;
    if (fseek(f, 0, SEEK_END) != 0) return 1;
    long n = ftell(f);
    if (n < 0) return 1;
    rewind(f);
    if (n > 4 * 1024 * 1024) n = 4 * 1024 * 1024;
    uint8_t *buf = malloc((size_t)n ? (size_t)n : 1);
    if (!buf) return 1;
    size_t got = fread(buf, 1, (size_t)n, f);
    fclose(f);
    parse(buf, got);
    free(buf);
    return 0;
}

/* Persistent mode version:
 *
 * __AFL_FUZZ_INIT();
 * int main(void) {
 *   __AFL_INIT();
 *   unsigned char *buf = __AFL_FUZZ_TESTCASE_BUF;
 *   while (__AFL_LOOP(10000)) {
 *     int len = __AFL_FUZZ_TESTCASE_LEN;
 *     parse(buf, len);
 *   }
 *   return 0;
 * }
 */
