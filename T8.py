def time_function(val):

    val = int(val)
    hours = int(val / 60)
    min = int(val % 60)
    
    strHr = hours > 1 and ' hours, ' or ' hour, '
    strMin = min > 1 and ' minutes' or ' minute '
    
    print(str(hours) +  strHr  + str(min) + strMin)
  
time_function(99)

  