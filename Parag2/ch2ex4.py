#うるう年
print("西暦を入力してください")
x = int(input())
if (x%4==0 and x%100!=0) or (x%400==0):
    print("うるう年")
else:
    print("うるう年ではありません")