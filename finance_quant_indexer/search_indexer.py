"""
Finance Quant Search Indexer - Main entry point.

This module contains the main class and functions for the finance quant search indexer.
"""

from collections import defaultdict
import re


class SearchIndexer:
    """
    Finance Quant Search Indexer.

    This class provides an inverted-index search engine with ranking functionality.
    """

    def __init__(self):
        self.index = defaultdict(list)

    def add_document(self, doc_id, text):
        """
        Add a document to the index.

        :param doc_id: Unique identifier for the document
        :param text: Text content of the document
        """
        words = re.findall(r'\b\w+\b', text.lower())
        for word in words:
            self.index[word].append(doc_id)

    def search(self, query):
        """
        Search the index for matching documents.

        :param query: Search query (text)
        :return: List of document IDs that match the query
        """
        words = re.findall(r'\b\w+\b', query.lower())
        results = set()
        for word in words:
            if word in self.index:
                results.update(self.index[word])
        return list(results)


def main():
    indexer = SearchIndexer()

    # Example usage:
    indexer.add_document('doc1', 'The quick brown fox jumps over the lazy dog')
    indexer.add_document('doc2', 'The sun was shining brightly in the clear blue sky')

    print(indexer.search('quick brown fox'))
    print(indexer.search('sun shining'))

if __name__ == '__main__':
    main()
