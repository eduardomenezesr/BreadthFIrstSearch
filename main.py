import searches


# Main menu where the user can choose between BreadthFirstSearch, A* and exit the program
def main():
    choice = None
    choice = input('Select your option: 1-BreadthFirstSearch; 2-A*; c-exit: ')
    while(choice != 'c'):
        file = input("What's the file's name? ")
        if (choice == '1'):
            searches.BreadthFirstSearch(file)
        elif (choice == '2'):
            searches.A_star(file)
        choice = input('Select one option: 1-BreadthFirstSearch; 2-A*; c-exit: ')


if __name__ == '__main__':
    main()
