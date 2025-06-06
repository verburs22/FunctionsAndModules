#sarah verburg 06-06

def greet(items: list) -> None:
    greeting = "Hello"
    print("ID greeting funct: ", id(greeting))

    def make_greeting(item: str) -> str:
        greeting = "Hi"
        print("ID greeting nested: ", id(greeting))
        return f'{greeting} {item}'

    for item in items:
        print(make_greeting(item))

    print("greeting:", greeting)
    print("ID greeting outside: ", id(greeting))

name = ['Sarah', 'Sam', 'Megan', 'Noah', 'Faith']
greet(name)
