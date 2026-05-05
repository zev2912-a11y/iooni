# Python
# Instagram Bot Template (Automation of Likes, Views, Followers)

from instabot import Bot
import os

# Change console title if applicable (Windows only)
os.system("title Instagram Botter")

# Initialize Bot
bot = Bot()

# Login credentials (replace with your own credentials)
username = input("Enter your Instagram username: ")
password = input("Enter your Instagram password: ")
bot.login(username=username, password=password)

def main():
    print("Please choose a botter category:")
    print("[1] - Like posts")
    print("[2] - View stories")
    print("[3] - Follow users")
    
    choice = input("> ")
    
    if choice == "1":
        post_url = input("Paste your Instagram post URL (must be public): ")
        if not post_url.startswith("https://www.instagram.com/p/"):
            print("Invalid post URL")
        else:
            media_id = bot.get_media_id_from_link(post_url)
            bot.like(media_id)
            print("Post liked successfully!")
            
    elif choice == "2":
        user_to_view = input("Enter Instagram username to view story: ")
        if not bot.get_user_id_from_username(user_to_view):
            print("Cannot find this user or user is private")
        else:
            user_id = bot.get_user_id_from_username(user_to_view)
            bot.view_story(user_id)
            print("Story viewed successfully!")
            
    elif choice == "3":
        user_to_follow = input("Enter Instagram username to follow: ")
        if not bot.get_user_id_from_username(user_to_follow):
            print("User not found")
        else:
            bot.follow(user_to_follow)
            print(f"Now following {user_to_follow}")

    else:
        print("Invalid choice. Exiting")

if __name__ == "__main__":
    main()
