def time_function():

    val = int(input('Enter user input: '))
    hours = int(val / 60)
    minutes = int(val % 60)
    
    print(str(hours) + ' hours, ' + str(minutes) + ' minutes')
  
time_function()

