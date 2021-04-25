"""
This module will bring together different modules and help in planning the best possible routes:
1. source: starting place of travel
2. destination: ending place of travel
3. etas: estimated time of arrival at source
4. etad: estimated time of arrival at destination
5. priority:
    1. high: cost of travel is irrelevant
    2. med: balanced cost/time trade-off
    3. low: economical
6.
"""


class RoutePlanner:

    def __init__(self,
                 source,
                 destination,
                 etas,
                 etad,
                 priority,
                 **kwargs):
        self.source = source
        self.destination = destination
        self.etas = etas
        self.etad = etad
        self.priority = priority

        print(f"kwargs: {kwargs}")

    def plan(self):
        """

        :return:
        """
        list_plans = [
            {
                "route": [],
                "cost": 0.0,
                "waiting_time_mins": 0.0
            }
        ]
        connectors = self.find_connectors()
        return list_plans

    def find_connectors(self):
        """
        Need a graph representation for shortest routes

        - This can be learnt with people's preferred ways of travelling

        Treat like points. point 0 and n-1 are source
        search intermediate travel options between source and destination
        :return:
        """
        return {}

