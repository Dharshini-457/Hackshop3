def check():
    try:
        num=int(input("ENTER A VALUE:"))
        num1=int(input("Enter a value:"))
        print(f"Result {num&num1}")
    except(ValueError):
        print("enter a number")
    except(TypeError):
        print("enter a integer type")

def kill():
    num=1
    while (num<10):
        print(num)
