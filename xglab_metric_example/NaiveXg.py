from typing import List

from xglab_metric import Event, NumericMetric, ValuedEvent, EventType, ShotType, TeamValueStrategyType


class NaiveXg(NumericMetric):
    team_value_strategy = TeamValueStrategyType.TotalProbability

    def evaluate(self, events: List[Event]) -> List[ValuedEvent]:
        valued: List[ValuedEvent] = []
        for event in events:
            if event['type'] == EventType.Shot:
                if event['shotType'] == ShotType.Penalty:
                    valued.append(ValuedEvent(event, 0.76, 'Penalty'))
                elif event['bigChance']:
                    valued.append(ValuedEvent(event, 0.6, 'Open_Play'))
                else:
                    valued.append(ValuedEvent(event, 0.1, 'Open_Play'))
        return valued
