def isEven(value):
	"""Первая реализация от вакансии:
		Лакончино по делу, ничего лишнего,
		но если в конечном итоге выполняет
		функцию необходимым образом, делает
		это по сранению остатка с нулем,
		что выглядит не совсем красиво
	"""
	return value % 2 == 0

def Is_Even(num):
	"""
	Данный пример делает исключительно
	то что должен делать,
	проверяет число на четность,
	Он хоть и может вызвать путаницу, но
	проверяет само выражение на истинность"""
	if num%2 or num == 0:
		print("Нечетное число")
		return 
	print("Четное число")

def main(x):
	Is_Even(x)
if __name__ == '__main__':
	Number = 0
	main(Number)