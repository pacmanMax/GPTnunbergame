import random

def guess_the_number_game():
    # 生成一個 1 到 100 的隨機數字
    target_number = random.randint(1, 100)
    
    print("歡迎來到猜數字小遊戲！我們生成了一個 1 到 100 的數字，你來猜吧！")

    attempts = 0
    
    while True:
        # 讓玩家輸入猜測的數字
        try:
            guess = int(input("請輸入你的猜測（1到100之間的整數）: "))
        except ValueError:
            print("請輸入有效的整數！")
            continue
        
        # 更新猜測次數
        attempts += 1
        
        # 檢查猜測是否正確
        if guess == target_number:
            print(f"恭喜你！你在第 {attempts} 次猜中了數字 {target_number}。")
            break
        elif guess < target_number:
            print("太小了，再試一次！")
        else:
            print("太大了，再試一次！")

# 啟動遊戲
guess_the_number_game()
