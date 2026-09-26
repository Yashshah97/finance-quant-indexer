"""
Inverted Index Data Structure.

Implementation of an inverted index as a dictionary mapping terms to lists of document IDs.
"""

class InvertedIndex:
    """
    An inverted index data structure.

    Maps terms to lists of document IDs.
    """

    def __init__(self):
        """
        Initialize the inverted index with an empty dictionary.
        """
        self.index = {}

    def add_document(self, doc_id, terms):
        """
        Add a document to the index.

        :param doc_id: Unique ID for the document
        :param terms: List of terms in the document
        """
        for term in terms:
            if term not in self.index:
                self.index[term] = []
            self.index[term].append(doc_id)

    def get_docs(self, term):
        """
        Get a list of documents containing the given term.

        :param term: Term to search for
        :return: List of document IDs
        """
        return self.index.get(term, [])

def main():
    # Example usage:
    index = InvertedIndex()
    index.add_document("doc1", ["apple", "banana"])
    index.add_document("doc2", ["banana", "orange"])

    print(index.get_docs("banana"))  # Output: ['doc1', 'doc2']

if __name__ == "__main__":
    main()
