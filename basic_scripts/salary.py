def salaryCal(hours_worked, hourly_rate):

	if hours_worked <= 40:
		salary = hourly_rate * hours
		print(salary)
	elif hours_worked > 40:
		over_time = hours_worked - 40
		salary = (hourly_rate*40) + (hourly_rate*1.5*over_time)
		print(salary)
	else:
		print("Error your entry is invalid")