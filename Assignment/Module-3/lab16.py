# Write a Python program to demonstrate the use of local and global variables in a class.

msg = "This is global variable..."

class temp:

    def demo(self):

        msg = "This is local variable..."
        print("Message ::",msg)

    def global_demo(self):

        global msg
        print("Message ::",msg)

obj = temp()

obj.demo()
obj.global_demo()