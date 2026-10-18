import requests

URL = "https://api.mojang.com/users/profiles/minecraft/"

def get_uuid(username: str):
    response = requests.get(URL + username)

    if response.status_code == 200:
        data = response.json()

        return data["id"]
    elif response.status_code == 400 or response.status_code == 404:
        raise LookupError()
    else:
        raise SystemError()

while True:
    username = input("Enter username: ")

    try:
        print(f"UUID of {username} is {get_uuid(username)}")
    except LookupError:
        print(f"The account {username} doesn't exist!")
    except SystemError:
        print(f"Internal API error")
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.ConnectionError:
        print("Network connection failed.")
    except requests.exceptions.Timeout:
        print("The request timed out.")
    except requests.exceptions.RequestException as e:
        print(f"An unexpected error occurred: {e}")