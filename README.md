# GAEFlask
Learn, create and play with GAE and flask based service

Install Python 2.7

Install Google cloud sdk.

Install Google Appengine sdk.

Install PyCharm

Create new project in PyCharm for Google App Engine.

Select option to provide support for flask.

Comment application and version fields from app.yaml

Add field service with value as trialservice

From the terminal in pycharm, try gcloud init.
  login to gcloud, if not already logged in.

Run 'pip install -t lib -r requirements.txt' 

Run the deploy command 'gcloud -q app deploy --version v1 --project [rmoveBracketsAndPutGoogleProjectID] app.yaml'

Hit the base url and route mjk and verify if the service is deployed or not.
