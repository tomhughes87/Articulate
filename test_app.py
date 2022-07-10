# import json

class TestAPICase():
    def test_all_topics(self, api):
        res = api.get('/api/all')
        assert res.status == '200 OK'
        assert res.json == ["person","world","object","action","nature"]

    def test_get_entire_topic_list(self, api):
        res = api.get('/api/person')
        assert res.status == '200 OK'
        assert len(res.json) == 2

    def test_get_word(self, api):
        res = api.get('/api/nature/1')
        assert res.status == '200 OK'
        assert res.json == 'Leaf'

    

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