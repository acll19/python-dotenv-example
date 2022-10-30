import os
from dotenv import load_dotenv


def main():
    load_dotenv()
    print(os.getenv('MY_SECRET'))


if __name__ == '__main__':
    main()