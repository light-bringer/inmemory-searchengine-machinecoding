import collections
import typing

import constants
import document
import exceptions
import utils


class DataSet:
    def __init__(self, name):
        self.d_name = name
        self.__auto_id: int = 0
        self.documents: typing.Dict[int, document.Document] = {}
        self.idx: typing.Dict[str, typing.List] = collections.defaultdict(list)

    def insertDoc(self, document_content):
        self.__auto_id += 1
        doc = document.Document(self.__auto_id, content=document_content)
        if doc.get_id() in self.documents:
            raise exceptions.InconsistencyException

        self.documents[doc.get_id()] = doc

        unique_words = utils.get_unique_words_from_sentence(document_content)
        word_count = utils.get_frequency_of_words(document_content)

        for word in unique_words:
            index_dict = {
                'id': doc.get_id(),
                'count': word_count[word],
                'date': doc.creation_date(),
            }
            self.idx[word].append(index_dict)

    def __getDoc(self, doc_id):
        if doc_id not in self.documents:
            raise exceptions.InconsistencyException
        doc = self.documents[doc_id]
        return [doc.get_id(), doc.get_content()]

    def __search(self, search_str: str):
        if search_str not in self.idx:
            return []

        results = self.idx[search_str]
        return results

    def search(self, search_str, key):
        if key not in (constants.SearchOrder.COUNT, constants.SearchOrder.CREATION_TIME):
            raise exceptions.InvalidSearchParamException

        results = self.__search(search_str)
        if key == constants.SearchOrder.CREATION_TIME:
            results.sort(reverse=True, key=lambda x: x['date'])
        elif key == constants.SearchOrder.COUNT:
            results.sort(reverse=True, key=lambda x: x['count'])
        return [self.__getDoc(result['id']) for result in results]
