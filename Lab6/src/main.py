def boyer_moore_search(haystack, needle):
    if not haystack or not needle:
        return []
    
    m, n = len(needle), len(haystack)

    bad_char_shift = {char: m - index - 1 for index, char in enumerate(needle[:-1])}
    bad_char_shift[needle[-1]] = m + 1 if needle[-1] not in needle[:-1] else 0

    indices = []

    i = m - 1 
    while i < n:
        j = m - 1

        while j >= 0 and needle[j] == haystack[i]:
            i -= 1
            j -= 1

        if j == -1:
            indices.append(i + 1)
        
        i += max(bad_char_shift.get(haystack[i], m), m - j)

    return indices

haystack = "ababagalamaga"
needle = "lama"
result = boyer_moore_search(haystack, needle)
print(f"Indexes of '{needle}' in '{haystack}': {result}")
