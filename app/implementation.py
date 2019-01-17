from .models.models import RedFlag
import datetime

red_flags = {}


class Implementation:
    def create(self, data):
        others = {
            'type': 'red-flag', 'status': 'draft', 'videos': [], 'images': [],
            'comment': ''}
        red_flag = RedFlag(
            (RedFlag.count + 1), data['location'], data['createdBy'],
            data['title']
            )
        red_flag.__setattr__('createdOn', datetime.datetime.now())
        for key in others:
            if key in data:
                red_flag.__setattr__(key, data[key])
            else:
                red_flag.__setattr__(key, others[key])
        red_flags[str(red_flag.id)] = red_flag.__dict__
        return [
            201, 'data', [{'id': red_flag.id, 'message': 'Created red flag'}]
            ]

    def get_flags(self):
        res = [200, 'data', [red_flags[key] for key in red_flags.keys()]]
        return res

    def get_flag(self, red_flag_id):
        try:
            red_flag = red_flags[str(red_flag_id)]
            res = [200, 'data', [red_flag]]
        except Exception as e:
            print(e)
            res = [200, 'data', []]
        return res

    def edit(self, id, data, field):
        flag = self.get_flag(id)[2]
        if field == 'location' and 'geolocation' not in flag[0][
                'location']:
            flag[0]['location'] += ' ' + data['location']
            res = 'added'
        elif field == 'location' and 'geolocation' in flag[0]['location']:
            flag[0]['location'] =\
                    flag[0]['location'][:flag[0]['location'].index(
                        'geolocation')] + data['location']
            res = 'updated'
        else:
            flag[0][field] = data[field]
            res = 'updated'
        return [200, 'data', [{
                'id': int(id), 'message':
                f'{res} red-flag record\'s {field}'}]]

    def delete(self, id):
        try:
            red_flags.pop(str(id))
            res = [200, 'data', [{'id': int(id), 'message':
                                 'red-flag record has been deleted'}]]
        except Exception:
            res = [404, 'error', 'red flag not found']
        return res
