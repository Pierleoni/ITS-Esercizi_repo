from my_project.weather import check_weather()
# passed
# def test_check_weather1():
# 	assert check_weather(21.00) == "hot", "temperatures greater than 20 degree must be considered as "

def test_check_weather2():
	assert check_weather(5.00) == "average", 'temperatures between 10 and 20 degree \
must be considered as average temperature'