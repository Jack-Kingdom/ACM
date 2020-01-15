class Solution {
    // The question is very verbose and not clear what it expected. We have to modify the array as expected (*** in-place) and send back the length till you have modified.
    // I did this myself, its like of a visualisation problem. Take an example and do that way. ["a","a","b","c","c","c"]
    // See spoiler comments
    public int compress(char[] chars) {

        int inserter = 0;
        char current = chars[0];
        int count = 1;

        for(int i = 1; i < chars.length; i++) {
            if(chars[i] == current) {
                count++;
            } else {
                if(count == 1) {
                    // Inserting the character alone.
                    chars[inserter] = current;
                    inserter++;
                } else {
                    chars[inserter] = current;
                    inserter++;

                    // Insert the count as expected in the problem [For eg, 12 should be written as '1' and '2']
                    int length = String.valueOf(count).length();
                    for(int j = 0; j < length; j++) {
                        chars[inserter] = String.valueOf(count).charAt(j);
                        inserter++;
                    }
                }

                // Change current char and reset count to 1.
                current = chars[i];
                count = 1;
            }
        }

        // Do a sweep up completion after coming out of the loop. Same condition as inside the loop.
        if(count == 1) {
            chars[inserter] = current;
            inserter++;
        } else {
            chars[inserter] = current;
            inserter++;

            int length = String.valueOf(count).length();
            for(int j = 0; j < length; j++) {
                chars[inserter] = String.valueOf(count).charAt(j);
                inserter++;
            }
        }

        return inserter;
    }
}

/*
  Inserter is to keep of where to insert currently.
  current and count to keep current character in memory and its count.
*/