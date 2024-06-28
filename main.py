def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        report = character_report(file_contents)
        count = word_count(file_contents)
        print(report)

#Get the word count 
def word_count(book):
   words = book.split()
   count = len(words)
   return count

#Gets the number each time a character in a string
def character_report(book):
    report_dict = {}
    dict_list = []

    # Count characters
    for c in book:
        lower_c = c.lower()
        if lower_c in report_dict:
            report_dict[lower_c] += 1 
        else:
            report_dict[lower_c] = 1 

    # Create list of dictionaries
    for c in report_dict:
        if c.isalpha():
            dict_list.append({"character": c, "num": report_dict[c]})
    
    # Define sort function
    def sort_on(character_data):
        return character_data["num"]

    # Sort the list based on counts
    dict_list.sort(reverse=True, key=sort_on)

    #Printing Report 
    print("--- Begin Report ---")
    print(f"{sum(report_dict.values())} words found in this document")
    for item in dict_list:
        print(f" The'{item['character']}' was found {item['num']} times")
    print("--- End Report ---")
    

main()