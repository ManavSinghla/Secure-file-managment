#include <stdio.h>
#include <string.h>

typedef struct {
    char username[50];
    char role[10];
} User;

void checkAccess(User user, const char *operation) {
    if (strcmp(user.role, "admin") == 0 || (strcmp(user.role, "user") == 0 && strcmp(operation, "read") == 0))
        printf("Access granted for %s\n", operation);
    else
        printf("Access denied for %s\n", operation);
}

int main() {
    User user = {"Alice", "user"};
    checkAccess(user, "delete");
    return 0;
}
