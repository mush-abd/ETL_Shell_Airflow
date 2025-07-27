#! /bin/bash

#Exercise 1 - Extracting data using 'cut' command

# The command below shows how to extract the first four characters.

echo "database" | cut -c1-4

#he command below shows how to extract 5th to 8th characters.
echo "database" | cut -c5-8

# The command below shows how to extract the 1st and 5th characters.
echo "database" | cut -c1,5

# The command below extracts usernames (the first field) from /etc/passwd.
cut -d":" -f1 /etc/passwd

# The command below extracts multiple fields 1st, 3rd, and 6th (username, userid, and home directory) from /etc/passwd.
cut -d":" -f1,3,6 /etc/passwd

#The command below extracts a range of fields 3rd to 6th (userid, groupid, user description and home directory) from /etc/passwd.
cut -d":" -f3-6 /etc/passwd

# Exercise 2 - Transforming data using 'tr'

# The command below translates all lower case alphabets to upper case.
echo "Shell Scripting" | tr "[a-z]" "[A-Z]"

# You could also use the pre-defined character sets also for this purpose:
echo "Shell Scripting" | tr "[:lower:]" "[:upper:]"

# The command below translates all upper case alphabets to lower case.
echo "SHELL SCRIPTING" | tr "[A-Z]" "[a-z]"

# Squeeze repeating occurrences of characters
# The -s option replaces a sequence of a repeated characters with a single occurrence of that character.
ps | tr -s " "

# Delete characters
# We can delete specified characters using the -d  option.

echo "My name is John" | tr -d "aeiou"

