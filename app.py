import subprocess

def run_command(user_input):
    subprocess.run(
        user_input.split(),
        check=True
    )

password = input("Enter password: ")
print("Password received.")

run_command(input("Command: "))
