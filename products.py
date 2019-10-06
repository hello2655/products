import os # operating system


#讀取檔案
def read_file(filename):
	products = []
	with open(filename, 'r' , encoding='utf-8') as f:
		for line in f:
			if '品名, 價格' in line:
				#print('有進去呦～')
				continue#繼續
			name, price = line.strip().split(',')
			products.append([name, price])
	print(products)
	return products

#使用者輸入區段
def user_input(products):
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
	return products

#印出所有購買紀錄
def print_products(products):
	for p in products:
		#print(p)
		#print(p[0])
		print(p[0] , '的價格為' , p[1])

#寫入檔案
def write_file(filename, products):
	with open('filename', 'w', encoding='utf-8') as f:
		f.write('品名, 價格\n')
		for p in products:
			f.write(p[0] + ',' + p[1] + '\n')


def main():
	filename = 'products.csv'
	if os.path.isfile(filename):#檢查檔案
		print('yeah! 找到檔案了')
		products = read_file(filename)
	else:
		print('找不到舊資料，將建立新檔案')

	products = user_input(products)
	print_products(products)
	write_file('products.csv', products)

main()




#data = [1, 3, 5, 7, 9] # 清單中裝著一些整數
# 請開始寫"寫入檔案"的程式碼
#with open('test.txt', 'w') as f1:
	#for d in data:
		#d = str(d)
		#f1.write(d + '\n')