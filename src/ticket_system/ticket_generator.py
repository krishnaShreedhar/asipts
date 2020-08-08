import json


class TicketGenerator:

    def __init__(self, source, destination, **kwargs):
        self.source = source
        self.destination = destination
        self.start_time = kwargs.get('start_time', None)
        self.end_time = kwargs.get('end_time', None)
        self.max_hops = kwargs.get('max_hops', 9999)
        self.max_cost = kwargs.get('max_cost', 9999)
        self.is_senior_citizen = kwargs.get('is_senior_citizen', False)
        self.is_adult = kwargs.get('is_adult', True)

        self.dict_ticket = {}

    def get_dict_ticket(self):
        if not self.dict_ticket:
            self.dict_ticket = self.compute_dict_ticket()
        return self.dict_ticket

    def compute_dict_ticket(self):
        dict_ticket = {
            'source': self.source,
            'destination': self.destination,
            'cost': 100.0
        }
        return dict_ticket

    def get_json_ticket(self):
        return json.dumps(self.get_dict_ticket())
