import random
n = random.randint(1,100)
guess = int(input("輸入數字1到100："))
l = "1"
h = "100"
while n != 'guess':
    if guess < n:
        l = str(guess)
        print(("-"*36)+'\n猜高一點')
        guess = int(input("輸入數字"+ l + "到"+h+"："))

    elif guess > n:
        h = str(guess)
        print(("-"*36)+'\n猜低一點')
        guess = int(input("輸入數字"+l+"到"+ h + "："))
    else:
        print("你猜到了")
        break
