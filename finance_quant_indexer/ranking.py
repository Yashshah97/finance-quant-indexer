"""
Ranking algorithm implementation.
"""

class BM25:
    """
    BM25 ranking algorithm.

    Attributes:
        k1 (float): Brier parameter.
        b (float): Length normalizing parameter.
    """

    def __init__(self, k1=1.2, b=0.75):
        """
        Initialize the BM25 object.

        Args:
            k1 (float, optional): Brier parameter. Defaults to 1.2.
            b (float, optional): Length normalizing parameter. Defaults to 0.75.
        """
        self.k1 = k1
        self.b = b

    def score(self, doc_length, query_terms, term_freqs):
        """
        Calculate the BM25 score.

        Args:
            doc_length (int): Document length.
            query_terms (list[str]): Query terms.
            term_freqs (dict[str, int]): Term frequencies in the document.

        Returns:
            float: The BM25 score.
        """
        score = 0
        for term, freq in term_freqs.items():
            if term in query_terms:
                idf = self._idf(term)
                score += (self.k1 + 1) * freq / (self.k1 * (1 - self.b + self.b * doc_length / (doc_length + self.k1)) * idf)
        return score

    def _idf(self, term):
        """
        Calculate the inverse document frequency.

        Args:
            term (str): Term.

        Returns:
            float: The inverse document frequency.
        """
        # This is a very simplified version of IDF calculation
        # In real-world scenario, you would need to calculate it based on the corpus
        return 1 / len(term)


def rank_docs(doc_lengths, query_terms, term_freqs):
    """
    Rank documents.

    Args:
        doc_lengths (list[int]): Document lengths.
        query_terms (list[str]): Query terms.
        term_freqs (dict[str, dict[str, int]]): Term frequencies in each document.

    Returns:
        list[tuple[int, float]]: Ranked documents with their scores.
    """
    bm25 = BM25()
    ranked_docs = []
    for i, doc_length in enumerate(doc_lengths):
        score = bm25.score(doc_length, query_terms, term_freqs[i])
        ranked_docs.append((i, score))
    return sorted(ranked_docs, key=lambda x: x[1], reverse=True)
