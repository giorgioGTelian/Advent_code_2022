def find_start_of_packet(s):
    # Initialize a list to store the most recent four characters received
    recent_chars = []

    # Iterate through the characters in the datastream buffer
    for i, c in enumerate(s):
        # Add the current character to the list of recent characters
        recent_chars.append(c)
        # If the list of recent characters has more than four elements, remove the oldest one
        if len(recent_chars) > 4:
            recent_chars.pop(0)
        # If the list of recent characters is now four characters long and all different, return the number of characters processed
        if len(recent_chars) == 4 and len(set(recent_chars)) == 4:
            return i + 1

# Example usage
print(find_start_of_packet("mjqjpqmgbljsphdztnvjfqwrcgsmlb"))  # 7
print(find_start_of_packet("bvwbjplbgvbhsrlpgdmjqwftvncz"))  # 5
print(find_start_of_packet("nppdvjthqldpwncqszvftbrmjlhg"))  # 6
print(find_start_of_packet("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"))  # 10
print(find_start_of_packet("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"))  # 11

#This solution initializes a list to store the most recent four characters received, 
#and iterates through the characters in the datastream buffer. For each character, 
#it adds it to the list of recent characters, and if the list has more than four elements, 
#it removes the oldest one. If the list of recent characters is now four characters long and 
#all different, it returns the number of characters processed.
