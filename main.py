import database

# Main method
if __name__ == "__main__":
    allGamesList = database.get_game_names()
    print(allGamesList)