#!flask/bin/python
from flask import Flask, jsonify, request, _app_ctx_stack, json
import requests
from helper import generate_basic_auth, generate_simple_auth, get_oauth_body_client_credentials, get_oauth_body_password, requires_auth, requires_scope

app = Flask(__name__)
app.config['SECRET_KEY'] = 'super-secret' # Change to uuid

auth_server_id = 'aus1n9537m60l8ASr2p6' # Replace with your okta authroziation server id
auth_server_url = 'https://jay.okta.com' # Replace with your okta org
auth_domain_endpoint = '{}/oauth2/{}'.format(auth_server_url, auth_server_id)
API_AUDIENCE = 'http://localhost:3000/' # whatever your API domain is called and should be added as audience to the API

@app.route('/')
def index():
    """Unprotected API
    """
    return "Hello, World!"

@app.route('/authenticate', methods=['POST'])
def authenticate():
    """Authentication end point, authenticate here to get the access token.
    For password flow, provide in payload:
        username,
        password,
        client_id,
        client_secret
    For client credentials flow, provide in payload:
        client_id,
        client_secret
    """
    cred_dict = {}
    try:
        cred_dict = request.json
    except TypeError, e:
        msg = "payload must be a valid json"
        return jsonify({"code": "invalid credentials",
                        "description": msg}), 400
    basic_authorization_header = generate_basic_auth(cred_dict)
    if not basic_authorization_header:
        return jsonify({"code": "invalid credentials",
                        "description": "valid username and password needed"}), 400
    oauth_body = get_oauth_body_password(cred_dict)
    basic_authorization_header = generate_simple_auth(cred_dict)
    #oauth_body = get_oauth_body_client_credentials() # For client credential flow
    #basic_authorization_header = generate_basic_auth(cred_dict) # For client credential flow
    url = '{}/v1/token'.format(auth_domain_endpoint)
    r = requests.post(url, headers=basic_authorization_header, data=oauth_body)
    return jsonify(r.json()), 200

@app.route('/card_services')
@requires_auth
def card_services():
    """Protected endpoint"""
    if requires_scope('username'): # Additional check for scope to verify if user has right scope
        return jsonify(card_services='Welcome to Card services',
                      membership='Only for card members',
                      excluding='partners')
    else:
        return jsonify({"code":"Not authorized",
                        "description":"Not authorized to access this application"}), 200

@app.route('/card_referrals')
@requires_auth
def card_referrals():
    """Protected endpoint"""
    return jsonify(card_services='Welcome to Card referrals',
                  membership='Only for card partners',
                  excluding='customers')

@app.route('/rewards_points')
@requires_auth
def card_points():
    """Protected endpoint"""
    return jsonify(card_services='Welcome to Reward points',
                  membership='Only for customers and partners',
                  excluding='')

@app.route('/interest_rate')
@requires_auth
def interest_rate():
    """Protected endpoint"""
    return jsonify(card_services='Welcome to Interest rate',
                  membership='Only for bank employess',
                  excluding='customers, partners')



if __name__ == '__main__':
    app.run(debug=True)