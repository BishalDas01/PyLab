balance = 500
book = 5

def buy_things(item, cost):
    global balance
    print('balance before buying' , balance) # you can use global variable without use global keywords
   
    balance = balance - cost # but you can't modify without global keyword
    print('balance after buying', balance)

buy_things('watch', 200)

def read_book(number):
    print('before i read books', book)
    book = book - number # it will give you a error❌
    print('after i read book', book)

read_book(2)