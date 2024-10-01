#imports: logging, requests, smtplib, json
import logging, requests, smtplib, json

# setup
# implement logging
log_file = 'api_logs.log'
logging.basicConfig(
    filename=log_file, 
    filemode='a', 
    level=logging.INFO, 
    format='%(asctime)s : %(levelname)s - %(message)s'
    )

logging.info('=============== Joke Email ===============\n')

URL = 'https://v2.jokeapi.dev/joke/Programming?blacklistFlags=nsfw,religious,political,racist,sexist,explicit'

# read json settings for gmail
with open('creds.json', 'r') as f:
    logging.info('Retrieving login credentials...')
    credential_info = json.load(f)
    f.close()

# send email with content from API: v2.jokeapi.dev


def send_email(joke_content):
    logging.info('=============== Email ===============')
    EMAIL = credential_info['email']
    PASSWORD = credential_info['password']
    RECIPIENT = EMAIL
    SUBJECT = 'Python Joke Api'
    message = f'Subject: {SUBJECT}\n\n{joke_content}'
    try: 
        logging.info('Attempting to connect to gmail...')
        s = smtplib.SMTP('smtp.gmail.com', 587) #Specific to Gmail
        s.starttls()    # encrypt connection in order to send using TLS
    except smtplib.SMTPConnectError:
        logging.fatal('Could not connect to the mail server...')
        exit()
    try:
        s.login(EMAIL, PASSWORD)    # login with credentials
    except smtplib.SMTPAuthenticationError:
        logging.fatal('Authentication Failure: Check your json configuration')
        exit()
    try:
        s.sendmail(EMAIL, RECIPIENT, message)
        logging.info('Message was successfully sent!')
    except smtplib.SMTPException:
        logging.fatal('Error occurred while attempting to send email...')
        exit()
    s.quit()
        

def get_joke():
    logging.info('=============== Joke API ===============')
    logging.info('Attempting to get joke content...')
    try:
        response = requests.get(URL)
        resp_code = response.status_code
        if resp_code == 200:
            data = response.json()
            if data['error']:
                logging.error('Error occurred during API call on server side...')
                return None
            joke_type = data['type'] #twopart or single
            if joke_type == 'single':
                joke = f"Joke: {data['joke']}"
            else:
                joke = f"Joke: {data['setup']}\nFollow-up: {data['delivery']}"
            logging.info('Successfully Retrieved Joke')
            return joke
        else:
            logging.warning(f'Error, status code: {resp_code}')
            return f'Issue with request: {resp_code}'
    except:
        logging.error('Exception...')
        print(f'Exception occurred')
        exit()


# ensure email creds are not in src code (use external json)
joke = get_joke()

if joke is not None:
    send_email(joke)
# Properly handle all exceptions specifically

