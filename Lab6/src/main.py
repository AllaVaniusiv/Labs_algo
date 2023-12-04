def boyer_moore_search(haystack, needle):
    m, n = len(needle), len(haystack)
    if m == 0 or n == 0 or m > n:
        return []

    indices = []

    # Calculate bad character shift
    bad_char_shift = {char: max(1, m - needle.rindex(char) - 1) for char in set(needle[:-1])}
    bad_char_shift[needle[-1]] = max(1, m)

    i = 0
    while i <= n - m:
        j = m - 1

        while j >= 0 and needle[j] == haystack[i + j]:
            j -= 1

        if j < 0:
            indices.append(i)
            i += 1
        else:
            i += max(1, j - bad_char_shift.get(haystack[i + j], 0))

    return indices

haystack = "ababcababcabcabc"
needle = "abc"
result = boyer_moore_search(haystack, needle)
print(f"Indexes of '{needle}' in '{haystack}': {result}")
