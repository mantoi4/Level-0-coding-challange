def time_function(val):

    val = int(val)
    hours = int(val / 60)
    min = int(val % 60)
    
    strHr = hours > 1 and ' hours, ' or ' hours, '
    strMin = min > 1 and ' minutes' or ' minutes '
    
    print(str(hours) +  strHr  + str(min) + strMin)
  
time_function(0)

  