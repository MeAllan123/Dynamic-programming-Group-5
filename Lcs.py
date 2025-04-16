def get_lcs(s1, s2):
    rows, cols = len(s1), len(s2)
    table = [[0]*(cols+1) for _ in range(rows+1)]
    for i in range(rows):
        for j in range(cols):
            if s1[i] == s2[j]:
                table[i+1][j+1] = 1 + table[i][j]
            else:
                table[i+1][j+1] = max(table[i][j+1], table[i+1][j])
    return table[rows][cols]

a = "SUGARCANE"
b = "GUAVACANE"
print(get_lcs(a, b))
