import searches


# Main menu where the user can choose between BreadthFirstSearch, A* and exit the program
def main():
    choice = None
    print('==================================================================')
    choice = input('Select your option: 1-Breadth First Search; 2-A* Search; c-exit: ')
    while(choice != 'c' and (choice == '1' or choice == '2')):
        file = input("What's the file's name? ")
        if (choice == '1'):
            searches.BreadthFirstSearch(file)
            choice = 'c'
        elif (choice == '2'):
            searches.A_star(file)
            choice = 'c'
        print('==================================================================')
        choice = input('Select your option: 1-Breadth First Search; 2-A* Search; c-exit: ')

    print('==================================================================')
    print('(^ _ ^)/')
    print('Goodbye!!!')


if __name__ == '__main__':
    main()
