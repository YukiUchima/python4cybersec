from gtoken import get_token
import requests
# retrieve token
my_token = 'test' #get_token() -> Retrieve token from another file...

# github
username = '-'
base_url = 'https://api.github.com'
# auth_header = (username, token)
header = {
    'Authorization': 'token ' + my_token
}
 
# login to github
resp = requests.get(f'{base_url}/users/{username}/repos', headers = header)
print(resp.json())