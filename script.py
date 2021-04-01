# Counts occurances of a specific pattern in a given string 
def pattern_count(text, pattern):
    count = 0
    for i in range(0, len(text)-len(pattern) + 1):
        if text[i:(i + len(pattern))] == pattern:
            count += 1
    return count

# Returns a frequency table of patterns from a given string
def frequency_table(text, k):
    freq_table = {}
    length = len(text)
    for i in range(0, length - k + 1):
        pattern = text[i: i + k]
        if pattern in freq_table:
            freq_table[pattern] += 1
        else:
            freq_table[pattern] = 1
    return freq_table

# Returns the largest value from a dictionary 
def max_map(dict):
    return max(dict.values())

# Returns an array of the most frequent pattern(s) in a string
def frequent_words(text, k):
    frequent_patterns = []
    freq_table = frequency_table(text, k)
    max = max_map(freq_table)
    for pattern in freq_table:
        if freq_table[pattern] == max:
            frequent_patterns.append(pattern)
    return frequent_patterns


print(frequent_words('GCGACTAAGTCTGGTAAGAGCGTAATAGTCTGGTAAAGTCTGGTAACGCGACTAAGTCCGCTCATGCGTATCGAGCGTAATAGTCTGGTAAAGTCCGCTCATGCGTATCATGCGTATCGAGCGTAATAGTCCGCTCATGCGTATCGAGCGTAATAGTCCGCTCCGCGACTACGCGACTACGCGACTAAGTCCGCTCATGCGTATCAGTCCGCTCATGCGTATCAGTCCGCTCGAGCGTAATAGTCCGCTCAGTCTGGTAACGCGACTAAGTCCGCTCATGCGTATCGAGCGTAATAGTCTGGTAAAGTCTGGTAAGAGCGTAATAGTCTGGTAAGAGCGTAATAGTCCGCTCAGTCTGGTAAAGTCCGCTCATGCGTATCGAGCGTAATATGCGTATCAGTCCGCTCCGCGACTAGAGCGTAATAGTCTGGTAAATGCGTATCATGCGTATCAGTCTGGTAAATGCGTATCAGTCTGGTAAATGCGTATCAGTCTGGTAAAGTCCGCTCGAGCGTAATAGTCCGCTCAGTCCGCTCAGTCTGGTAAGAGCGTAATAGTCTGGTAACGCGACTACGCGACTAGAGCGTAATAGTCCGCTCATGCGTATCAGTCTGGTAAAGTCCGCTCAGTCCGCTCAGTCTGGTAACGCGACTAAGTCTGGTAACGCGACTAGAGCGTAATGAGCGTAATAGTCTGGTAAATGCGTATCAGTCTGGTAAATGCGTATCCGCGACTAATGCGTATCGAGCGTAATAGTCTGGTAAGAGCGTAATCGCGACTAGAGCGTAATCGCGACTAATGCGTATCAGTCTGGTAAATGCGTATCCGCGACTACGCGACTAGAGCGTAATCGCGACTAAGTCTGGTAAGAGCGTAATAGTCTGGTAAATGCGTATCAGTCCGCTCATGCGTATCATGCGTATCCGCGACTAATGCGTATCAGTCTGGTAAATGCGTATCCGCGACTAGAGCGTAAT', 13))


