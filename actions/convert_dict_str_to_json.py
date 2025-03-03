from st2common.runners.base_action import Action
import json

class ConvertDictStrToJsonAction(Action):
    def run(self, string):
        string = string.replace("\"", "\\\"")
        string = string.replace("\'", "\"")

        try:
            data = json.loads(string)
        except Exception as e:
            return False, str(e)

        return True, data