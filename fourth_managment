#include <stdio.h>
#include <string.h>
#include <openssl/aes.h>

void encryptFile(const char *input, const char *output, const unsigned char *key) {
    FILE *in = fopen(input, "rb");
    FILE *out = fopen(output, "wb");
    AES_KEY encryptKey;
    AES_set_encrypt_key(key, 128, &encryptKey);

    unsigned char buffer[AES_BLOCK_SIZE];
    while (fread(buffer, 1, AES_BLOCK_SIZE, in))
        AES_encrypt(buffer, buffer, &encryptKey), fwrite(buffer, 1, AES_BLOCK_SIZE, out);

    fclose(in);
    fclose(out);
}

int main() {
    unsigned char key[16] = "securekey123456"; 
    encryptFile("example.txt", "encrypted.bin", key);
    return 0;
}
