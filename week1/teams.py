class Teams:
    def __init__(self, members):
        self.__myTeam = members

    def __len__(self):
        return len(self.__myTeam)

    def __contains__(self):
        if 'Tim' or 'Sam' in self.__myTeam:
            return True
        else:
            return False

    def __iter__(self):
        return iter(self.__myTeam)


def main():
    classmates = Teams(['John', 'Steve', 'Tim'])
    print(len(classmates))
    print(classmates.__contains__())


main()
