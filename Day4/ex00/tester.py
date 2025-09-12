from S1E9 import Stark
# from S1E9 import Character


def main():
    """Main to test character & stark classes
    """
    Ned = Stark("Ned")
    print(Ned.__dict__)
    print(Ned.is_alive)
    Ned.die()
    print(Ned.is_alive)
    print(Ned.__doc__)
    print(Ned.__init__.__doc__)
    print(Ned.die.__doc__)
    print("---")
    Lyanna = Stark("Lyanna", False)
    print(Lyanna.__dict__)
    # try:
    #     hodor = Character("hodor") # To show you can't instanciate character
    # except Exception as e:
    #     print(f"{Exception.__name__}: {e}")


if __name__ == "__main__":
    main()
