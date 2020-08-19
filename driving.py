country = input('請問你是哪國人: ')
age = input('請輸入年齡: ')
age = int(age)
if country == '台灣':
	if age >= 18:
		print('您可以開車')
	else:
		print('您還不能開車')
else:
	print('您的國家不再我們的判別範圍之內。')