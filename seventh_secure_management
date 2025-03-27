#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <openssl/sha.h>
#include <openssl/aes.h>

void writeFile(const char *filename, const char *content);
void readFile(const char *filename);
void renameFile(const char *oldname, const char *newname);
void deleteFile(const char *filename);
void hashPassword(const char *password, unsigned char *hash);
void encryptFile(const char *input, const char *output, const unsigned char *key);
void scanFile(const char *filename);

int main() {
    printf("Secure File Management System\n");

    // User Authentication
    unsigned char hash[SHA256_DIGEST_LENGTH];
    hashPassword("securePass123", hash);

    // File Operations
    writeFile("secure.txt", "Sensitive Data");
    readFile("secure.txt");
    renameFile("secure.txt", "data.txt");

    // Encryption
    unsigned char key[16] = "securekey123456";
    encryptFile("data.txt", "encrypted.bin", key);

    // Threat Detection
    scanFile("data.txt");

    // Deletion
    deleteFile("data.txt");

    return 0;
}
