#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef void (*callback)(void);

struct object {
    callback cb;
    char name[24];
};

void win(void) {
    puts("flag{use_after_free_101}");
}

void hello(void) {
    puts("hello");
}

int main(void) {
    struct object *obj = malloc(sizeof(struct object));
    if (!obj) return 1;
    obj->cb = hello;
    strcpy(obj->name, "original");
    printf("before: ");
    obj->cb();

    free(obj);

    struct object *replacement = malloc(sizeof(struct object));
    if (!replacement) return 1;
    memset(replacement, 0, sizeof(struct object));
    printf("send 32 bytes: ");
    fflush(stdout);
    if (fread(replacement, 1, sizeof(struct object), stdin) < 8) return 1;

    printf("after: ");
    fflush(stdout);
    obj->cb();  /* stale pointer */
    return 0;
}
