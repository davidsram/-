def convert_min(min):
    hour,min=divmod(min,60)
    print('%s hour %s minutes'%(hour,min))

convert_min(123)