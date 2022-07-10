# import json

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
    def test_get_nature(self, api):
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

    




    # def test_get_word_error(self, api):
    #     res = api.get('/api/world/4')
    #     assert res.status == '400 BAD REQUEST'


    # def test_post_cats(self, api):
    #     mock_data = json.dumps({'name': 'Molly'})
    #     mock_headers = {'Content-Type': 'application/json'}
    #     res = api.post('/api/cats', data=mock_data, headers=mock_headers)
    #     assert res.json['id'] == 3

    # def test_patch_cat(self, api):
    #     mock_data = json.dumps({'name': 'Molly'})
    #     mock_headers = {'Content-Type': 'application/json'}
    #     res = api.patch('/api/cats/2', data=mock_data, headers=mock_headers)
    #     assert res.json['id'] == 2
    #     assert res.json['name'] == 'Molly'

    # def test_delete_cat(self, api):
    #     res = api.delete('/api/cats/1')
    #     assert res.status == '204 NO CONTENT'

    # def test_not_found(self, api):
    #     res = api.get('/bob')
    #     assert res.status == '404 NOT FOUND'
    #     assert 'Oops!' in res.json['message']