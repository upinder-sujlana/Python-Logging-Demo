import logging
#--------------------Logging Block-------------------------------------------------
# Create a logfile with the same name as the script name and in the same directory
# as the script.
log_filename_absolute= __file__.split(".")[0] + ".log"
# Define your handler, FileHandler is for files.
log_file_handle = logging.FileHandler(log_filename_absolute)
# Define your log message format
formatter = logging.Formatter("%(asctime)s — %(levelname)s — %(funcName)s:%(lineno)d — %(message)s")
log_file_handle.setFormatter(formatter)
# get a Logging object, add the file handle & set the logging level
logy = logging.getLogger(__name__)
logy.addHandler(log_file_handle)
logy.setLevel(logging.DEBUG)
#--------------------------------------------------------------------------------
def number_of_vowels(word):
    logy.info("Starting processing of the word")
    num_vowels=0
    for letter in word:
        logy.info(f"Checking if {letter.upper()} in the word {word.upper()} is a vowel?")
        if letter in "aeiou":
            logy.info(f"Yes {letter.upper()} is a vowel.")
            num_vowels += 1
            logy.info(f"Running count of vowels hit : {num_vowels}")
    logy.info(f"Done with the word. Good Bye!")
    return num_vowels
#--------------------------------------------------------------------------------
def main():
    user_data = input("Give me a word : ")
    vowels = number_of_vowels(user_data)
    print (f"There are {vowels} vowels in the word {user_data.upper()}")
    return
#--------------------------------------------------------------------------------
if __name__ == "__main__":
    main()
