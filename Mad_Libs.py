def ask_for_word(prompt):
    return input(prompt + ": ")

def mad_libs_story():
    placeholders = ["place", "plant", "texture", "emotion", "animal", "food", "noun", "number"]

    story_template = """Deep in a {place}, is a {plant}.
This {plant} was known for its {texture} appearance and its spectacular healing properties.
One day, a {emotion} {animal} came to the {place} looking for {food}.
It asked the {noun} for a {food}, but the {noun} said, "That is not available at the moment!"
The {animal} was so hungry that it took the {plant}.
As soon as it took the {plant}, {number} more grew immediately."""

    filled_story = story_template

#this is a for loop that iterates over each element in the placeholder
    
    for placeholder in placeholders:
        word = ask_for_word(f"Enter a {placeholder}")
        filled_story = filled_story.replace(f"{{{placeholder}}}", word)

    print("\nYour Mad Libs Story:\n")
    print(filled_story)

# Call the function to run the Mad Libs game
mad_libs_story()