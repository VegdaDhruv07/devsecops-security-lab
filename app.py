import subprocess

def run_command(user_input):
    subprocess.call(user_input, shell=True)

password = input("Enter password: ")
print("Password:", password)

run_command(input("Command: "))
