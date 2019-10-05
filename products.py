import os # operating system

products = []
if os.path.isfile('products.csv'):#檢查檔案
	print('yeah! 找到檔案了')
	#讀取檔案
	with open('products.csv', 'r' , encoding='utf-8') as f:
		for line in f:
			if '品名, 價格' in line:
				#print('有進去呦～')
				continue#繼續
			name, price = line.strip().split(',')
			products.append([name, price])
	print(products)

else:
	print('找不到舊資料，將建立新檔案')

#使用者輸入區段
while  True:
	name = input('請輸入商品名稱：')
	if name == 'q':
		break
	price = input('請輸入商品價格：')
	#p =[]
	#p.append(name)
	#p.append(price)
	products.append([name , price])
print(products)

#印出所有購買紀錄
for p in products:
	#print(p)
	#print(p[0])
	print(p[0] , '的價格為' , p[1])

#寫入檔案
with open('products.csv', 'w', encoding='utf-8') as f:
	f.write('品名, 價格\n')
	for p in products:
		f.write(p[0] + ',' + p[1] + '\n')





#data = [1, 3, 5, 7, 9] # 清單中裝著一些整數
# 請開始寫"寫入檔案"的程式碼
#with open('test.txt', 'w') as f1:
	#for d in data:
		#d = str(d)
		#f1.write(d + '\n')