# Write a Python program to write multiple strings into a file.

import os 

os.chdir("Text_Data")

x = open("my_file2.txt", "w")

my_str = [
            "The sun sets behind the mountains.\n",
            "Python is fun and powerful.\n",
            "Artificial Intelligence shapes the future.\n",
            "Books open doors to new worlds.\n",
            "Clouds drift slowly across the sky.\n",
            "Hard work beats talent every time.\n",
            "Music connects hearts across cultures.\n",
            "A gentle breeze makes the trees dance.\n"
         ]

# x.writelines(my_str)

for i in my_str:
    x.write(i + "\n")

print("Data Print Successfully....!!")

