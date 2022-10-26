def palindromo(w):
	t_w = len(w)
	m = int(t_w / 2)

	for i in range(m):
		if w[i] != w[t_w - i - 1]:
			return False
		i = i + 1
	return True

w = input('')

if palindromo(w):
	print('É palíndromo')
else:
	print('Não é palíndromo')
