import unittest
from finance_quant_indexer import ranking

class TestRanking(unittest.TestCase):
    def test_bm25_init(self):
        bm25 = ranking.BM25(k1=1.0, b=0.5)
        self.assertEqual(bm25.k1, 1.0)
        self.assertEqual(bm25.b, 0.5)

    def test_bm25_score(self):
        bm25 = ranking.BM25()
        doc_length = 10
        query_terms = ['term1', 'term2']
        term_freqs = {'term1': 5, 'term2': 3}
        score = bm25.score(doc_length, query_terms, term_freqs)
        self.assertGreater(score, 0)

    def test_bm25_idf(self):
        bm25 = ranking.BM25()
        term = 'test'
        idf = bm25._idf(term)
        self.assertEqual(idf, 1 / len(term))

    def test_rank_docs(self):
        doc_lengths = [10, 20]
        query_terms = ['term1', 'term2']
        term_freqs = [{'term1': 5, 'term2': 3}, {'term1': 6, 'term2': 4}]
        ranked_docs = ranking.rank_docs(doc_lengths, query_terms, term_freqs)
        self.assertEqual(len(ranked_docs), len(doc_lengths))

if __name__ == '__main__':
    unittest.main()
