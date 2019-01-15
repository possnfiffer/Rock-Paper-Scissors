def print_header():
    print("--------------------------------------")
    print("      ROCK, PAPER, SCISSORS APP")
    print("--------------------------------------")
    print()


def get_players_name():
    name = input("What is your name my friend? ")


class Player:
    def __init__(self, name):
        self.name = name


def main():
    print_header()
    name = get_players_name()
    print(
        "Hello",
        name,
        "Please bear with me as I build up this app to make it more useful! -The Developer",
    )


if __name__ == "__main__":
    main()
