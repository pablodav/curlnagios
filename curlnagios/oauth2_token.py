#
# documentation:
# https://docs.microsoft.com/en-us/azure/active-directory/develop/v2-oauth2-auth-code-flow
import requests
import json

# Will support with access token

class GetOauth2Token:
    def __init__(self, client_id, scope, client_secret, 
                 grant_type = 'client_credentials',
                 auth_url = 'https://login.microsoftonline.com/company.onmicrosoft.com/oauth2/v2.0/token'):
        """
        reference: https://docs.microsoft.com/en-us/azure/active-directory/develop/v2-oauth2-auth-code-flow#request-an-access-token
        The Authority configured on the client MUST match the one configured on the server. 
        The Scope configured on the client MUST match the one configured on the server, followed by the .default suffix. 
        The Client Id is the ApplicationId of the client application configured on the Microsoft Application Registration Portal. 
        The Client Key is the Password generated on the client. 

        param client_id: example client id: 6731de76-14a6-49ae-97bc-6eba6914391e
        param scope: example: https://company.onmicrosoft.com/some-unique-number-for-scope/.default
        param client_secret: "client password secret here"
        param grant_type: default is "client_credentials"
        param auth_url: use the correct one for your organization and application server, default example
                        https://login.microsoftonline.com/company.onmicrosoft.com/oauth2/v2.0/token
        """
        self.client_id = client_id
        self.scope = scope
        self.client_secret = client_secret
        self.grant_type = grant_type
        self.auth_url = auth_url
    
    def get_token(self):
        """

        return: tuple dict with access_token, status_code
            {'access_token': 'tokenid'
            'expires_in': 3600,
            'ext_expires_in': 0,
            'token_type': 'Bearer'}, 200
        """
        # Request access token:
        # https://docs.microsoft.com/en-us/azure/active-directory/develop/v2-oauth2-auth-code-flow#request-an-access-token

        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        url = self.auth_url
        data = { "client_id": self.client_id,
                "scope": self.scope,
                "client_secret": self.client_secret,
                "grant_type": self.grant_type
            }
        # requests doc http://docs.python-requests.org/en/v0.10.7/user/quickstart/#custom-headers
        r = requests.post(url=url, data=data, headers=headers)
        
        return r.json(), r.status_code

    def url_check(self, url_check):
        """
        Just example howto proceed with the token got

        param url_check: url to check with authenticated token

        """
        # Use the access token:
        # https://docs.microsoft.com/en-us/azure/active-directory/develop/v2-oauth2-auth-code-flow#use-the-access-token
        
        get_token = self.get_token()
        access_token = get_token[0]['access_token']
        header_token = {"Authorization": "Bearer {}".format(access_token)}
        rt = requests.get(url=url_check, headers=header_token)

        return rt.json(), rt.status_code

# Refresh? will need to check if we are going to do it (don't think so)
# https://docs.microsoft.com/en-us/azure/active-directory/develop/v2-oauth2-auth-code-flow#refresh-the-access-token
