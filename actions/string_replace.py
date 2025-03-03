from st2common.runners.base_action import Action
import json

class StringToJsonAction(Action):
    def run(self, string, match, replace):
        try:
            output = string.replace(match, replace)
        except Exception as e:
            return False, str(e)
        return True, output