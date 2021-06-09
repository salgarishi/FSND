curl --request POST \
  --url https://salgarishi.us.auth0.com/oauth/token \
  --header 'content-type: application/json' \
  --data '{"client_ID":"eUaQkItNEpZjqlaf28WcYeniVWMH3WhL","client_secret":"1uKK8YSs5cmOdV91_6-lit7GF89KvOLjt5dzCg9WZcK403dKL-woHh8KAQ8xj8W1","audience":"Agency","grant_type":"client_credentials"}'

export AUTH0_DOMAIN='https://salgarishi.us.auth0.com'
export API_AUDIENCE='Agency'
export ALGORITHEMS=['RS256']
export ROWS_PER_PAGE = 10
export database_name = "Agency"
export database_path = "postgresql://postgres:123!@#@{}/{}".format('localhost:5432', database_name)
export AUTH0_CALLBACK_URL='https://salquraishi-agency.herokuapp.com/'

