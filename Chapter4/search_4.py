data = [
    ["佐藤", "000-0000-0000"],
    ["鈴木", "111-1111-1111"],
    ["高橋", "222-2222-2222"],
    ["田中", "333-3333-3333"],
    ["島袋", "444-4444-4444"],
    [None]
]
n = len(data)
s = input("検索する相手の苗字は? ")
i = 0
while i < n and data[i][0] != s:
    i += 1
if i == n:
    print("その名は登録されていません")
else:
    print(data[i][0]+"さんの番号は "+data[i][1]+"です")