from encode import encode, build_abecedary

def run():
    print("Welcome to cipher system:")
    build_abecedary()
    main_loop()
    
def main_loop():
    loop = True
    while(loop):
        print("Do you want to \n'1. CODE', \n'2. DECODE'\n 3. Exit ")
        actionInput = input()
        action : int
        try:
            action = int(actionInput)
        except Exception as e:
            continue
        
        result : str = ""
        if (action == 3):
            loop=False
            print("Thank you for use this system...")
        else:
            input_encode(action)

def input_encode(action: int):
    text = input("\nWrite the secret message: ")
    if(action == 1):
        result = encode(text, 'code')
    elif(action == 2):
        result = encode(text, 'decode')
    else:
        print("Invalid option, try again...")
    print(f"The result is '{result}'")

if __name__ == '__main__':
    run()