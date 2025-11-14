#Simulate OTP/PIN/PASSWORD Verfication System

#actual_otp = 1304
#random module

import random
actual_otp = random.randint(2000,3000)
print(actual_otp)

attempt = 3

while attempt:
    (user_otp) = int(input("Enter otp: "))
    if len(str(user_otp)) !=4:
        print("otp must be 4 digitis only")
    if user_otp ==actual_otp:
        print("Correct otp-transaction success")
        break
    attempt = attempt-1

else:
    print("maximum attempts reached, try after 24 hours")