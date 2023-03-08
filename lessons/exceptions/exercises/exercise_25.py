def weird_number(num):

    if not isinstance(num,( int,float,str)):
        raise TypeError("this function only accepts integers, floats and strings.")

    try:
        num=float(num)
        num=num**3
    except:
        num=0
    finally:
        num+=1

    return num
