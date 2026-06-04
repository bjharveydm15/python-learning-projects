import random

def roll_dice(current_player, player_scores):
    turn_score = 0
    rolled_6 = 0
    print(f"Player {current_player}'s turn")

    while True:
        roll_outcome = random.randint(1, 6)

        if roll_outcome == 1:
            score_text = ', '.join(
                f'Player {i}: {score}'
                for i, score in enumerate(player_scores, start=1)
            )

            print('\nYou rolled a 1. You will get 0 points this turn.')
            print(f'Current scores: {score_text}\n')

            return

        elif roll_outcome == 6:
            rolled_6 += 1

            if rolled_6 != 2:
                print(f'You rolled a {roll_outcome}')
                turn_score += roll_outcome
        else:
            print(f'You rolled a {roll_outcome}')
            turn_score += roll_outcome
            rolled_6 = 0

        if rolled_6 == 2:
            player_scores[current_player - 1] = 0

            score_text = ', '.join(
                f'Player {i}: {score}'
                for i, score in enumerate(player_scores, start=1)
            )

            print('\nYou rolled a 6 twice in a row. Your accumulated score will reset to 0')
            print(f'Current scores: {score_text}\n')

            return

        while True:
            will_roll = input('Roll again? (y/n): ').lower()

            if will_roll not in ('y', 'n'):
                print('Please choose y or n only.')
                continue

            break

        if will_roll == 'y':
            continue
        elif will_roll == 'n':
            player_scores[current_player - 1] += turn_score

            score_text = ', '.join(
                f'Player {i}: {score}'
                for i, score in enumerate(player_scores, start=1)
            )

            print(f'\nYou scored {turn_score} points this turn.')
            print(f'Current scores: {score_text}\n')

            return

def check_win(current_player, player_scores, target_score, player_points):
    winner_score = player_scores[current_player - 1]
    player_point = player_points[current_player - 1]

    if winner_score >= target_score:
        print(f'\nPlayer {current_player} got a score of {winner_score} '
              + f'which is greater than or equal to {target_score}.')
        print(f'Player {current_player} wins the game!')

        player_points[current_player - 1] += 1

        return True

    return False

def customize_game():
    while True:
        try:
            player_number = int(input('Please set the number of players: '))
        except ValueError:
            print('Please enter a number.')
            continue

        if player_number <= 1:
            print('Players should be more than one.')
            continue

        break

    while True:
        try:
            target_score = int(input('Please set a target score: '))
        except ValueError:
            print('Please enter a number.')
            continue

        if target_score <= 0:
            print('Please enter a number greater than 0.')
            continue

        break

    return target_score, player_number

def should_continue():
    while True:
        continue_game = input('\nWould you like to play again? (y/n): ').lower()

        if continue_game not in ('y', 'n'):
            print('Please choose y or n only.')
            continue

        print('\n')

        if continue_game == 'y':
            return True
        elif continue_game == 'n':
            return False

def main():
    count = 0
    games_played = 0

    player_scores = []
    player_points = []
    players = []

    target_score, player_number = customize_game()

    for i in range(1, player_number + 1):
        players.append(i)
        player_scores.append(0)
        player_points.append(0)

    while True:
        current_player = players[count]
        roll_dice(current_player, player_scores)
        declare_winner = check_win(current_player, player_scores, target_score, player_points)

        if declare_winner:
            points_text = ', '.join(
                f'Player {i}: {score}'
                for i, score in enumerate(player_points, start=1)
            )

            print(f'\nPlayer overall scores: {points_text}')

            continue_game = should_continue()
        else:
            count = (count + 1) % player_number
            continue

        if continue_game:
            games_played += 1
            count = games_played % player_number
            print(f'The first player now is Player {players[count]}.')

            for i in range(player_number):
                player_scores[i] = 0

            continue
        else:
            break

if __name__ == "__main__":
    main()
