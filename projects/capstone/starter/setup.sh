DATABASE_URL: postgres://sljqkkkxdpdbhd:eb297ded42440f1d7d711601a2533d66676b32a537657750188a1720c6bace10@ec2-18-214-195-34.compute-1.amazonaws.com:5432/d3vb1pi15q70cp
HEROKU_POSTGRESQL_COBALT_URL: postgres://joeiqqqyetndqe:45ad39a89116cb2db7a3e15bed35f4c02f2095044e413f07b7efbe953c16de9b@ec2-52-86-2-228.compute-1.amazonaws.com:5432/d36kdacsl325nk
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
export AUTH0_CALLBACK_URL='https://Salquraishi.herokuapp.com/'

