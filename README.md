# Flask Sample application

### Table of Contents

  - [Introduction](#introduction)
  - [Prerequisites](#prerequisites)
  - [Quick Start](#quick-start)
  - [Setup Okta environment](#setup-okta-environment)
  - [Client credential flow](#client-credential-flow)
  - [Resource password grant flow](#resource-password-flow)
  
## Introduction

This tutorial will demonstrate how to use OAuth 2.0 and OpenID Connect to add authentication to a Python/Flask application.

## Prerequisites

This sample app needs python (python 2.7). It can work with python3.0 also, but some of the statements will need to be refactored

```bash
# Verify that python is installed
$ python -V
```

```bash
# Verify that virtualenv for python is installed
$ virtualenv
```

Then, clone this sample from GitHub and install the front-end dependencies:
```bash
# Clone the repo and navigate to the samples-python-flask dir
$ git clone https://github.com/jayanthv86/okta_oauth.git && cd okta_oauth
```

# Install the dependencies
```bash
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Quick Start

Start by running the following command `python app.py`. This will start up the server and it will start listening for requests on http://localhost:3000/

## Setup Okta environment

Create an authorization server, by clicking on API -> Authorization server -> Create Authorization server
    Make sure to add your custom scopes here that you will use in the code
    Make sure to set access policy, for all clients to access this authorization server

For resource password flow, create an OIDC application, by clicking on Application -> Add application -> Create new app -> Native -> OpenID Connect
        Make sure #Resource Owner password grant# is selected
For client credential flow, create an OIDC application, by clicking on Application -> Add application -> Create new app -> Web -> OpenID Connect
        Make sure #Client credentials grant# is selected

Edit the code to include the details from your Okta environment in constants below in `app.py`:

```
auth_server_id = 'YOUR_OKTA_AUTH_SERVER_ID' # Replace with your okta authorization server id
auth_server_url = 'YOUR_OKTA_DOMAIN' # Replace with your okta org
```

Edit the code to include the details for the custom scopes in `helper.py`:

```
CUSTOM_SCOPES= 'Your custome scopes'
```

Edit the code to include the details for the same custom scope you want to check at end point in `app.py`:

```
CUSTOM_SCOPE_TOCHECK='Your custom scopes you want to check'
```

The auth server id will be the element https://mycompanyname.okta.com/oauth2/#aus1n9537m60l8ASr2p6
The okta domain name would be #https://mycompanyname.okta.com

## Client credential flow

You can run the below commands as is, if you have curl installed or use postman.

Uncomment the below two lines in the `app.py` file and save it (code will automatically reload)

```
#oauth_body = get_oauth_body_client_credentials() # uncomment For client credential flow
#basic_authorization_header = generate_basic_auth(cred_dict) # uncomment For client credential flow
```

First authenticate by providing the client credentials against the authenticate end point:

```
curl -H 'Content-Type: application/json' -d '{"client_id":"YOUR_OKTA_OIDC_CLIENTID", "client_secret":"YOUR_OKTA_OIDC_CLIENTSECRET"}' http://localhost:5000/authenticate
```

Once you receive an access token, you can use this against your protected URI:

```
curl -H "Authorization: Bearer YOUR_ACCESS_TOKEN" http://localhost:5000/card_services
```

## Resource password flow

You can run the below commands as is, if you have curl installed or use postman:

First authenticate by providing the client credentials against the authenticate end point:

```
curl -H 'Content-Type: application/json' -d '{"client_id":"YOUR_OKTA_OIDC_CLIENTID", "client_secret":"YOUR_OKTA_OIDC_CLIENTSECRET", "username":"YOUR_OKTA_USERNAME", "password":"YOUR_OKTA_PASSWORD"}' http://localhost:5000/authenticate
```

Once you receive an access token, you can use this against your protected URI:

```
curl -H "Authorization: Bearer YOUR_ACCESS_TOKEN" http://localhost:5000/card_services
```
