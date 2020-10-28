TWD = 1
USD = 0.03475
JPY = 3.61805
CNY = 0.23339

def currencyConverter():
    choseCurrency = input("輸入新台幣轉換：\n1)USD \n2)JPY \n3)CNY\n")
    print(('--'*36) + '\n')
    print(choseCurrency, "\n" + ('--'*36))

    #USD
    if(choseCurrency) == '1':
        result = round(float(input("輸入轉換為美金的金額：\n")))
        print(('--' * 36) + '\n')
        print(result, 'TWD is ', round(result) * 0.03475, 'USD \n' + ('--'*36) + '\n')

    #JPY
    elif (choseCurrency) == '2':
        result = round(float(input("輸入轉換為日幣的金額：\n")))
        print(('--' * 36) + '\n')
        print(result, 'TWD is ', round(result) * 3.61805, 'JPY \n' + ('--'*36) + '\n')

    #CNY
    elif (choseCurrency) == '3':
        result = round(float(input("輸入轉換為人民幣的金額：\n")))
        print(('--' * 36) + '\n')
        print(result, 'TWD is ', round(result) * 0.23339, 'CNY \n' + ('--'*36) + '\n')
    else:
        print('錯誤的輸入，請輸入 1)美金 2)日幣 3)人民幣')
currencyConverter()