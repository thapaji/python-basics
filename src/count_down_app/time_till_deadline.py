from datetime import datetime


def main():
    user_goal = input('Enter your goal: ')
    user_date_input = input('Enter deadline date of the goal(dd.mm.yyyy format): ')
    user_goal_deadline = datetime.strptime(user_date_input, '%d.%m.%Y')
    today = datetime.today()
    difference = (user_goal_deadline - today).total_seconds() / 60 // 60
    print(f'The time remaining for achieving for your goal {user_goal} is {difference} hours')


main()
