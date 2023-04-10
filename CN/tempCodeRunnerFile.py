            s = sum([get_element_from_matrix(A, i, j) *
                    xc[j] for j in range(n) if j != i])