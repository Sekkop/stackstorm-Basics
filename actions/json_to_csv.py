from locale import normalize

from st2common.runners.base_action import Action
import json

class JsonToCSVAction(Action):
    def run(self, json_data):
        """
        Normalise JSON data.
        Take a list of JSON objects and make all keys present in each entry

        :param json_data:
        1:return: json_normalised_data
        """

        all_keys = set()
        for entry in json_data:
            all_keys.update(entry.keys())

        header = ",".join(all_keys)

        file = header
        for entry in json_data:
            row = []
            for key in all_keys:
                row.append(entry.get(key, ""))
            file += ",".join(row) + "\n"

        return file