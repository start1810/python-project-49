import random
from .. import cli
from .. import game_progression





def main():
    user_name = cli.welcome_user()
    game_points = 0
    game_status = True
    while game_status == True:
        game_status = game_progression.game()
        game_points +=1
        if game_points == 3:
            print(f"Congratulations, {user_name}!")
            return
    print(f"Let's try again, {user_name}!")


if __name__ == "__main__":
    main()