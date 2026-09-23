from pathlib import Path

import numpy as np
import pytest

from mathkit.naive_bayes import MultinomialNaiveBayes, logsumexp, tokenize

DATA = Path(__file__).resolve().parents[1] / "data" / "sms_spam.tsv"

TOY_DOCS = ["free money now", "win free prize", "meet me for lunch",
            "lunch tomorrow?", "free lunch", "call me now to win"]
TOY_Y = ["spam", "spam", "ham", "ham", "ham", "spam"]


def test_tokenize():
    assert tokenize("FREE entry!! Win £1000 now") == ["free", "entry", "win", "£1000", "now"]


def test_logsumexp_is_stable():
    assert logsumexp([1000.0, 1000.0]) == pytest.approx(1000 + np.log(2))


def test_probabilities_sum_to_one():
    nb = MultinomialNaiveBayes().fit(TOY_DOCS, TOY_Y)
    P = nb.predict_proba(["free lunch now", "totally unseen words"])
    np.testing.assert_allclose(P.sum(axis=1), 1.0)


def test_hand_computed_example():
    # Worked by hand in the notebook: 2 docs per class, alpha = 1
    docs = ["free win", "free cash", "hi friend", "hi"]
    y = ["spam", "spam", "ham", "ham"]
    nb = MultinomialNaiveBayes(alpha=1).fit(docs, y)
    # vocab = {cash, free, friend, hi, win} (V = 5)
    # spam: 4 words, free=2 -> P(free|spam) = (2+1)/(4+5) = 1/3
    # ham : 3 words, free=0 -> P(free|ham)  = (0+1)/(3+5) = 1/8
    ham, spam = 0, 1
    j = nb.vocab_["free"]
    assert np.exp(nb.feature_log_prob_[spam, j]) == pytest.approx(1 / 3)
    assert np.exp(nb.feature_log_prob_[ham, j]) == pytest.approx(1 / 8)
    # P(spam | "free") = (1/2 * 1/3) / (1/2 * 1/3 + 1/2 * 1/8) = 8/11
    assert nb.predict_proba(["free"])[0, spam] == pytest.approx(8 / 11)


def test_matches_sklearn():
    sk = pytest.importorskip("sklearn.naive_bayes")
    rng = np.random.default_rng(0)
    lines = DATA.read_text(encoding="utf-8").splitlines()
    rng.shuffle(lines)
    y = np.array([l.split("\t", 1)[0] for l in lines])
    X = [l.split("\t", 1)[1] for l in lines]
    train, test = slice(0, 4000), slice(4000, None)

    mine = MultinomialNaiveBayes(alpha=1.0).fit(X[train], y[train])
    ref = sk.MultinomialNB(alpha=1.0).fit(mine.transform(X[train]), y[train])

    np.testing.assert_allclose(mine.predict_proba(X[test]),
                               ref.predict_proba(mine.transform(X[test])), atol=1e-10)
    assert (mine.predict(X[test]) == ref.predict(mine.transform(X[test]))).all()
