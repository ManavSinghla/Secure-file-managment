#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int generateOTP() {
    srand(time(NULL));
    return rand() % 900000 + 100000;  // 6-digit OTP
}

int main() {
    int otp = generateOTP();
    printf("Your OTP is: %d\n", otp);
    
    int userOTP;
    printf("Enter OTP: ");
    scanf("%d", &userOTP);

    if (userOTP == otp)
        printf("Authentication successful!\n");
    else
        printf("Invalid OTP!\n");
    
    return 0;
}
