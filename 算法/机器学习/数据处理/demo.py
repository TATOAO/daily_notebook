from scipy.sparse import csr_matrix

"""
# from csr_matrix documentation

        csr_matrix((data, (row_ind, col_ind)), [shape=(M, N)])
            where ``data``, ``row_ind`` and ``col_ind`` satisfy the
            relationship ``a[row_ind[k], col_ind[k]] = data[k]``.

        csr_matrix((data, indices, indptr), [shape=(M, N)])
            is the standard CSR representation where the column indices for
            row i are stored in ``indices[indptr[i]:indptr[i+1]]`` and their
            corresponding values are stored in ``data[indptr[i]:indptr[i+1]]``.
            If the shape parameter is not supplied, the matrix dimensions
            are inferred from the index arrays.
"""


docs = [["hello", "world", "hello"], ["goodbye", "cruel", "world"]]
indptr = [0]
indices = []
data = []
vocabulary = {}
for d in docs:
    for term in d:
        index = vocabulary.setdefault(term, len(vocabulary))
        indices.append(index)
        data.append(1)
    indptr.append(len(indices))

"""
ipdb> data
[1, 1, 1, 1, 1, 1]
ipdb> indices
[0, 1, 0, 2, 3, 1]
ipdb> indptr
[0, 3, 6]


重复出现
0, 1, 0,  的会自动加和data

array([[2, 1, 0, 0],
        [0, 1, 1, 1]])


"""

data = [3, 1, 1, 1, 1, 1]
indices = [0, 1, 0, 2, 3, 1]
indptr = [0, 3, 6]

xxx = csr_matrix((data, indices, indptr), dtype=int).toarray()
print(xxx)
'''
[[4 1 0 0]
 [0 1 1 1]]
'''
