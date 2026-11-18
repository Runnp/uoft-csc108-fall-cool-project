# 1. Test Cases for is_uppercase(s)
# Parameter Value (s)	Expected Return Value	Purpose of the Test Case
# ''	                True	                Empty string
# 'ABCDEF'	            True	                All uppercase letters
# 'A123.,!A'	        False	                Contains non-alphabetic characters
# 'abcdef'	            False	                All lowercase letters
# 'AbCDEF'          	False	                Mixed uppercase and lowercase
#
#
# 2. Test Cases for odds(L)
# Parameter Value (L)	Expected Return Value	            Purpose of the Test Case
# []	                []	                                    Empty list
# [7]	                []	Single-element                      list
# [10, 20, 30, 40]	    [20, 40]	                            Even-length list
# ['a', 'b', 'c']	    ['b']	                                Odd-length list
# [10, 20, 30, 40]  	Original list unchanged	                Check that the function does not mutate its input
# [10, 20, 30, 40] using odds_v2	Original list unchanged	    Detect mutation bug in the second implementation
#
#
# 3. Test Cases for reverse(L)
# Parameter Value (L)	Expected Return Value	Purpose of the Test Case
# []	                []	                    Empty list
# [1]	                [1]	                    Single-element list
# [1, 2, 3, 4]	        [4, 3, 2, 1]	        Reverse multiple elements
# [1, 2, 3]	Original list unchanged	Check that the function does not modify its input
#
#
# 4. Test Cases for right_strip(s1, s2)
# Parameter Values (s1, s2)	    Expected Return Value	    Purpose of the Test Case
# ('', 'x')	                    ''	                        Empty string
# ('fffabcdefffgfff', 'f')	    'fffabcdefffg'	            Remove multiple trailing characters
# ('abc', 'x')	                'abc'	                    No matching trailing characters
# ('xxxx', 'x')	                ''	                        All characters match
# ('xaxxx', 'x')	            'xa'	                    Remove only trailing characters, preserving internal ones
#
#
# 5. Test Cases for reverse_in_place(L)
# Parameter Value (L)	Expected Outcome	        Purpose of the Test Case
# []	                L == [], return None	    Empty list and return value
# [1, 2, 3, 4]      	L == [4, 3, 2, 1]	        Even-length list
# [1, 2, 3]         	L == [3, 2, 1]	            Odd-length list
# ['a']                	L == ['a']	                Single-element list
