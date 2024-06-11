import string

# Define the blacklists
TA_BLACKLIST = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz-(\')/[]♪/%#$&\\/_"{}.}|=<>@~`'
EN_BLACKLIST = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ"#""$%&\\()*+-./:;<=>@[\\]^_`♪{|}~='

# Define the punctuation to keep
PUNCTUATION_KEEP = {'.', '!', '?'}

# Function to clean text based on a blacklist and keeping specified punctuation
def clean_text(text, blacklist, punctuation_keep):
    # Remove characters in blacklist
    text = text.lower()
    text = ''.join([char for char in text if char not in blacklist])
    # Remove punctuation except specified ones
    text = ''.join([char if char in punctuation_keep or char not in string.punctuation else ' ' for char in text])
    # Convert to lowercase
    return text.strip() + ' .\n'

# Function to read lines from a file
def read_lines(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return file.readlines()

# Function to write lines to a file
def write_lines(filename, lines):
    with open(filename, 'w', encoding='utf-8') as file:
        file.writelines(lines)

# Read lines from the input files
en_lines = read_lines('en.txt')
ta_lines = read_lines('ta.txt')

# Clean the lines
cleaned_en_lines = [clean_text(line, EN_BLACKLIST, PUNCTUATION_KEEP) for line in en_lines]
cleaned_ta_lines = [clean_text(line, TA_BLACKLIST, PUNCTUATION_KEEP) for line in ta_lines]

# Write the cleaned and deduplicated lines back to files
write_lines('cleaned_en.txt', cleaned_en_lines)
write_lines('cleaned_ta.txt', cleaned_ta_lines)

print("Cleaning and deduplication completed successfully!")