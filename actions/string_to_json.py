from st2common.runners.base_action import Action
import json

class StringToJsonAction(Action):
    def run(self, data):
        try:
            json_data = json.loads(data)
        except Exception as e:
            return False, str(e)

        return True, json_data