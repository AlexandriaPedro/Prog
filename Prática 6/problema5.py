data = input("")

data = data.split('/')

data = [data[1], data[0], data[2]]

data = '/'.join(data)

print(data)
