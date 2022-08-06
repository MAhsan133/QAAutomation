import requests
import json
from read_config import ReadConfigFile


class TestRestAPI:

    @staticmethod
    def generate_token(refresh_token, app_key):
        # Based upon client app key and refresh token, an access token will be generated
        # For testing purpose doing it simple, this api does not support this
        access_token = None
        if refresh_token == '12345' and app_key == '12345':
            access_token = 11223344
        return access_token

    @classmethod
    def setup_class(cls):
        cls.BASE_URL, refresh_token, app_key = ReadConfigFile().get_user_credentails()
        cls.session = requests.session()
        cls.session.VALID_USER = False
        access_token = cls.generate_token(refresh_token, app_key)
        cls.headers = {'Content-Type': 'application/json'}
        if access_token:
            cls.session.VALID_USER = True
            cls.headers['Authorization'] = 'Bearer ' + str(access_token)

    # GET method - ALL Users - Verify total records=12 and response=200
    def test_0001_all_users_get_request(self):
        if not self.session.VALID_USER:
            assert False, "Invalid User"
        else:
            user_url = self.BASE_URL + 'api/users'
            resp = self.session.get(user_url, headers=self.headers)
            total_records = json.loads(resp.text)['total']
            assert resp.status_code == 200
            assert total_records == 12

    # GET method - ALL Users - Page number is 100 and data should be empty list
    def test_0002_all_users_page_100(self):
        if not self.session.VALID_USER:
            assert False, "Invalid User"
        else:
            user_url = self.BASE_URL + 'api/users'
            params = {'page': 100}
            resp = self.session.get(user_url, params=params, headers=self.headers)
            data_length = len(json.loads(resp.text)['data'])
            assert resp.status_code == 200
            assert data_length == 0

    # GET method - Single User Detail - Verify records=12 and response=200
    def test_0003_single_user_get_request(self):
        if not self.session.VALID_USER:
            assert False, "Invalid User"
        else:
            user_url = self.BASE_URL + 'api/users/2'
            resp = self.session.get(user_url, headers=self.headers)
            user_email = json.loads(resp.text)['data']['email']
            assert resp.status_code == 200
            assert user_email == 'janet.weaver@reqres.in'

    # GET method - Single User Detail - Fetch user which does not exist
    def test_0004_single_user_invalid_id(self):
        if not self.session.VALID_USER:
            assert False, "Invalid User"
        else:
            user_url = self.BASE_URL + 'api/users/100'
            resp = self.session.get(user_url, headers=self.headers)
            assert resp.status_code == 404

    # POST method - Create user with custom data in request body
    # It fails as it accept any thing you passed
    def test_0005_post_request_invalid_data(self):
        if not self.session.VALID_USER:
            assert False, "Invalid User"
        else:
            post_url = self.BASE_URL + 'api/users'
            post_data = {"test": "abc"}
            resp = self.session.post(url=post_url, json=post_data, headers=self.headers)
            assert resp.status_code == 400

    # POST method - Verify user created with status code 201
    def test_0006_post_request(self):
        if not self.session.VALID_USER:
            assert False, "Invalid User"
        else:
            post_url = self.BASE_URL + 'api/users'
            post_data = {"name": "Ahsan", "job": "IT"}
            resp = self.session.post(url=post_url, json=post_data, headers=self.headers)
            assert resp.status_code == 201

    # GET method - Verify User count after new user creation. It should be 13 now
    #  It fails as it does not increase count after increment
    def test_0007_get_all_users(self):
        if not self.session.VALID_USER:
            assert False, "Invalid User"
        else:
            user_url = self.BASE_URL + 'api/users'
            resp = self.session.get(user_url, headers=self.headers)
            total_records = json.loads(resp.text)['total']
            assert resp.status_code == 200
            assert total_records == 13

    # PUT method - Update Users detail
    def test_0008_put_request(self):
        if not self.session.VALID_USER:
            assert False, "Invalid User"
        else:
            user_url = self.BASE_URL + 'api/users/2'
            put_data = {"name": "Ahsan1", "job": "IT1"}
            resp = self.session.put(url=user_url, json=put_data, headers=self.headers)
            name = json.loads(resp.text)['name']
            assert resp.status_code == 200
            assert name == 'Ahsan1'

    # PUT method - Update Users detail with custom data
    # It fails as it accept anything you passed in body
    def test_0009_put_request_invalid_data(self):
        if not self.session.VALID_USER:
            assert False, "Invalid User"
        else:
            user_url = self.BASE_URL + 'api/users/2'
            put_data = {"test": "james"}
            resp = self.session.put(url=user_url, json=put_data, headers=self.headers)
            assert resp.status_code == 400

    # PATCH method - Update name only
    def test_0010_patch_request(self):
        if not self.session.VALID_USER:
            assert False, "Invalid User"
        else:
            user_url = self.BASE_URL + 'api/users/2'
            put_data = {"name": "AhsanPatch"}
            resp = self.session.patch(url=user_url, json=put_data, headers=self.headers)
            name = json.loads(resp.text)['name']
            assert resp.status_code == 200
            assert name == 'AhsanPatch'

    # PATCH method - Update name only
    # It fails as it accept invalid value, It should be bad request
    def test_0011_patch_request_invalid_data(self):
        if not self.session.VALID_USER:
            assert False, "Invalid User"
        else:
            user_url = self.BASE_URL + 'api/users/2'
            put_data = {"testing": "12345"}
            resp = self.session.patch(url=user_url, json=put_data, headers=self.headers)
            assert resp.status_code == 400

    # DELETE method - with invalid user id
    # it fails as user does not exist
    def test_0012_delete_request_invalid_id(self):
        if not self.session.VALID_USER:
            assert False, "Invalid User"
        else:
            user_url = self.BASE_URL + 'api/users/100'
            resp = self.session.delete(url=user_url, headers=self.headers)
            assert resp.status_code == 404

    # DELETE method - status code=204
    def test_0013_delete_request(self):
        if not self.session.VALID_USER:
            assert False, "Invalid User"
        else:
            user_url = self.BASE_URL + 'api/users/2'
            resp = self.session.delete(url=user_url, headers=self.headers)
            assert resp.status_code == 204

    # GET method - Verify User count after new user creation. It should be 13 now
    def test_0014_get_all_users(self):
        if not self.session.VALID_USER:
            assert False, "Invalid User"
        else:
            user_url = self.BASE_URL + 'api/users?page=2'
            resp = self.session.get(user_url, headers=self.headers)
            total_records = json.loads(resp.text)['total']
            assert resp.status_code == 200
            assert total_records == 12
