def add_time(start, duration, day_of_week=''):
	day_of_week = day_of_week.lower()
	days_of_week = {
		0: 'Monday', 
		1: 'Tuesday', 
		2: 'Wednesday', 
		3: 'Thursday', 
		4: 'Friday', 
		5: 'Saturday', 
		6: 'Sunday'
	}

	convert_to_twenty_four_hours = twelve_to_twenty_four_hours(start)

	duration = list(map(int, duration.split(':'))) # ['0', '00']
	
	hours_and_minutes = calc_minutes(convert_to_twenty_four_hours[1], duration[1]) # return [0, 00]
	days_and_hours = calc_hours(convert_to_twenty_four_hours[0], duration[0], hours_and_minutes[0])

	convert_to_twelve_hours = twenty_four_to_twelve_hours(days_and_hours[1])

	days = days_and_hours[0]
	hours = convert_to_twelve_hours[0]
	minutes = hours_and_minutes[1]
	am_pm = convert_to_twelve_hours[1]

	if days >= 2:
		next_day = f'({days} days later)'
	elif days >= 1:
		next_day = f'(next day)'
	else:
		next_day = f''

	if day_of_week != '':
		amount_days_of_week = [i for i in days_of_week if days_of_week[i] == day_of_week.capitalize()]
		amount_days_of_week = amount_days_of_week[0] + days
		day_of_week = days_of_week[amount_days_of_week % 7]
		time = [hours, minutes, am_pm, day_of_week, next_day]
		new_time = f'{time[0]}:{str(time[1]).zfill(2)} {time[2]}, {time[3]} {time[4]}'.strip()
	else:
		time = [hours, minutes, am_pm, next_day]
		new_time = f'{time[0]}:{str(time[1]).zfill(2)} {time[2]} {time[3]}'.strip()
	return new_time


def calc_minutes(a, b):
	""" Recive two values in minutes, and return a list with hours and minutes [0:00]"""
	amount_of_minutes = int(a) + int(b)
	hours = 0
	if amount_of_minutes > 59:
		hours = amount_of_minutes // 60 # 60 min is one hour
		minutes = amount_of_minutes % 60
		return [hours, minutes]
	else:
		minutes = amount_of_minutes
		return [hours, minutes]

def calc_hours(start_hour, add_hour, minutes_hour):
	"""Recive three values, first hour, hour to add, and hour calculate with minutes\nReturn days and hours"""
	amount_of_hours = int(start_hour) + int(add_hour) + int(minutes_hour)
	hours = 0
	days = 0
	
	if amount_of_hours < 24:
		hours = amount_of_hours
	else:
		days += amount_of_hours // 24
		hours += amount_of_hours % 24
	return [days, hours]

def twelve_to_twenty_four_hours(time):
	"""Receive a time 00:00 AM/PM and convert standard 12 hour format to military time"""
	time = time.split() # ['00:00', 'AMPM']
	time_without_AMPM = list(map(int, time[0].split(':'))) # ['00', '00']
	if time[1] == 'PM':
		time_without_AMPM[0] += 12
		time = time_without_AMPM
	else:
		time = time_without_AMPM
	return time

def twenty_four_to_twelve_hours(time):
	if time > 12:
		time = [time - 12, 'PM']
	elif time == 12:
		time = [time, 'PM']
	elif time == 0:
		time = [time + 12, 'AM']
	else:
		time = [time, 'AM']
	return time