def count_vowels_and_consonants(text: str) -> dict:
    vowels = "aeiouAEIOU"
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    
    count = {"unli": 0, "undosh": 0}
    
    for char in text:
        if char in vowels:
            count["unli"] += 1
        elif char in consonants:
            count["undosh"] += 1
            
    return count


print(count_vowels_and_consonants("Salom Dunyo!"))
# Kutilgan natija: {"unli": 4, "undosh": 5}