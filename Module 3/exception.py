try:
    result = 45 / 0 # there is an error , but the code will not stop here
except:
    print('error happened')
finally: # this is optinal
    print('finally here') 
    
print('Hello World')