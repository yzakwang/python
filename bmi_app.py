def bmi_app():
	height = input('How tall are you? ')
	weight = input('How much do you weight? ')
	bmi_val = int(weight)/(int(height)/100)**2
	print('Your bmi is {}'.format(round(bmi_val, 2)))
	if bmi_val < 18.5:
		print('You\'d better eat more!')
	elif bmi_val >= 18.5 and bmi_val <= 24:
		print('Good job!')
	else:
		print('You\'d better take some exercises')

bmi_app()
