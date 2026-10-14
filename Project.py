import math 
history = []
print("Welcome to Calculated (Press close to exit)")

while True :
    user = input("Enter your question : ").lower()
    if user == "close" : #关闭程序
        print("Thanks for use our intelligent calculator!! Hope i can see you soon.")
        print("Program is closed !!")
        break
    elif user == "bye":
        print("Goodbye! Have a great day!")
        break

# Chatbot
    if user == "" :
        print("Error : Please enter something !")
    elif user == "hi" :
        print("HI im your intelligent calculator.")
        continue
    elif user == "help" or user == "what can you do":
        print("I can solve math problems like +, -, *, /, ^, √, ! and more!")
        continue
    elif user == "who are you":
        print("I am your smart calculator powered by Python and NLP.")
        continue
    elif user == "how to use you":
        print("Just type any math question, like 5 + 3 or √16, and I'll answer it.")
        continue
    elif user == "thank you":
        print("You're welcome! Let me know if you have more questions.")
        continue
    elif user == "tell me a joke":
        print("Why was the math book sad? Because it had too many problems!")
        continue

# Caluculation
    words = user.split()
    corrected = []
    for v in words:
        if v in ("pls", "plsu", "plu", "pus", "pul", "lus", "pusl", "pluz", "pluss"):
            print("Did you mean 'plus'? I replaced it with 'plus'")
            corrected.append("plus")
        if v in ("divd", "divs", "dvd", "dvide", "divie", "devide"):
            print("Did you mean 'divide'? I replaced it with 'divide'")
            corrected.append("divide")
        if v in ("mlt", "mlpy", "multy", "mult", "multyply", "mutiply", "mutlpy"):
            print("Did you mean 'multiply'? I replaced it with 'multiply'")
            corrected.append("multiply")
        if v in ("subb", "subs", "sab", "sbu", "substract", "minuz", "minas"):
            print("Did you mean 'subtract'? I replaced it with 'minus'")
            corrected.append("minus")
        if v in ("sqrroot", "sqr", "squareroot", "sqroot", "sqr rot", "squaroot"):
            print("Did you mean 'square root'? I replaced it with 'square root'")
            corrected.append("square root")
        else:
            corrected.append(v)

    user = " ".join(corrected)
    user = user.replace("divide", "div").replace("div","/").replace("/", "÷") 
    user = user.replace("multiply", "times").replace("times","mul").replace("mul", "*") 
    user = user.replace("sub", "minus").replace("minus","-") 
    user = user.replace("plus", "add").replace("add","+") 
    user = user.replace("square root", "sqrt").replace("sqrt","√") 
    user = user.replace("power", "exp").replace("exp", "**").replace("**","^") 
    user = user.replace("percent", "%") 
    user = user.replace("factorial", "!") 

    value = user.split()

    # 计算题目
    total = 0
    operation = ""
    operation_name = ["+", "-", "÷", "*", "^", "√", "%", "!", "(", ")"]

    new_value = []
    for v in value:
        if "." in v or "-" in v or v.isdigit() or v in operation_name:
            new_value.append(v)

    show_value = []
    show_value.extend(new_value)
    
    # 括号
    while "(" in new_value and ")" in new_value:
        idx = new_value.index("(")
        num1 = new_value[idx+1]
        op = new_value[idx+2]
        num2 = new_value[idx+3]

        if op in ["√", "!"]:
            if op == "√":
                result = math.sqrt(float(num1))
            elif op == "!":
                result = math.factorial(int(num1))
            new_value[idx:idx+3] = [str(result)]
        else:
            if op == "*":
                result = float(num1) * float(num2)
            elif op == "÷":
                result = float(num1) / float(num2)
            elif op == "^":
                result = float(num1) ** float(num2)
            elif op == "%":
                result = float(num1) * float(num2) / 100
            elif op == "+":
                result = float(num1) + float(num2)
            elif op == "-":
                result = float(num1) - float(num2)
            new_value[idx:idx+5] = [str(result)]

        if ")" in new_value:
            new_value.remove(")")

    # √
    try :
        while "√" in new_value:
            idx = new_value.index("√")
            num1 = new_value[idx+1]
            result = math.sqrt(float(num1))
            new_value[idx:idx+2] = [str(result)]
    except Exception :
        print("Error : Cannot square root not a number !!")
        continue

    # !
    try :
        while "!" in new_value :
            idx = new_value.index("!")

            num1 = new_value[idx-1]
            result = math.factorial(int(num1))
            num = result

            new_value[idx-1:idx+1] = [str(num)]
    except Exception :
        print("Error : Factorials can only be used for non-negative integers !!!")
        continue

    # ^
    try :
        while "^" in new_value :
            idx = new_value.index("^")

            num1 = new_value[idx-1]
            num2 = new_value[idx+1]
            result = float(num1) ** float(num2)
            num = result

            new_value[idx-1:idx+2] = [str(num)]
    except Exception :
        print("Error: Invalid input, please enter valid numbers and operators !!!")

    # *
    while "*" in new_value :
        idx = new_value.index("*")

        num1 = new_value[idx-1]
        num2 = new_value[idx+1]
        result = float(num1) * float(num2)
        num = result

        new_value[idx-1:idx+2] = [str(num)]

    # ÷
    try :
        while "÷" in new_value :
            idx = new_value.index("÷")

            num1 = new_value[idx-1]
            num2 = new_value[idx+1]
            result = float(num1) / float(num2)
            num = result

            new_value[idx-1:idx+2] = [str(num)]
    except Exception as error :
        print("Error : Cannot divide by zero !!!!") 
        continue

    # %
    while "%" in new_value :
        idx = new_value.index("%")

        num1 = new_value[idx-1]
        num2 = new_value[idx+1]
        result = (float(num1) / 100) * float(num2)
        num = result

        new_value[idx-1:idx+2] = [str(num)]

    # 最终加减
    for Value in new_value:
        if Value in operation_name:
            operation = Value
        else:
            num = float(Value)
            if total == 0:
                total = num
            elif operation == "+":
                total += num
            elif operation == "-":
                total -= num

    # 显示结果
    his = " ".join(show_value)
    History = his + " = " + str(round(total, 2))
    history.append(History)
    if user == "history":
        history.pop()
        print(history)
        continue

    show_value = " ".join(show_value)
    print(show_value , " = ", round(total, 2))
