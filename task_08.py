def time_function(val):

    hour = val // 60
    min = val % 60
    
    h = 'hour'
    m = 'minute'

    
    if hour == 1:
        h = 'hour'

    else:
        h = 'hours'

    if min == 1:
        m = 'minute'

    else:
        m = 'minutes'


    print(f'{hour} {h}, {min} {m}')



time_function(0)

  