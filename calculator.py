import argparse
import csv
import sys
import pyperclip
import os

def args():
    parser = argparse.ArgumentParser(description = 'get command')
    parser.add_argument('--get', required=False, default="none", help='get')
    return parser.parse_args()

def authentication(a):
    if a == 'you shall not pass!':
        return "\n"
    else:
        sys.exit()
    return ""

def read(a):
    with open('times_tables.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for line in csv_reader:
            if line[0].upper()==a.upper():
                if len(line)>2:
                    print(f"{line[0]}\nパスワード: {line[1]}\nユーザー: {line[2]}")
                    pyperclip.copy(line[1])
                else:
                    print(f"{line[0]}\nパスワード: {line[1]}")
                    pyperclip.copy(line[1])

def main():
    os.system('cls')
    prompt = str(input("いらしゃいませ。パスワードお願いします。\n"))
    print(authentication(prompt))
    os.system('cls')
    command = args()

    if command.get:
        read(command.get)

    x = 0
    while x<16:
        print("\n")
        x+=1
                         
if __name__ == "__main__":
    main()