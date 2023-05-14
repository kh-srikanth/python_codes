x = input("enter first number: ")
y= input("enter second number: ")
try:
    z = int(x)/int(y)
except ZeroDivisionError as e:
    print('Divide by Zero Exception')
    z = 'INF'
except ValueError as e:
    print('improper data entered')
    z = 'NAN'
except Exception as e:
    print('Exception type: ', type(e).__name__)
    z = 'Unknown'
print("Division is: ", z)




