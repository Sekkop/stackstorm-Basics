from locale import normalize

from st2common.runners.base_action import Action
import json

class FilterJsonAction(Action):
    def run(self, json_data, to_exclude=[], to_include=[]):
        """
        Filter JSON data.
        Take a list of JSON objects and make all keys present in each entry

        :param json_data:
        1:return: json_Filterd_data
        """
        filtered_array = []

        for entry in json_data:
            new_entry = {}
            for key in entry:
                if key in to_exclude:
                    continue
                if len(to_include) != 0 and key not in to_include:
                    continue
                new_entry[key] = entry[key]
            filtered_array.append(new_entry)


        return filtered_array