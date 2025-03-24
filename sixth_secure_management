#include <stdio.h>
#include <string.h>

void scanFile(const char *filename) {
    FILE *file = fopen(filename, "r");
    if (!file) {
        printf("File not found!\n");
        return;
    }

    char buffer[256];
    while (fgets(buffer, sizeof(buffer), file)) {
        if (strstr(buffer, "malware") || strstr(buffer, "virus"))
            printf("Threat detected!\n");
    }
    fclose(file);
}

int main() {
    scanFile("example.txt");
    return 0;
}
