# import json

import json


class TestAPICase():

# ////////////////////////
# GET TESTS-----------------------------------
# ////////////////////////
    # 1
    def test_get_entire_api (self,api):
        res = api.get('api/all')
        assert res.status == '200 OK'
        assert len(res.json[0]) == 5
        assert len(res.json[0]) == 5
        for i in res.json[0]:
            assert len(res.json[0][i]) == 2
    # 2
    def test_get_all_topics(self, api):
        res = api.get('/api/topics')
        assert res.status == '200 OK'
        assert res.json == ["person","world","object","action","nature"]
    # 3
    def test_get_person(self, api):
        res = api.get('/api/person')
        assert res.status == '200 OK'
        assert len(res.json) == 2
    # 4
    def test_get_world(self, api):
        res = api.get('/api/world')
        assert res.status == '200 OK'
        assert len(res.json) == 2
        assert res.json[0] == 'Paris'
        assert res.json[1] == 'The Thames'
    # 5
    def test_get_nature(self, api):
        res = api.get('/api/nature')
        assert res.status == '200 OK'
        assert len(res.json) == 2
        assert res.json[0] == 'Zebra'
        assert res.json[1] == 'Leaf'
    # 6
    def test_get_object(self,api):
        res=api.get('api/object')
        assert res.status == '200 OK'
        assert len(res.json) == 2
        assert res.json[0] == 'Fan'
        assert res.json[1] == 'Trident'
    # 7
    def test_get_action(self,api):
        res = api.get('api/action')
        assert res.status == '200 OK'
        assert len(res.json) == 2
        assert res.json[0] == 'jump'
        assert res.json[1] == 'sing'
    # 8
    def test_get_word(self, api):
        res = api.get('/api/nature/1')
        assert res.status == '200 OK'
        assert res.json[0] == 'Leaf'
    # 9
    def test_get_random(self, api):
        res = api.get('/api/random')
        assert res.status == '200 OK'
        assert len(res.json) == 10

    # 10
    def test_get_no_rand_double(self,api):
        res= api.get('api/random')
        json_to_set = set(res.json)  
        assert len(json_to_set) == len(res.json) #by converting the json to set it removes any doubles

# ////////////////////////
# DELETE TESTS-----------------------------------
# ////////////////////////
    # 11
    def test_destroy_word(self,api):
        res = api.delete('/api/action/1')
        assert res.status == '204 NO CONTENT'

# ////////////////////////
# PATCH TESTS-----------------------------------BROKEN
# ////////////////////////
    #12
    def test_patch_word(self, api):
            mock_data = json.dumps('Car')
            mock_headers = {'Content-Type': 'application/json'}
            # res = api.patch('/api/nature/1', data=mock_data)
            res = api.patch('/api/nature/1', data=mock_data, headers=mock_headers)
            # assert res.json['id'] == 2
            assert res.json[0] == 'Car'


# ////////////////////////
# CREATE TESTS-----------------------------------BROKEN
# ////////////////////////
    #13
    def test_post_word(self, api):
        original_api= api.get('/api/object')
        print(original_api.json)
        mock_data = json.dumps(['banana'])
        mock_headers = {'Content-Type': 'application/json'}
        res = api.post('/api/object', data=mock_data, headers=mock_headers)
        print('after posting:',  original_api.json)
        assert len(original_api.json) == 3

# ////////////////////////
# MISC TESTS-----------------------------------
# ////////////////////////
    # 14
    def test_homepage_status(self,api):
        res = api.get ('/')
        assert res.status == "200 OK"
