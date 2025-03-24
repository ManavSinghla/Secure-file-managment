#include <stdio.h>
#include <stdlib.h>

void writeFile(const char *filename, const char *content) {
    FILE *file = fopen(filename, "w");
    if (file == NULL) {
        printf("Error opening file!\n");
        return;
    }
    fprintf(file, "%s", content);
    fclose(file);
    printf("File written successfully.\n");
}

void readFile(const char *filename) {
    FILE *file = fopen(filename, "r");
    if (file == NULL) {
        printf("File not found!\n");
        return;
    }
    char ch;
    while ((ch = fgetc(file)) != EOF)
        putchar(ch);
    fclose(file);
}

void renameFile(const char *oldname, const char *newname) {
    if (rename(oldname, newname) == 0)
        printf("File renamed successfully.\n");
    else
        printf("Error renaming file!\n");
}

void deleteFile(const char *filename) {
    if (remove(filename) == 0)
        printf("File deleted successfully.\n");
    else
        printf("Error deleting file!\n");
}

int main() {
    writeFile("example.txt", "Secure File Management System");
    readFile("example.txt");
    renameFile("example.txt", "secure_file.txt");
    deleteFile("secure_file.txt");
    return 0;
}
