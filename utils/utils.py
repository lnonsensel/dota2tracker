import os
import glob


def clear_parsed_folder() -> None:
    files = glob.glob('./protracker/*.html')
    for file in files:
        os.remove(file)

if __name__ == '__main__':
    clear_parsed_folder()