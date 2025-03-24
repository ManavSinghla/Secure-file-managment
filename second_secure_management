#include <stdio.h>
#include <string.h>
#include <openssl/sha.h>

void hashPassword(const char *password, unsigned char *hash) {
    SHA256((const unsigned char*)password, strlen(password), hash);
}

void registerUser() {
    char username[50], password[50];
    unsigned char hash[SHA256_DIGEST_LENGTH];

    printf("Enter username: ");
    scanf("%s", username);
    printf("Enter password: ");
    scanf("%s", password);

    hashPassword(password, hash);
    FILE *file = fopen("users.db", "a");
    fprintf(file, "%s ", username);
    for (int i = 0; i < SHA256_DIGEST_LENGTH; i++)
        fprintf(file, "%02x", hash[i]);
    fprintf(file, "\n");
    fclose(file);
    printf("User registered successfully!\n");
}

int main() {
    registerUser();
    return 0;
}
