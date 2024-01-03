import csv

def find_matching_words():
    # Read words from words.csv into a list
    with open('words_whole_book.csv', 'r') as words_file:
        words_reader = csv.reader(words_file)
        target_words = [row[0] for row in words_reader]

    # Process tocfl.csv and write to final_list.csv
    with open('tocfl.csv', 'r') as tocfl_file, open('final_list_whole_book.csv', 'w', newline='') as final_list_file:
        tocfl_reader = csv.reader(tocfl_file)
        final_list_writer = csv.writer(final_list_file)

        # Create a set to track words that have been processed
        processed_words = set()

        for row in tocfl_reader:
            # Check if the word is in the target words list
            if row[0] in target_words:
                processed_words.add(row[0])
                # Check if the level (fourth column) is greater than 3
                if int(row[3]) > 4:
                    final_list_writer.writerow([row[0], row[1] + '\n' + '\n' + row[4], '', ''])

        # Add words not found in tocfl.csv to final_list.csv
        # for word in target_words:
        #     if word not in processed_words:
        #         # Write the word with blank spaces in other columns except the fourth
        #         final_list_writer.writerow([word, '', '', '0'])

# Call the function
find_matching_words()
