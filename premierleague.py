import pandas as pd

df = pd.read_csv('PLPstats.csv')

def display_stats(category=None, team=None):
    if category:
        top_players = df.nlargest(10, category)
        print(f"Top 10 performers in {category}:\n")
        print(top_players)
    
    if team:
        team_stats = df[df['TEAM'] == team]
        print(f"\nPlayer stats for {team}:\n")
        print(team_stats)

def main_menu():
    while True:
        print("Select an option:")
        print("1. Display top performers by category")
        print("2. Display player stats for a team")
        print("3. Quit")
        
        choice = input()
        
        if choice == '1':
            category = input("Enter the category (e.g., G, ASST): ")
            try:
                display_stats(category=category)
            except Exception as e:
                print(f"An error occurred: {e}")
        elif choice == '2':
            team = input("Enter the team name (e.g., Chelsea): ")
            try:
                display_stats(team=team)
            except Exception as e:
                print(f"An error occurred: {e}")
        elif choice == '3':
            print("Goodbye!")
            return
        else:
            print("Invalid choice. Please select a valid option.")

main_menu()
