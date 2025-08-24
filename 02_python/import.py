import random

# 產生 1-100 的隨機數字
target = random.randint(1, 100)
guess_count = 0
max_tries = 7

print("歡迎來到猜數字遊戲！")
print(f"你有 {max_tries} 次機會猜一個 1-100 的數字")

while guess_count < max_tries:
    try:
        # 取得玩家輸入
        guess = int(input(f"\n還剩 {max_tries - guess_count} 次機會，請猜一個數字: "))
        guess_count += 1
        
        # 檢查猜測結果
        if guess < target:
            print("太小了！")
        elif guess > target:
            print("太大了！")
        else:
            print(f"\n恭喜你猜對了！答案就是 {target}")
            print(f"你總共猜了 {guess_count} 次")
            break
            
    except ValueError:
        print("請輸入有效的數字！")
        guess_count -= 1

if guess_count >= max_tries and guess != target:
    print(f"\n遊戲結束！正確答案是 {target}")