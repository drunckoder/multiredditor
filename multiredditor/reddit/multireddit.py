import logging
import pprint
from typing import List

import praw.models

log = logging.getLogger(__name__)


class Multireddit:
    def __init__(self, multireddit: praw.models.Multireddit = None):
        self.name = multireddit.name
        self.display_name = multireddit.display_name
        self.subreddits = list(map(str, multireddit.subreddits))

        if not multireddit.can_edit:  # TODO: debug
            log.warning(f'multireddit.can_edit is False for\n'
                        f'{pprint.pformat(vars(self))}')

    def to_json(self):
        result = {
            'name': self.name,
            'display_name': self.display_name,
            'subreddits': self.subreddits
        }
        return result


def parse_multireddits(multireddits: List[praw.models.Multireddit]) -> List[Multireddit]:
    parsed_multireddits = [Multireddit(x) for x in multireddits]
    return parsed_multireddits
