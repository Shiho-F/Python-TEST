#課題１
print('hello world')
#課題２
def greet():
    print("こんにちは")
greet()
#課題３
def print_name(name):
    return f"私の名前は{name}です"
message = print_name("しほ")
print(message)
#課題４
def get_greet(greeting):
    return greeting
greeting = get_greet("おはようございます")
print(greeting)

#課題５
def add (a, b):
    return a + b
print(add(2,5))

#課題６
import webbrowser
url = "file:///Users/shiho/.ssh/Python-TEST/example.html"
webbrowser.open_new_tab(url)


    
