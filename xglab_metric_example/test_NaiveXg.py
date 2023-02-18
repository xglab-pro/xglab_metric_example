import unittest

import numpy as np
import pandas as pd

from xglab_metric_example.NaiveXg import NaiveXg


class TestNaiveXg(unittest.TestCase):
    maxDiff = 1024

    expected_rows = [
        {'metricId': 0, 'eventUuid': 'penalty', 'teamId': 0, 'matchId': 0, 'playerId': 0,
         'className': 'Penalty', 'value': 0.76, 'teamValue': 0.76},
        {'metricId': 0, 'eventUuid': 'otherTeam', 'teamId': 100, 'matchId': 0, 'playerId': 200,
         'className': 'Open_Play', 'value': 0.1, 'teamValue': 0.1},
        {'metricId': 0, 'eventUuid': 'regular', 'teamId': 0, 'matchId': 0, 'playerId': 0,
         'className': 'Open_Play', 'value': 0.1, 'teamValue': 0.1},
        {'metricId': 0, 'eventUuid': 'bigChance', 'teamId': 0, 'matchId': 0, 'playerId': 1,
         'className': 'Open_Play', 'value': 0.6, 'teamValue': 0.54}]

    def test_evaluate(self):
        df = pd.read_csv('../test_data/test.csv')
        events = df.replace([np.nan], [None]).to_dict('records')
        model = NaiveXg(0)
        rows = model.metric_rows(events)
        self.assertCountEqual(rows, self.expected_rows)
