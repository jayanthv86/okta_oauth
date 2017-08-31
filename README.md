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

Create an OIDC application, by clicking on Application -> Add application -> Create new app -> Native -> OpenID Connect

## Client credential flow

You can run the below commands as is, if you have curl installed or use postman:

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
