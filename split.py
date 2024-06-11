import random

def read_lines(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return file.readlines()

def write_lines(filename, lines):
    with open(filename, 'w', encoding='utf-8') as file:
        file.writelines(lines)

def split_data(lines, train_ratio=0.8, dev_ratio=0.1):
    total_lines = len(lines)
    indices = list(range(total_lines))
    random.shuffle(indices)

    train_end = int(total_lines * train_ratio)
    dev_end = train_end + int(total_lines * dev_ratio)

    train_indices = indices[:train_end]
    dev_indices = indices[train_end:dev_end]
    test_indices = indices[dev_end:]

    return train_indices, dev_indices, test_indices

# Read cleaned lines
cleaned_en_lines = read_lines('cleaned_en.txt')
cleaned_ta_lines = read_lines('cleaned_ta.txt')

# Ensure both files have the same number of lines
assert len(cleaned_en_lines) == len(cleaned_ta_lines), "Mismatch between number of English and Tamil lines."

# Split the data indices while maintaining correspondence
train_indices, dev_indices, test_indices = split_data(cleaned_en_lines)

# Write the split data to respective files
write_lines('data/corpus.bcn.train.en', [cleaned_en_lines[i] for i in train_indices])
write_lines('data/corpus.bcn.train.ta', [cleaned_ta_lines[i] for i in train_indices])
write_lines('data/corpus.bcn.dev.en', [cleaned_en_lines[i] for i in dev_indices])
write_lines('data/corpus.bcn.dev.ta', [cleaned_ta_lines[i] for i in dev_indices])
write_lines('data/corpus.bcn.test.en', [cleaned_en_lines[i] for i in test_indices])
write_lines('data/corpus.bcn.test.ta', [cleaned_ta_lines[i] for i in test_indices])

print("Data successfully split and saved!")