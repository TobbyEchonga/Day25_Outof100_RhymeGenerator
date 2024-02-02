import requests

def get_rhymes(word):
    """
    Get rhyming words for the given word using the Datamuse API.
    """
    base_url = "https://api.datamuse.com/words"
    params = {"rel_rhy": word}
    
    try:
        response = requests.get(base_url, params=params)
        rhymes_data = response.json()

        # Extract rhyming words from the API response
        rhymes = [entry['word'] for entry in rhymes_data]

        return rhymes

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return []

def main():
    # Input: Word for which rhymes are to be generated
    input_word = input("Enter a word: ")

    # Get rhyming words
    rhymes = get_rhymes(input_word)

    # Display results
    if rhymes:
        print(f"\nRhyming words for '{input_word}':")
        for rhyme in rhymes:
            print(rhyme)
    else:
        print(f"\nCould not fetch rhymes for '{input_word}'.")

if __name__ == "__main__":
    main()
