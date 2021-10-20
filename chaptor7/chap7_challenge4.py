numbers = [1, 2, 3, 4, 5]

while True:
    answer = input("数字を入力するか、’q’で終了します: ")
    if answer == "q":
        break
    try:
        answer = int(answer)
    except ValueError:
        print("数字を入力するか、’q’で終了します")
    if answer in numbers:
        print("正解")
    else:
        print("不正解")
        
