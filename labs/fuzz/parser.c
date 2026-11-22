#include <stdint.h>
#include <string.h>

int parse(const uint8_t *data, size_t size) {
    if (size < 6) return 0;
    if (memcmp(data, "BFZ1", 4) != 0) return 0;

    unsigned int len = data[4] | (data[5] << 8);
    char buf[64];
    memset(buf, 0, sizeof(buf));
    if (size - 6 < len) return 0;

    memcpy(buf, data + 6, len);  /* no bound check against 64 */
    return buf[0];
}
