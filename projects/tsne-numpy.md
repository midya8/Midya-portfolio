# tsne-numpy

t-SNE written from scratch in NumPy. The Gaussian input affinities use
a per-point binary search on beta = 1/(2 sigma^2) that targets a given
perplexity; the output distribution is the Student-t form with one
degree of freedom; the KL divergence and its gradient,
dC/dy_i = 4 sum_j (P_ij - Q_ij)(1 + d^2)^-1 (y_i - y_j), are both
written out and checked against finite differences. The optimizer is
momentum gradient descent with early exaggeration.

Run on the sklearn digits set (1797 points): with ten neighbors, the
share of each point's input neighbors that survive into the embedding
is 0.550, against 0.121 for two-component PCA. Trustworthiness, checked
against sklearn's own implementation in the test suite, is 0.982
against PCA's 0.816.

Seven tests cover the distribution properties, the perplexity search,
the gradient, and an agreement test with sklearn's trustworthiness.

https://github.com/midya8/tsne-numpy
