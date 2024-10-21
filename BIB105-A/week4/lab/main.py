from random import randint
secret_number = randint(1,100)
max_guess = 5
guess_count = 0


while guess_count < max_guess:
    guess = int(input("Sayıyı giriniz: \t"))
    if guess == secret_number:
        print(f"Doğru, gizli sayı: {secret_number}")
        break
    elif guess < secret_number:
        print("Tahmin çok küçük")
    else:
        print("Tahmin çok büyük")

    guess_count += 1

if guess != secret_number:
    print("Kaybettiniz")
