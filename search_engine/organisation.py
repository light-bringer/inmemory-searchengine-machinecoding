import typing

import constants
import dataset
import exceptions

class Org:

    def __init__(self, name):
        self.name = name
        self.datasets: typing.Dict[str, dataset.DataSet] = {}

    def create_dataset(self, name: str):
        if name in self.datasets:
            print(f'Dataset already exists in the Org')
            raise exceptions.EntityExistsException

        self.datasets[name] = dataset.DataSet(name)
        print(f'DataSet with {name} has been created')

    def insert_content(self, dataset_name: str, content: str):
        if dataset_name not in self.datasets:
            print(f'{dataset_name} does not exist in org')
            return

        try:
            self.datasets[dataset_name].insertDoc(content)
            print(f'Doc inserted to {dataset_name}')
        except exceptions.InconsistencyException:
            print('Contact Dev')

    def search(self, dataset_name: str, search_key: str, search_type: str):
        if search_type not in (constants.SearchOrder.COUNT, constants.SearchOrder.CREATION_TIME):
            print(f'invalid search type {search_type}')
            return

        if dataset_name not in self.datasets:
            print(f'{dataset_name} does not exist in org')
            return

        print(self.datasets[dataset_name].search(search_key, search_type))
