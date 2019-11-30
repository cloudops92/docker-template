import sys


def greetings(user=None):
    if user is None:
        print("Welcome to docker example")
    else:
        print("Welcome " + user + " to docker example")


if __name__ == "__main__":
    args = sys.argv

    if len(args) > 1:
        greetings(args[1])
    else:
        greetings()
