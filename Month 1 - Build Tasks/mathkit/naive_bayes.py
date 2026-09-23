"""Week 3 - a multinomial naive Bayes text classifier, from scratch.

In simple words
---------------
Bayes' theorem says

    P(class | message)  =  P(message | class) * P(class) / P(message)

We cannot know P(message | class) for a whole message - every message is
unique. The "naive" trick: pretend each word is chosen independently, given
the class. Then

    P(message | class)  =  product over words w of  P(w | class) ** count(w)

and those per-word probabilities are just counting:

    P(w | class) = (times w appears in that class + alpha)
                   / (total words in that class + alpha * vocabulary size)

``alpha`` (Laplace smoothing) stops one unseen word from making the whole
product zero. We work with logarithms so the product becomes a sum and very
small numbers do not underflow to 0.
"""

from __future__ import annotations

import re
from collections import Counter

import numpy as np

TOKEN_RE = re.compile(r"[a-z0-9£$']+")


def tokenize(text: str) -> list[str]:
    """Lower-case the text and split it into word-like pieces."""
    return TOKEN_RE.findall(text.lower())


def logsumexp(a, axis=None, keepdims=False):
    """log(sum(exp(a))) without overflow: pull out the max first."""
    a = np.asarray(a, dtype=float)
    m = np.max(a, axis=axis, keepdims=True)
    out = m + np.log(np.sum(np.exp(a - m), axis=axis, keepdims=True))
    return out if keepdims else np.squeeze(out, axis=axis)


class MultinomialNaiveBayes:
    def __init__(self, alpha: float = 1.0):
        if alpha <= 0:
            raise ValueError("alpha must be > 0")
        self.alpha = alpha

    # ---------------------------------------------------------------- fit
    def fit(self, docs, labels):
        labels = np.asarray(labels)
        self.classes_ = np.unique(labels)

        # 1) vocabulary: every word seen in training gets a column index
        token_lists = [tokenize(d) for d in docs]
        vocab = sorted({w for toks in token_lists for w in toks})
        self.vocab_ = {w: i for i, w in enumerate(vocab)}
        V = len(vocab)

        # 2) word counts per class,  shape (n_classes, V)
        counts = np.zeros((len(self.classes_), V))
        for toks, y in zip(token_lists, labels):
            c = np.searchsorted(self.classes_, y)
            for w, n in Counter(toks).items():
                counts[c, self.vocab_[w]] += n
        self.word_counts_ = counts

        # 3) log prior:  log P(class) = log(fraction of training messages in class)
        class_totals = np.array([(labels == c).sum() for c in self.classes_])
        self.class_log_prior_ = np.log(class_totals / class_totals.sum())

        # 4) log likelihood of each word given each class (with smoothing)
        smoothed = counts + self.alpha
        self.feature_log_prob_ = np.log(smoothed / smoothed.sum(axis=1, keepdims=True))
        return self

    # ----------------------------------------------------------- helpers
    def transform(self, docs):
        """Bag-of-words count matrix using the training vocabulary.
        Words never seen in training are ignored."""
        X = np.zeros((len(docs), len(self.vocab_)))
        for r, d in enumerate(docs):
            for w, n in Counter(tokenize(d)).items():
                j = self.vocab_.get(w)
                if j is not None:
                    X[r, j] += n
        return X

    # ----------------------------------------------------------- predict
    def joint_log_likelihood(self, docs):
        """log P(class) + sum_w count(w) * log P(w | class),  shape (n_docs, n_classes)"""
        X = self.transform(docs)
        return X @ self.feature_log_prob_.T + self.class_log_prior_

    def predict_log_proba(self, docs):
        jll = self.joint_log_likelihood(docs)
        return jll - logsumexp(jll, axis=1, keepdims=True)   # divide by P(message)

    def predict_proba(self, docs):
        return np.exp(self.predict_log_proba(docs))

    def predict(self, docs):
        return self.classes_[np.argmax(self.joint_log_likelihood(docs), axis=1)]

    # ------------------------------------------------------ explanation
    def most_indicative_words(self, positive_class, k: int = 15):
        """Words with the largest log P(w|positive) - log P(w|other)."""
        pos = int(np.searchsorted(self.classes_, positive_class))
        neg = 1 - pos
        ratio = self.feature_log_prob_[pos] - self.feature_log_prob_[neg]
        inv_vocab = {i: w for w, i in self.vocab_.items()}
        top = np.argsort(ratio)[::-1][:k]
        return [(inv_vocab[i], float(ratio[i])) for i in top]
