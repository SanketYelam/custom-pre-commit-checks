import subprocess

expectedUserName = "Sanket Yelam"

userName = subprocess.run(["git", "config", "user.name"], capture_output=True, text=True).stdout.strip()

if userName == expectedUserName:

        print("You are using user name as per configuration, proceeding to commit")
        exit(0)

else:
        print(f"Configured user name is not as per config. It should be {expectedUserName}")
        exit(1)

