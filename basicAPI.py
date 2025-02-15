import requests

def fetch_random_user():
    url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"
    response = requests.get(url) # here we will response<200> as o/p om print
    data = response.json()

    #Extracting data
    if data["success"] and "data" in data: # data is oblect in data from API
        user_data = data["data"]
        username = user_data["login"]["username"] # as it data is coming in dictionary striucture
        country = user_data["location"]["country"]# inside data ->location& inside location country is given in dictionay
        return username, country
    else:
        raise Exception("Failed to fetch user data")

def main():
    # to protesct main fron crash

    try:
        username, country = fetch_random_user()
        print(f"Username is {username} & country is {country}")
    except Exception as e:
        print(str(e))
if __name__ == "__main__":
    main()


      