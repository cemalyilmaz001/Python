def asal_(sayi, boolen):
	if (sayi <= 2):
		return sayi == 2

	if (sayi % boolen == 0):
		return False

	if (boolen * boolen > sayi):
		return True

	return asal_(sayi, boolen + 1)


print(asal_(16,2))