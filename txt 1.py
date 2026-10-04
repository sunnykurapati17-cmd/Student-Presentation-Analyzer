import re

print("=" * 50)
print("       STUDENT PRESENTATION ANALYZER")
print("=" * 50)

# Get presentation text
text = input("\nEnter your presentation text:\n\n")

# Remove extra spaces
text = text.strip()

if not text:
    print("Please enter some presentation text.")
    exit()

# Word count
words = text.split()
word_count = len(words)

# Sentence count
sentences = re.split(r'[.!?]+', text)
sentence_count = len([s for s in sentences if s.strip()])

# Get presentation duration
minutes = float(input("\nEnter presentation duration in minutes: "))

# Speaking speed
if minutes > 0:
    words_per_minute = word_count / minutes
else:
    words_per_minute = 0

# Filler words
filler_words = [
    "um", "uh", "like", "actually",
    "basically", "you know", "so"
]

lower_text = text.lower()

filler_count = 0

for word in filler_words:
    filler_count += len(re.findall(r'\b' + re.escape(word) + r'\b', lower_text))

# Important keywords
common_words = {
    "the", "is", "a", "an", "and", "of", "to",
    "in", "for", "on", "with", "this", "that",
    "are", "was", "were", "it", "as", "be"
}

word_frequency = {}

for word in words:
    clean_word = re.sub(r'[^a-zA-Z]', '', word.lower())

    if clean_word and clean_word not in common_words:
        word_frequency[clean_word] = word_frequency.get(clean_word, 0) + 1

# Find top keywords
keywords = sorted(
    word_frequency,
    key=word_frequency.get,
    reverse=True
)[:5]

# Display results
print("\n" + "=" * 50)
print("             ANALYSIS RESULT")
print("=" * 50)

print("Total Words       :", word_count)
print("Total Sentences   :", sentence_count)
print("Presentation Time :", minutes, "minutes")
print("Speaking Speed    :", round(words_per_minute, 2), "words/minute")
print("Filler Words      :", filler_count)

print("\nImportant Keywords:")
if keywords:
    for keyword in keywords:
        print("-", keyword)
else:
    print("No keywords found.")

# Feedback
print("\n" + "=" * 50)
print("                 FEEDBACK")
print("=" * 50)

if words_per_minute < 100:
    print("• Your speaking speed is slow. Try to speak a little faster.")
elif words_per_minute <= 160:
    print("• Good speaking speed!")
else:
    print("• Your speaking speed is fast. Try to slow down.")

if filler_count == 0:
    print("• Excellent! No common filler words detected.")
elif filler_count <= 3:
    print("• Good use of language. Try to reduce filler words slightly.")
else:
    print("• Try to reduce filler words such as 'um', 'uh', and 'like'.")

if sentence_count < 3:
    print("• Try to use more sentences to explain your topic clearly.")
else:
    print("• Good sentence structure.")

print("\nPresentation analysis completed!")