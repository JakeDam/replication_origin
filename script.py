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

# Returns the reverse complement of a DNA sequence 
def reverse_complement(dna):
    complement = ''
    for base in dna:
        if (base == 'A' or base == 'a'):
            complement += 'T'
        elif (base == 'T' or base == 't'):
            complement += 'A'
        elif (base == 'C' or base == 'c'):
            complement += 'G'
        else:
            complement += 'C'
    rev_comp = complement[::-1]
    return rev_comp

# Scans a genome for a specific pattern and returns the starting index of all occurences of the pattern
def pattern_match(genome, pattern):
    indices = []
    for i in range(0, len(genome) - len(pattern) + 1):
        if genome[i: i + len(pattern)] == pattern:
            indices.append(i)
    return indices




