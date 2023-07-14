import instaloader

class InstagramProfile:
    def __init__(self):
        self.bot = instaloader.Instaloader()

    def get_profile_information(self, username):
        """Retrieve information about an Instagram profile."""
        profile = instaloader.Profile.from_username(self.bot.context, username)
        print("Profile Type: ", type(profile))
        print("Username: ", profile.username)
        print("User ID: ", profile.userid)
        print("Number of Posts: ", profile.mediacount)
        print("Followers: ", profile.followers)
        print("Followees: ", profile.followees)
        print("Bio: ", profile.biography, profile.external_url)

    def login_with_2fa(self, username, password):
        """Login to Instagram account with two-factor authentication."""
        try:
            self.bot.login(username, password)
        except instaloader.exceptions.TwoFactorAuthRequiredException as e:
            # Two-factor authentication is required, perform necessary steps to continue
            verification_code = input("Enter verification code: ")
            try:
                self.bot.two_factor_login(verification_code)
            except instaloader.exceptions.BadCredentialsException as e:
                print("Invalid verification code. Please try again.")
                self.login_with_2fa(username, password)  # Retry by calling the function again
            except Exception as e:
                print("An unexpected error occurred:", str(e))
                # Cannot proceed further, handle appropriately
        except instaloader.exceptions.BadCredentialsException as e:
            print("Invalid username or password. Please try again.")
        except Exception as e:
            print("An unexpected error occurred:", str(e))
            # Cannot proceed further, handle appropriately

    def get_followers(self, username):
        """Retrieve the usernames of all followers of an Instagram profile."""
        profile = instaloader.Profile.from_username(self.bot.context, username)
        followers = [follower.username for follower in profile.get_followers()]
        return followers

    def get_followees(self, username):
        """Retrieve the usernames of all followees of an Instagram profile."""
        profile = instaloader.Profile.from_username(self.bot.context, username)
        followees = [followee.username for followee in profile.get_followees()]
        return followees

    def save_to_file(self, data, filename):
        """Save the data to a text file."""
        with open(filename, 'w') as file:
            for item in data:
                file.write(item + '\n')
        print("Data saved to", filename)

    def load_from_file(self, filename):
        """Load data from a text file."""
        with open(filename, 'r') as file:
            data = file.read().splitlines()
        return data


# Example usage
insta_profile = InstagramProfile()
insta_profile.login_with_2fa("username", "passwd")
insta_profile.get_profile_information("onuryilmazo")
followers = insta_profile.get_followers("username")
followees = insta_profile.get_followees("username")

# Save followers and followees to files
insta_profile.save_to_file(followers, "followers.txt")
insta_profile.save_to_file(followees, "followees.txt")

# Load data from files
loaded_followers = insta_profile.load_from_file("followers.txt")
loaded_followees = insta_profile.load_from_file("followees.txt")

