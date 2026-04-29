PRACTICE_PROBLEMS = [
    # ─── PYTHON ───────────────────────────────────────────────────────────────

    # Arrays
    {
        "pid": "py-arr-001",
        "language": "python",
        "topic": "Arrays",
        "difficulty": "Easy",
        "title": "Two Sum",
        "description": "Given an array of integers `nums` and an integer `target`, return indices of the two numbers that add up to target.",
        "input_format": "Line 1: space-separated integers\nLine 2: target integer",
        "output_format": "Two space-separated indices",
        "sample_input": "2 7 11 15\n9",
        "sample_output": "0 1",
        "test_cases": [
            {"input": "2 7 11 15\n9",  "output": "0 1"},
            {"input": "3 2 4\n6",      "output": "1 2"},
            {"input": "3 3\n6",        "output": "0 1"},
        ],
    },
    {
        "pid": "py-arr-002",
        "language": "python",
        "topic": "Arrays",
        "difficulty": "Easy",
        "title": "Maximum Subarray",
        "description": "Find the contiguous subarray with the largest sum (Kadane's Algorithm).",
        "input_format": "Space-separated integers",
        "output_format": "Maximum sum integer",
        "sample_input": "-2 1 -3 4 -1 2 1 -5 4",
        "sample_output": "6",
        "test_cases": [
            {"input": "-2 1 -3 4 -1 2 1 -5 4", "output": "6"},
            {"input": "1",                       "output": "1"},
            {"input": "5 4 -1 7 8",              "output": "23"},
        ],
    },
    {
        "pid": "py-arr-003",
        "language": "python",
        "topic": "Arrays",
        "difficulty": "Medium",
        "title": "Rotate Array",
        "description": "Rotate an array to the right by k steps.",
        "input_format": "Line 1: space-separated integers\nLine 2: k",
        "output_format": "Space-separated rotated array",
        "sample_input": "1 2 3 4 5 6 7\n3",
        "sample_output": "5 6 7 1 2 3 4",
        "test_cases": [
            {"input": "1 2 3 4 5 6 7\n3", "output": "5 6 7 1 2 3 4"},
            {"input": "-1 -100 3 99\n2",   "output": "3 99 -1 -100"},
        ],
    },

    # Strings
    {
        "pid": "py-str-001",
        "language": "python",
        "topic": "Strings",
        "difficulty": "Easy",
        "title": "Reverse String",
        "description": "Reverse the given string.",
        "input_format": "A single string",
        "output_format": "Reversed string",
        "sample_input": "hello",
        "sample_output": "olleh",
        "test_cases": [
            {"input": "hello",   "output": "olleh"},
            {"input": "Hannah",  "output": "hannaH"},
            {"input": "abcde",   "output": "edcba"},
        ],
    },
    {
        "pid": "py-str-002",
        "language": "python",
        "topic": "Strings",
        "difficulty": "Easy",
        "title": "Valid Palindrome",
        "description": "Given a string, determine if it is a palindrome (ignoring case and non-alphanumeric characters).",
        "input_format": "A single string",
        "output_format": "True or False",
        "sample_input": "A man a plan a canal Panama",
        "sample_output": "True",
        "test_cases": [
            {"input": "A man a plan a canal Panama", "output": "True"},
            {"input": "race a car",                  "output": "False"},
            {"input": " ",                            "output": "True"},
        ],
    },

    # Linked Lists
    {
        "pid": "py-ll-001",
        "language": "python",
        "topic": "Linked Lists",
        "difficulty": "Easy",
        "title": "Reverse Linked List",
        "description": "Given the head of a linked list as space-separated values, reverse it and print the values.",
        "input_format": "Space-separated integers representing list nodes",
        "output_format": "Space-separated reversed list",
        "sample_input": "1 2 3 4 5",
        "sample_output": "5 4 3 2 1",
        "test_cases": [
            {"input": "1 2 3 4 5", "output": "5 4 3 2 1"},
            {"input": "1 2",       "output": "2 1"},
            {"input": "1",         "output": "1"},
        ],
    },

    # Recursion
    {
        "pid": "py-rec-001",
        "language": "python",
        "topic": "Recursion",
        "difficulty": "Easy",
        "title": "Factorial",
        "description": "Compute n! recursively.",
        "input_format": "A single integer n",
        "output_format": "n factorial",
        "sample_input": "5",
        "sample_output": "120",
        "test_cases": [
            {"input": "5",  "output": "120"},
            {"input": "0",  "output": "1"},
            {"input": "10", "output": "3628800"},
        ],
    },
    {
        "pid": "py-rec-002",
        "language": "python",
        "topic": "Recursion",
        "difficulty": "Easy",
        "title": "Fibonacci",
        "description": "Return the nth Fibonacci number (0-indexed). fib(0)=0, fib(1)=1.",
        "input_format": "A single integer n",
        "output_format": "nth Fibonacci number",
        "sample_input": "6",
        "sample_output": "8",
        "test_cases": [
            {"input": "6",  "output": "8"},
            {"input": "0",  "output": "0"},
            {"input": "10", "output": "55"},
        ],
    },

    # Sorting
    {
        "pid": "py-sort-001",
        "language": "python",
        "topic": "Sorting",
        "difficulty": "Medium",
        "title": "Merge Sort",
        "description": "Sort an array using Merge Sort and print the sorted array.",
        "input_format": "Space-separated integers",
        "output_format": "Space-separated sorted integers",
        "sample_input": "38 27 43 3 9 82 10",
        "sample_output": "3 9 10 27 38 43 82",
        "test_cases": [
            {"input": "38 27 43 3 9 82 10", "output": "3 9 10 27 38 43 82"},
            {"input": "5 1 4 2 8",           "output": "1 2 4 5 8"},
            {"input": "1",                    "output": "1"},
        ],
    },

    # Trees
    {
        "pid": "py-tree-001",
        "language": "python",
        "topic": "Trees",
        "difficulty": "Medium",
        "title": "Binary Tree Inorder Traversal",
        "description": "Given level-order representation of a binary tree (use -1 for null), print inorder traversal.",
        "input_format": "Space-separated integers (level-order, -1 = null)",
        "output_format": "Space-separated inorder traversal",
        "sample_input": "1 -1 2 3",
        "sample_output": "1 3 2",
        "test_cases": [
            {"input": "1 -1 2 3", "output": "1 3 2"},
            {"input": "1",        "output": "1"},
            {"input": "3 1 2",    "output": "1 3 2"},
        ],
    },

    # Dynamic Programming
    {
        "pid": "py-dp-001",
        "language": "python",
        "topic": "Dynamic Programming",
        "difficulty": "Medium",
        "title": "Climbing Stairs",
        "description": "You can climb 1 or 2 steps at a time. In how many distinct ways can you climb n stairs?",
        "input_format": "A single integer n",
        "output_format": "Number of distinct ways",
        "sample_input": "3",
        "sample_output": "3",
        "test_cases": [
            {"input": "2", "output": "2"},
            {"input": "3", "output": "3"},
            {"input": "5", "output": "8"},
        ],
    },
    {
        "pid": "py-dp-002",
        "language": "python",
        "topic": "Dynamic Programming",
        "difficulty": "Hard",
        "title": "0/1 Knapsack",
        "description": "Given weights and values of n items, find max value achievable with capacity W.\nLine 1: n W\nLine 2: weights\nLine 3: values",
        "input_format": "Line 1: n W\nLine 2: space-separated weights\nLine 3: space-separated values",
        "output_format": "Maximum value",
        "sample_input": "4 8\n2 3 4 5\n3 4 5 6",
        "sample_output": "10",
        "test_cases": [
            {"input": "4 8\n2 3 4 5\n3 4 5 6",    "output": "10"},
            {"input": "3 50\n10 20 30\n60 100 120", "output": "220"},
        ],
    },

    # ─── JAVASCRIPT ───────────────────────────────────────────────────────────

    {
        "pid": "js-arr-001",
        "language": "javascript",
        "topic": "Arrays",
        "difficulty": "Easy",
        "title": "Two Sum",
        "description": "Given an array of integers and a target, return indices of the two numbers that add up to target.",
        "input_format": "Line 1: space-separated integers\nLine 2: target integer",
        "output_format": "Two space-separated indices",
        "sample_input": "2 7 11 15\n9",
        "sample_output": "0 1",
        "test_cases": [
            {"input": "2 7 11 15\n9", "output": "0 1"},
            {"input": "3 2 4\n6",     "output": "1 2"},
        ],
    },
    {
        "pid": "js-str-001",
        "language": "javascript",
        "topic": "Strings",
        "difficulty": "Easy",
        "title": "Reverse String",
        "description": "Reverse the given string.",
        "input_format": "A single string",
        "output_format": "Reversed string",
        "sample_input": "hello",
        "sample_output": "olleh",
        "test_cases": [
            {"input": "hello",  "output": "olleh"},
            {"input": "abcde",  "output": "edcba"},
        ],
    },
    {
        "pid": "js-rec-001",
        "language": "javascript",
        "topic": "Recursion",
        "difficulty": "Easy",
        "title": "Factorial",
        "description": "Compute n! recursively.",
        "input_format": "A single integer n",
        "output_format": "n factorial",
        "sample_input": "5",
        "sample_output": "120",
        "test_cases": [
            {"input": "5",  "output": "120"},
            {"input": "0",  "output": "1"},
            {"input": "10", "output": "3628800"},
        ],
    },
    {
        "pid": "js-dp-001",
        "language": "javascript",
        "topic": "Dynamic Programming",
        "difficulty": "Medium",
        "title": "Climbing Stairs",
        "description": "In how many distinct ways can you climb n stairs (1 or 2 steps at a time)?",
        "input_format": "A single integer n",
        "output_format": "Number of distinct ways",
        "sample_input": "3",
        "sample_output": "3",
        "test_cases": [
            {"input": "2", "output": "2"},
            {"input": "3", "output": "3"},
            {"input": "5", "output": "8"},
        ],
    },

    # ─── JAVA ─────────────────────────────────────────────────────────────────

    {
        "pid": "java-arr-001",
        "language": "java",
        "topic": "Arrays",
        "difficulty": "Easy",
        "title": "Two Sum",
        "description": "Given an array of integers and a target, return indices of the two numbers that add up to target.",
        "input_format": "Line 1: space-separated integers\nLine 2: target integer",
        "output_format": "Two space-separated indices",
        "sample_input": "2 7 11 15\n9",
        "sample_output": "0 1",
        "test_cases": [
            {"input": "2 7 11 15\n9", "output": "0 1"},
            {"input": "3 2 4\n6",     "output": "1 2"},
        ],
    },
    {
        "pid": "java-str-001",
        "language": "java",
        "topic": "Strings",
        "difficulty": "Easy",
        "title": "Reverse String",
        "description": "Reverse the given string.",
        "input_format": "A single string",
        "output_format": "Reversed string",
        "sample_input": "hello",
        "sample_output": "olleh",
        "test_cases": [
            {"input": "hello",  "output": "olleh"},
            {"input": "abcde",  "output": "edcba"},
        ],
    },
    {
        "pid": "java-sort-001",
        "language": "java",
        "topic": "Sorting",
        "difficulty": "Medium",
        "title": "Merge Sort",
        "description": "Sort an array using Merge Sort.",
        "input_format": "Space-separated integers",
        "output_format": "Space-separated sorted integers",
        "sample_input": "38 27 43 3 9 82 10",
        "sample_output": "3 9 10 27 38 43 82",
        "test_cases": [
            {"input": "38 27 43 3 9 82 10", "output": "3 9 10 27 38 43 82"},
            {"input": "5 1 4 2 8",           "output": "1 2 4 5 8"},
        ],
    },

    # ─── C++ ──────────────────────────────────────────────────────────────────

    {
        "pid": "cpp-arr-001",
        "language": "cpp",
        "topic": "Arrays",
        "difficulty": "Easy",
        "title": "Two Sum",
        "description": "Given an array of integers and a target, return indices of the two numbers that add up to target.",
        "input_format": "Line 1: space-separated integers\nLine 2: target integer",
        "output_format": "Two space-separated indices",
        "sample_input": "2 7 11 15\n9",
        "sample_output": "0 1",
        "test_cases": [
            {"input": "2 7 11 15\n9", "output": "0 1"},
            {"input": "3 2 4\n6",     "output": "1 2"},
        ],
    },
    {
        "pid": "cpp-dp-001",
        "language": "cpp",
        "topic": "Dynamic Programming",
        "difficulty": "Medium",
        "title": "Climbing Stairs",
        "description": "In how many distinct ways can you climb n stairs (1 or 2 steps at a time)?",
        "input_format": "A single integer n",
        "output_format": "Number of distinct ways",
        "sample_input": "3",
        "sample_output": "3",
        "test_cases": [
            {"input": "2", "output": "2"},
            {"input": "3", "output": "3"},
            {"input": "5", "output": "8"},
        ],
    },
    {
        "pid": "cpp-sort-001",
        "language": "cpp",
        "topic": "Sorting",
        "difficulty": "Medium",
        "title": "Merge Sort",
        "description": "Sort an array using Merge Sort.",
        "input_format": "Space-separated integers",
        "output_format": "Space-separated sorted integers",
        "sample_input": "38 27 43 3 9 82 10",
        "sample_output": "3 9 10 27 38 43 82",
        "test_cases": [
            {"input": "38 27 43 3 9 82 10", "output": "3 9 10 27 38 43 82"},
            {"input": "5 1 4 2 8",           "output": "1 2 4 5 8"},
        ],
    },
]









# PRACTICE_PROBLEMS = {

#     "python": {

#         "Output / Print in Python": {

#             "Very Easy": [

#                 {
#                     "id": "py-print-ve-1",
#                     "title": "Print Hello Python",

#                     "task": (
#                         "Print 'Hello Python' exactly as shown."
#                     ),

#                     "input_format": "No input.",

#                     "output_format": "Print Hello Python",

#                     "sample_input": "",

#                     "sample_output": "Hello Python",

#                     "constraints": "No constraints.",

#                     "tests": [
#                         {"input": "", "output": "Hello Python"},
#                         {"input": "", "output": "Hello Python"},
#                         {"input": "", "output": "Hello Python"}
#                     ]
#                 },

#                 {
#                     "id": "py-print-ve-2",
#                     "title": "Print Two Lines",

#                     "task": (
#                         "Print 'Python' on first line and 'Programming' on second line."
#                     ),

#                     "input_format": "No input.",

#                     "output_format": "Two lines output.",

#                     "sample_input": "",

#                     "sample_output": "Python\nProgramming",

#                     "constraints": "No constraints.",

#                     "tests": [
#                         {"input": "", "output": "Python\nProgramming"},
#                         {"input": "", "output": "Python\nProgramming"},
#                         {"input": "", "output": "Python\nProgramming"}
#                     ]
#                 },

#                 {
#                     "id": "py-print-ve-3",
#                     "title": "Print Number 100",

#                     "task": (
#                         "Print the number 100."
#                     ),

#                     "input_format": "No input.",

#                     "output_format": "Print 100.",

#                     "sample_input": "",

#                     "sample_output": "100",

#                     "constraints": "No constraints.",

#                     "tests": [
#                         {"input": "", "output": "100"},
#                         {"input": "", "output": "100"},
#                         {"input": "", "output": "100"}
#                     ]
#                 }
#             ],

#             "Easy": [

#                 {
#                     "id": "py-print-e-1",
#                     "title": "Print Sum",

#                     "task": (
#                         "Given two integers a and b, print their sum."
#                     ),

#                     "input_format": (
#                         "First line contains integer a.\n"
#                         "Second line contains integer b."
#                     ),

#                     "output_format": "Print a + b.",

#                     "sample_input": "5\n3",

#                     "sample_output": "8",

#                     "constraints": "-10^9 ≤ a, b ≤ 10^9",

#                     "tests": [
#                         {"input": "5\n3", "output": "8"},
#                         {"input": "-5\n10", "output": "5"},
#                         {"input": "0\n0", "output": "0"}
#                     ]
#                 },

#                 {
#                     "id": "py-print-e-2",
#                     "title": "Print Square",

#                     "task": (
#                         "Given integer n, print n squared."
#                     ),

#                     "input_format": "First line contains integer n.",

#                     "output_format": "Print n * n.",

#                     "sample_input": "4",

#                     "sample_output": "16",

#                     "constraints": "-10^6 ≤ n ≤ 10^6",

#                     "tests": [
#                         {"input": "4", "output": "16"},
#                         {"input": "-3", "output": "9"},
#                         {"input": "0", "output": "0"}
#                     ]
#                 },

#                 {
#                     "id": "py-print-e-3",
#                     "title": "Print Greeting",

#                     "task": (
#                         "Given string name, print 'Hello, <name>!'"
#                     ),

#                     "input_format": "First line contains string name.",

#                     "output_format": "Print greeting.",

#                     "sample_input": "joe",

#                     "sample_output": "Hello, joe!",

#                     "constraints": "1 ≤ length ≤ 100",

#                     "tests": [
#                         {"input": "joe", "output": "Hello, joe!"},
#                         {"input": "Python", "output": "Hello, Python!"},
#                         {"input": "A", "output": "Hello, A!"}
#                     ]
#                 }
#             ],

#             "Medium": [

#                 {
#                     "id": "py-print-m-1",
#                     "title": "Formatted Output",

#                     "task": (
#                         "Given integers a and b, print the following in separate lines:\n"
#                         "Sum: <sum>\n"
#                         "Product: <product>"
#                     ),

#                     "input_format": (
#                         "First line contains integer a.\n"
#                         "Second line contains integer b."
#                     ),

#                     "output_format": "Formatted output as specified.",

#                     "sample_input": "2\n3",

#                     "sample_output": "Sum: 5\nProduct: 6",

#                     "constraints": "-10^6 ≤ a, b ≤ 10^6",

#                     "tests": [
#                         {"input": "2\n3", "output": "Sum: 5\nProduct: 6"},
#                         {"input": "5\n5", "output": "Sum: 10\nProduct: 25"},
#                         {"input": "0\n10", "output": "Sum: 10\nProduct: 0"}
#                     ]
#                 },

#                 {
#                     "id": "py-print-m-2",
#                     "title": "Print Pattern",

#                     "task": (
#                         "Given integer n, print a right triangle star pattern of height n."
#                     ),

#                     "input_format": "First line contains integer n.",

#                     "output_format": "Print star pattern.",

#                     "sample_input": "3",

#                     "sample_output": "*\n**\n***",

#                     "constraints": "1 ≤ n ≤ 50",

#                     "tests": [
#                         {"input": "3", "output": "*\n**\n***"},
#                         {"input": "1", "output": "*"},
#                         {"input": "2", "output": "*\n**"}
#                     ]
#                 },

#                 {
#                     "id": "py-print-m-3",
#                     "title": "Print Multiplication Table",

#                     "task": (
#                         "Given integer n, print its multiplication table from 1 to 10."
#                     ),

#                     "input_format": "First line contains integer n.",

#                     "output_format": "Print table in format: n x i = result",

#                     "sample_input": "2",

#                     "sample_output": (
#                         "2 x 1 = 2\n"
#                         "2 x 2 = 4\n"
#                         "2 x 3 = 6\n"
#                         "2 x 4 = 8\n"
#                         "2 x 5 = 10\n"
#                         "2 x 6 = 12\n"
#                         "2 x 7 = 14\n"
#                         "2 x 8 = 16\n"
#                         "2 x 9 = 18\n"
#                         "2 x 10 = 20"
#                     ),

#                     "constraints": "1 ≤ n ≤ 1000",

#                     "tests": [
#                         {
#                             "input": "2",
#                             "output": (
#                                 "2 x 1 = 2\n"
#                                 "2 x 2 = 4\n"
#                                 "2 x 3 = 6\n"
#                                 "2 x 4 = 8\n"
#                                 "2 x 5 = 10\n"
#                                 "2 x 6 = 12\n"
#                                 "2 x 7 = 14\n"
#                                 "2 x 8 = 16\n"
#                                 "2 x 9 = 18\n"
#                                 "2 x 10 = 20"
#                             )
#                         }
#                     ]
#                 }

#             ]
#         },
#         "Variables and Datatypes": {

#             "Very Easy": [

#                 {
#                     "id": "py-var-ve-1",
#                     "title": "Print Integer",
#                     "task": ("Read an integer n and print it."),
#                     "input_format": "First line contains integer n.",
#                     "output_format": "Print n.",
#                     "sample_input": "5",
#                     "sample_output": "5",
#                     "constraints": "-10^9 ≤ n ≤ 10^9",
#                     "tests": [
#                         {"input": "5", "output": "5"},
#                         {"input": "-10", "output": "-10"},
#                         {"input": "0", "output": "0"}
#                     ]
#                 },

#                 {
#                     "id": "py-var-ve-2",
#                     "title": "Print Float",
#                     "task": ("Read a floating-point number and print it."),
#                     "input_format": "First line contains float f.",
#                     "output_format": "Print f.",
#                     "sample_input": "3.14",
#                     "sample_output": "3.14",
#                     "constraints": "-10^6 ≤ f ≤ 10^6",
#                     "tests": [
#                         {"input": "3.14", "output": "3.14"},
#                         {"input": "-2.5", "output": "-2.5"},
#                         {"input": "0.0", "output": "0.0"}
#                     ]
#                 },

#                 {
#                     "id": "py-var-ve-3",
#                     "title": "Print String",
#                     "task": ("Read a string and print it."),
#                     "input_format": "First line contains string s.",
#                     "output_format": "Print s.",
#                     "sample_input": "Python",
#                     "sample_output": "Python",
#                     "constraints": "1 ≤ length of s ≤ 10^5",
#                     "tests": [
#                         {"input": "Python", "output": "Python"},
#                         {"input": "Slashcoder", "output": "Slashcoder"},
#                         {"input": "A", "output": "A"}
#                     ]
#                 },

#                 {
#                     "id": "py-var-ve-4",
#                     "title": "Add Two Integers",
#                     "task": ("Read two integers and print their sum."),
#                     "input_format": "First line contains two space-separated integers.",
#                     "output_format": "Print sum.",
#                     "sample_input": "2 3",
#                     "sample_output": "5",
#                     "constraints": "-10^9 ≤ values ≤ 10^9",
#                     "tests": [
#                         {"input": "2 3", "output": "5"},
#                         {"input": "-5 10", "output": "5"},
#                         {"input": "0 0", "output": "0"}
#                     ]
#                 },

#                 {
#                     "id": "py-var-ve-5",
#                     "title": "Multiply Two Numbers",
#                     "task": ("Read two integers and print their product."),
#                     "input_format": "First line contains two space-separated integers.",
#                     "output_format": "Print product.",
#                     "sample_input": "4 5",
#                     "sample_output": "20",
#                     "constraints": "-10^6 ≤ values ≤ 10^6",
#                     "tests": [
#                         {"input": "4 5", "output": "20"},
#                         {"input": "-3 6", "output": "-18"},
#                         {"input": "0 10", "output": "0"}
#                     ]
#                 }

#             ],

#             "Easy": [

#                 {
#                     "id": "py-var-e-1",
#                     "title": "Swap Two Numbers",
#                     "task": ("Given two integers a and b, swap them and print the result."),
#                     "input_format": "First line contains two space-separated integers.",
#                     "output_format": "Print swapped values separated by space.",
#                     "sample_input": "5 10",
#                     "sample_output": "10 5",
#                     "constraints": "-10^9 ≤ a, b ≤ 10^9",
#                     "tests": [
#                         {"input": "5 10", "output": "10 5"},
#                         {"input": "-1 1", "output": "1 -1"},
#                         {"input": "0 0", "output": "0 0"}
#                     ]
#                 },

#                 {
#                     "id": "py-var-e-2",
#                     "title": "Length of String",
#                     "task": ("Read a string and print its length."),
#                     "input_format": "First line contains string s.",
#                     "output_format": "Print length of s.",
#                     "sample_input": "Python",
#                     "sample_output": "6",
#                     "constraints": "1 ≤ length ≤ 10^5",
#                     "tests": [
#                         {"input": "Python", "output": "6"},
#                         {"input": "A", "output": "1"},
#                         {"input": "Slashcoder", "output": "10"}
#                     ]
#                 },

#                 {
#                     "id": "py-var-e-3",
#                     "title": "Convert String to Integer",
#                     "task": ("Read a string representing an integer and print double its value."),
#                     "input_format": "First line contains string number.",
#                     "output_format": "Print doubled integer.",
#                     "sample_input": "10",
#                     "sample_output": "20",
#                     "constraints": "-10^6 ≤ value ≤ 10^6",
#                     "tests": [
#                         {"input": "10", "output": "20"},
#                         {"input": "-5", "output": "-10"},
#                         {"input": "0", "output": "0"}
#                     ]
#                 },

#                 {
#                     "id": "py-var-e-4",
#                     "title": "Boolean Conversion",
#                     "task": ("Read an integer n and print True if it is non-zero else False."),
#                     "input_format": "First line contains integer n.",
#                     "output_format": "Print True or False.",
#                     "sample_input": "5",
#                     "sample_output": "True",
#                     "constraints": "-10^9 ≤ n ≤ 10^9",
#                     "tests": [
#                         {"input": "5", "output": "True"},
#                         {"input": "0", "output": "False"},
#                         {"input": "-1", "output": "True"}
#                     ]
#                 }

#             ],

#             "Medium": [

#                 {
#                     "id": "py-var-m-1",
#                     "title": "Average of Three Numbers",
#                     "task": ("Read three integers and print their average as float."),
#                     "input_format": "First line contains three space-separated integers.",
#                     "output_format": "Print average.",
#                     "sample_input": "3 6 9",
#                     "sample_output": "6.0",
#                     "constraints": "-10^6 ≤ values ≤ 10^6",
#                     "tests": [
#                         {"input": "3 6 9", "output": "6.0"},
#                         {"input": "1 2 3", "output": "2.0"},
#                         {"input": "-3 3 0", "output": "0.0"}
#                     ]
#                 },

#                 {
#                     "id": "py-var-m-2",
#                     "title": "Formatted Output",
#                     "task": ("Given name and age, print: Name: <name>, Age: <age>"),
#                     "input_format": (
#                         "First line contains string name.\n"
#                         "Second line contains integer age."
#                     ),
#                     "output_format": "Print formatted string.",
#                     "sample_input": "sam\n21",
#                     "sample_output": "Name: sam, Age: 21",
#                     "constraints": "1 ≤ length ≤ 100",
#                     "tests": [
#                         {"input": "sam\n21", "output": "Name: sam, Age: 21"},
#                         {"input": "Python\n30", "output": "Name: Python, Age: 30"},
#                         {"input": "A\n1", "output": "Name: A, Age: 1"}
#                     ]
#                 },

#                 {
#                     "id": "py-var-m-3",
#                     "title": "Power Calculation",
#                     "task": ("Given integers a and b, print a raised to the power b."),
#                     "input_format": "First line contains two space-separated integers.",
#                     "output_format": "Print a^b.",
#                     "sample_input": "2 3",
#                     "sample_output": "8",
#                     "constraints": "-100 ≤ a ≤ 100\n0 ≤ b ≤ 10",
#                     "tests": [
#                         {"input": "2 3", "output": "8"},
#                         {"input": "5 0", "output": "1"},
#                         {"input": "-2 2", "output": "4"}
#                     ]
#                 }

#             ]
#         },

#         "Operators": {

#             "Very Easy": [

#                 {
#                     "id": "py-op-ve-1",
#                     "title": "Addition Operator",
#                     "task": ("Given two integers a and b, print a + b."),
#                     "input_format": "First line contains two space-separated integers.",
#                     "output_format": "Print the sum.",
#                     "sample_input": "2 3",
#                     "sample_output": "5",
#                     "constraints": "-10^9 ≤ a, b ≤ 10^9",
#                     "tests": [
#                         {"input": "2 3", "output": "5"},
#                         {"input": "-5 5", "output": "0"},
#                         {"input": "0 0", "output": "0"}
#                     ]
#                 },

#                 {
#                     "id": "py-op-ve-2",
#                     "title": "Subtraction Operator",
#                     "task": ("Given two integers a and b, print a - b."),
#                     "input_format": "First line contains two space-separated integers.",
#                     "output_format": "Print the difference.",
#                     "sample_input": "5 3",
#                     "sample_output": "2",
#                     "constraints": "-10^9 ≤ a, b ≤ 10^9",
#                     "tests": [
#                         {"input": "5 3", "output": "2"},
#                         {"input": "3 5", "output": "-2"},
#                         {"input": "0 0", "output": "0"}
#                     ]
#                 },

#                 {
#                     "id": "py-op-ve-3",
#                     "title": "Multiplication Operator",
#                     "task": ("Given two integers a and b, print a * b."),
#                     "input_format": "First line contains two space-separated integers.",
#                     "output_format": "Print the product.",
#                     "sample_input": "4 5",
#                     "sample_output": "20",
#                     "constraints": "-10^6 ≤ a, b ≤ 10^6",
#                     "tests": [
#                         {"input": "4 5", "output": "20"},
#                         {"input": "-2 6", "output": "-12"},
#                         {"input": "0 10", "output": "0"}
#                     ]
#                 },

#                 {
#                     "id": "py-op-ve-4",
#                     "title": "Division Operator",
#                     "task": ("Given two integers a and b, print a divided by b as float."),
#                     "input_format": "First line contains two space-separated integers.",
#                     "output_format": "Print division result.",
#                     "sample_input": "6 3",
#                     "sample_output": "2.0",
#                     "constraints": "b ≠ 0",
#                     "tests": [
#                         {"input": "6 3", "output": "2.0"},
#                         {"input": "5 2", "output": "2.5"},
#                         {"input": "-4 2", "output": "-2.0"}
#                     ]
#                 },

#                 {
#                     "id": "py-op-ve-5",
#                     "title": "Modulus Operator",
#                     "task": ("Given two integers a and b, print a % b."),
#                     "input_format": "First line contains two space-separated integers.",
#                     "output_format": "Print remainder.",
#                     "sample_input": "5 2",
#                     "sample_output": "1",
#                     "constraints": "b ≠ 0",
#                     "tests": [
#                         {"input": "5 2", "output": "1"},
#                         {"input": "10 3", "output": "1"},
#                         {"input": "7 7", "output": "0"}
#                     ]
#                 }

#             ],

#             "Easy": [

#                 {
#                     "id": "py-op-e-1",
#                     "title": "Floor Division",
#                     "task": ("Given two integers a and b, print a // b."),
#                     "input_format": "First line contains two space-separated integers.",
#                     "output_format": "Print floor division result.",
#                     "sample_input": "7 2",
#                     "sample_output": "3",
#                     "constraints": "b ≠ 0",
#                     "tests": [
#                         {"input": "7 2", "output": "3"},
#                         {"input": "9 3", "output": "3"},
#                         {"input": "-7 2", "output": "-4"}
#                     ]
#                 },

#                 {
#                     "id": "py-op-e-2",
#                     "title": "Power Operator",
#                     "task": ("Given integers a and b, print a ** b."),
#                     "input_format": "First line contains two space-separated integers.",
#                     "output_format": "Print a raised to b.",
#                     "sample_input": "2 4",
#                     "sample_output": "16",
#                     "constraints": "-100 ≤ a ≤ 100\n0 ≤ b ≤ 10",
#                     "tests": [
#                         {"input": "2 4", "output": "16"},
#                         {"input": "5 0", "output": "1"},
#                         {"input": "-2 2", "output": "4"}
#                     ]
#                 },

#                 {
#                     "id": "py-op-e-3",
#                     "title": "Comparison Check",
#                     "task": ("Given two integers a and b, print True if a > b else False."),
#                     "input_format": "First line contains two space-separated integers.",
#                     "output_format": "Print True or False.",
#                     "sample_input": "5 3",
#                     "sample_output": "True",
#                     "constraints": "-10^9 ≤ a, b ≤ 10^9",
#                     "tests": [
#                         {"input": "5 3", "output": "True"},
#                         {"input": "2 7", "output": "False"},
#                         {"input": "4 4", "output": "False"}
#                     ]
#                 },

#                 {
#                     "id": "py-op-e-4",
#                     "title": "Logical AND",
#                     "task": ("Given two integers a and b, print True if both are positive."),
#                     "input_format": "First line contains two space-separated integers.",
#                     "output_format": "Print True or False.",
#                     "sample_input": "5 3",
#                     "sample_output": "True",
#                     "constraints": "-10^9 ≤ a, b ≤ 10^9",
#                     "tests": [
#                         {"input": "5 3", "output": "True"},
#                         {"input": "-1 3", "output": "False"},
#                         {"input": "0 5", "output": "False"}
#                     ]
#                 }

#             ],

#             "Medium": [

#                 {
#                     "id": "py-op-m-1",
#                     "title": "Arithmetic Expression",
#                     "task": ("Given integers a, b, and c, compute and print a + b * c."),
#                     "input_format": "First line contains three space-separated integers.",
#                     "output_format": "Print result of expression.",
#                     "sample_input": "2 3 4",
#                     "sample_output": "14",
#                     "constraints": "-10^6 ≤ values ≤ 10^6",
#                     "tests": [
#                         {"input": "2 3 4", "output": "14"},
#                         {"input": "5 2 2", "output": "9"},
#                         {"input": "0 10 5", "output": "50"}
#                     ]
#                 },

#                 {
#                     "id": "py-op-m-2",
#                     "title": "Bitwise AND",
#                     "task": ("Given two integers a and b, print a & b."),
#                     "input_format": "First line contains two space-separated integers.",
#                     "output_format": "Print bitwise AND.",
#                     "sample_input": "5 3",
#                     "sample_output": "1",
#                     "constraints": "0 ≤ a, b ≤ 10^6",
#                     "tests": [
#                         {"input": "5 3", "output": "1"},
#                         {"input": "6 2", "output": "2"},
#                         {"input": "7 7", "output": "7"}
#                     ]
#                 },

#                 {
#                     "id": "py-op-m-3",
#                     "title": "Complex Expression",
#                     "task": ("Given integers a, b, and c, print (a + b) // c."),
#                     "input_format": "First line contains three space-separated integers.",
#                     "output_format": "Print result.",
#                     "sample_input": "10 5 3",
#                     "sample_output": "5",
#                     "constraints": "c ≠ 0",
#                     "tests": [
#                         {"input": "10 5 3", "output": "5"},
#                         {"input": "9 3 4", "output": "3"},
#                         {"input": "8 4 2", "output": "6"}
#                     ]
#                 }

#             ]
#         },

#         "Strings": {

#             "Very Easy": [

#                 {
#                     "id": "py-str-ve-1",
#                     "title": "Print String Length",
#                     "task": ("Given a string s, print its length."),
#                     "input_format": "First line contains string s.",
#                     "output_format": "Print length of s.",
#                     "sample_input": "Python",
#                     "sample_output": "6",
#                     "constraints": "1 ≤ length of s ≤ 10^5",
#                     "tests": [
#                         {"input": "Python", "output": "6"},
#                         {"input": "A", "output": "1"},
#                         {"input": "Slashcoder", "output": "10"}
#                     ]
#                 },

#                 {
#                     "id": "py-str-ve-2",
#                     "title": "Print First Character",
#                     "task": ("Given a string s, print its first character."),
#                     "input_format": "First line contains string s.",
#                     "output_format": "Print first character.",
#                     "sample_input": "Code",
#                     "sample_output": "C",
#                     "constraints": "1 ≤ length of s ≤ 10^5",
#                     "tests": [
#                         {"input": "Code", "output": "C"},
#                         {"input": "A", "output": "A"},
#                         {"input": "Python", "output": "P"}
#                     ]
#                 },

#                 {
#                     "id": "py-str-ve-3",
#                     "title": "Print Last Character",
#                     "task": ("Given a string s, print its last character."),
#                     "input_format": "First line contains string s.",
#                     "output_format": "Print last character.",
#                     "sample_input": "Code",
#                     "sample_output": "e",
#                     "constraints": "1 ≤ length of s ≤ 10^5",
#                     "tests": [
#                         {"input": "Code", "output": "e"},
#                         {"input": "A", "output": "A"},
#                         {"input": "Python", "output": "n"}
#                     ]
#                 },

#                 {
#                     "id": "py-str-ve-4",
#                     "title": "Convert to Uppercase",
#                     "task": ("Given a string s, print it in uppercase."),
#                     "input_format": "First line contains string s.",
#                     "output_format": "Print uppercase string.",
#                     "sample_input": "python",
#                     "sample_output": "PYTHON",
#                     "constraints": "1 ≤ length ≤ 10^5",
#                     "tests": [
#                         {"input": "python", "output": "PYTHON"},
#                         {"input": "Code123", "output": "CODE123"},
#                         {"input": "aBc", "output": "ABC"}
#                     ]
#                 },

#                 {
#                     "id": "py-str-ve-5",
#                     "title": "Convert to Lowercase",
#                     "task": ("Given a string s, print it in lowercase."),
#                     "input_format": "First line contains string s.",
#                     "output_format": "Print lowercase string.",
#                     "sample_input": "PYTHON",
#                     "sample_output": "python",
#                     "constraints": "1 ≤ length ≤ 10^5",
#                     "tests": [
#                         {"input": "PYTHON", "output": "python"},
#                         {"input": "Code123", "output": "code123"},
#                         {"input": "AbC", "output": "abc"}
#                     ]
#                 },

#                 {
#                     "id": "py-str-ve-6",
#                     "title": "Concatenate Two Strings",
#                     "task": ("Given two strings s1 and s2, print their concatenation."),
#                     "input_format": (
#                         "First line contains string s1.\n"
#                         "Second line contains string s2."
#                     ),
#                     "output_format": "Print concatenated string.",
#                     "sample_input": "Hello\nWorld",
#                     "sample_output": "HelloWorld",
#                     "constraints": "1 ≤ length ≤ 10^5",
#                     "tests": [
#                         {"input": "Hello\nWorld", "output": "HelloWorld"},
#                         {"input": "A\nB", "output": "AB"},
#                         {"input": "Slash\nCoder", "output": "SlashCoder"}
#                     ]
#                 }

#             ],

#             "Easy": [

#                 {
#                     "id": "py-str-e-1",
#                     "title": "Reverse String",
#                     "task": ("Given a string s, print the reversed string."),
#                     "input_format": "First line contains string s.",
#                     "output_format": "Print reversed string.",
#                     "sample_input": "Python",
#                     "sample_output": "nohtyP",
#                     "constraints": "1 ≤ length ≤ 10^5",
#                     "tests": [
#                         {"input": "Python", "output": "nohtyP"},
#                         {"input": "A", "output": "A"},
#                         {"input": "abc123", "output": "321cba"}
#                     ]
#                 },

#                 {
#                     "id": "py-str-e-2",
#                     "title": "Count Vowels",
#                     "task": ("Given a string s, count the number of vowels."),
#                     "input_format": "First line contains string s.",
#                     "output_format": "Print vowel count.",
#                     "sample_input": "Education",
#                     "sample_output": "5",
#                     "constraints": "1 ≤ length ≤ 10^5",
#                     "tests": [
#                         {"input": "Education", "output": "5"},
#                         {"input": "bcdfg", "output": "0"},
#                         {"input": "AEIOU", "output": "5"}
#                     ]
#                 },

#                 {
#                     "id": "py-str-e-3",
#                     "title": "Check Substring",
#                     "task": ("Given strings s and sub, print True if sub exists in s else False."),
#                     "input_format": (
#                         "First line contains string s.\n"
#                         "Second line contains string sub."
#                     ),
#                     "output_format": "Print True or False.",
#                     "sample_input": "Python Programming\nthon",
#                     "sample_output": "True",
#                     "constraints": "1 ≤ length ≤ 10^5",
#                     "tests": [
#                         {"input": "Python Programming\nthon", "output": "True"},
#                         {"input": "Hello\nxyz", "output": "False"},
#                         {"input": "abcabc\nabc", "output": "True"}
#                     ]
#                 },

#                 {
#                     "id": "py-str-e-4",
#                     "title": "Remove Spaces",
#                     "task": ("Given a string s, remove all spaces and print the result."),
#                     "input_format": "First line contains string s.",
#                     "output_format": "Print string without spaces.",
#                     "sample_input": "Hello World",
#                     "sample_output": "HelloWorld",
#                     "constraints": "1 ≤ length ≤ 10^5",
#                     "tests": [
#                         {"input": "Hello World", "output": "HelloWorld"},
#                         {"input": "A B C", "output": "ABC"},
#                         {"input": "NoSpaces", "output": "NoSpaces"}
#                     ]
#                 }

#             ],

#             "Medium": [

#                 {
#                     "id": "py-str-m-1",
#                     "title": "Palindrome Check",
#                     "task": ("Given a string s, print True if it is a palindrome else False."),
#                     "input_format": "First line contains string s.",
#                     "output_format": "Print True or False.",
#                     "sample_input": "madam",
#                     "sample_output": "True",
#                     "constraints": "1 ≤ length ≤ 10^5",
#                     "tests": [
#                         {"input": "madam", "output": "True"},
#                         {"input": "python", "output": "False"},
#                         {"input": "racecar", "output": "True"}
#                     ]
#                 },

#                 {
#                     "id": "py-str-m-2",
#                     "title": "Character Frequency",
#                     "task": ("Given string s and character c, print how many times c appears in s."),
#                     "input_format": (
#                         "First line contains string s.\n"
#                         "Second line contains character c."
#                     ),
#                     "output_format": "Print frequency.",
#                     "sample_input": "banana\na",
#                     "sample_output": "3",
#                     "constraints": "1 ≤ length ≤ 10^5",
#                     "tests": [
#                         {"input": "banana\na", "output": "3"},
#                         {"input": "Python\no", "output": "1"},
#                         {"input": "abc\nz", "output": "0"}
#                     ]
#                 },

#                 {
#                     "id": "py-str-m-3",
#                     "title": "Capitalize Each Word",
#                     "task": ("Given a sentence, capitalize the first letter of each word."),
#                     "input_format": "First line contains sentence.",
#                     "output_format": "Print capitalized sentence.",
#                     "sample_input": "hello world",
#                     "sample_output": "Hello World",
#                     "constraints": "1 ≤ length ≤ 10^5",
#                     "tests": [
#                         {"input": "hello world", "output": "Hello World"},
#                         {"input": "python programming", "output": "Python Programming"},
#                         {"input": "a b c", "output": "A B C"}
#                     ]
#                 }

#             ]
#         },

#         "Conditional Statements": {

#             "Very Easy": [

#                 {
#                     "id": "py-cond-ve-1",
#                     "title": "Check Positive",
#                     "task": ("Given an integer n, print 'Positive' if n > 0."),
#                     "input_format": "First line contains integer n.",
#                     "output_format": "Print Positive if condition satisfied.",
#                     "sample_input": "5",
#                     "sample_output": "Positive",
#                     "constraints": "-10^9 ≤ n ≤ 10^9",
#                     "tests": [
#                         {"input": "5", "output": "Positive"},
#                         {"input": "10", "output": "Positive"},
#                         {"input": "1", "output": "Positive"}
#                     ]
#                 },

#                 {
#                     "id": "py-cond-ve-2",
#                     "title": "Check Negative",
#                     "task": ("Given an integer n, print 'Negative' if n < 0."),
#                     "input_format": "First line contains integer n.",
#                     "output_format": "Print Negative if condition satisfied.",
#                     "sample_input": "-5",
#                     "sample_output": "Negative",
#                     "constraints": "-10^9 ≤ n ≤ 10^9",
#                     "tests": [
#                         {"input": "-5", "output": "Negative"},
#                         {"input": "-1", "output": "Negative"},
#                         {"input": "-100", "output": "Negative"}
#                     ]
#                 },

#                 {
#                     "id": "py-cond-ve-3",
#                     "title": "Check Zero",
#                     "task": ("Given integer n, print 'Zero' if n == 0."),
#                     "input_format": "First line contains integer n.",
#                     "output_format": "Print Zero if condition satisfied.",
#                     "sample_input": "0",
#                     "sample_output": "Zero",
#                     "constraints": "-10^9 ≤ n ≤ 10^9",
#                     "tests": [
#                         {"input": "0", "output": "Zero"},
#                         {"input": "0", "output": "Zero"},
#                         {"input": "0", "output": "Zero"}
#                     ]
#                 },

#                 {
#                     "id": "py-cond-ve-4",
#                     "title": "Even Number",
#                     "task": ("Given integer n, print 'Even' if n is even."),
#                     "input_format": "First line contains integer n.",
#                     "output_format": "Print Even if condition satisfied.",
#                     "sample_input": "4",
#                     "sample_output": "Even",
#                     "constraints": "-10^9 ≤ n ≤ 10^9",
#                     "tests": [
#                         {"input": "4", "output": "Even"},
#                         {"input": "10", "output": "Even"},
#                         {"input": "0", "output": "Even"}
#                     ]
#                 },

#                 {
#                     "id": "py-cond-ve-5",
#                     "title": "Odd Number",
#                     "task": ("Given integer n, print 'Odd' if n is odd."),
#                     "input_format": "First line contains integer n.",
#                     "output_format": "Print Odd if condition satisfied.",
#                     "sample_input": "3",
#                     "sample_output": "Odd",
#                     "constraints": "-10^9 ≤ n ≤ 10^9",
#                     "tests": [
#                         {"input": "3", "output": "Odd"},
#                         {"input": "5", "output": "Odd"},
#                         {"input": "-7", "output": "Odd"}
#                     ]
#                 },

#                 {
#                     "id": "py-cond-ve-6",
#                     "title": "Greater Than 10",
#                     "task": ("Given integer n, print 'Yes' if n > 10."),
#                     "input_format": "First line contains integer n.",
#                     "output_format": "Print Yes if condition satisfied.",
#                     "sample_input": "15",
#                     "sample_output": "Yes",
#                     "constraints": "-10^9 ≤ n ≤ 10^9",
#                     "tests": [
#                         {"input": "15", "output": "Yes"},
#                         {"input": "100", "output": "Yes"},
#                         {"input": "11", "output": "Yes"}
#                     ]
#                 },

#                 {
#                     "id": "py-cond-ve-7",
#                     "title": "Less Than 100",
#                     "task": ("Given integer n, print 'Small' if n < 100."),
#                     "input_format": "First line contains integer n.",
#                     "output_format": "Print Small if condition satisfied.",
#                     "sample_input": "50",
#                     "sample_output": "Small",
#                     "constraints": "-10^9 ≤ n ≤ 10^9",
#                     "tests": [
#                         {"input": "50", "output": "Small"},
#                         {"input": "0", "output": "Small"},
#                         {"input": "-10", "output": "Small"}
#                     ]
#                 }

#             ],

#             "Easy": [

#                 {
#                     "id": "py-cond-e-1",
#                     "title": "Largest of Two Numbers",
#                     "task": ("Given two integers a and b, print the larger number."),
#                     "input_format": "First line contains two space-separated integers.",
#                     "output_format": "Print the larger number.",
#                     "sample_input": "5 9",
#                     "sample_output": "9",
#                     "constraints": "-10^9 ≤ a, b ≤ 10^9",
#                     "tests": [
#                         {"input": "5 9", "output": "9"},
#                         {"input": "10 2", "output": "10"},
#                         {"input": "-1 -5", "output": "-1"}
#                     ]
#                 },

#                 {
#                     "id": "py-cond-e-2",
#                     "title": "Eligible to Vote",
#                     "task": ("Given age, print 'Eligible' if age >= 18 else 'Not Eligible'."),
#                     "input_format": "First line contains integer age.",
#                     "output_format": "Print result.",
#                     "sample_input": "20",
#                     "sample_output": "Eligible",
#                     "constraints": "0 ≤ age ≤ 120",
#                     "tests": [
#                         {"input": "20", "output": "Eligible"},
#                         {"input": "17", "output": "Not Eligible"},
#                         {"input": "18", "output": "Eligible"}
#                     ]
#                 },

#                 {
#                     "id": "py-cond-e-3",
#                     "title": "Pass or Fail",
#                     "task": ("Given marks, print 'Pass' if marks >= 40 else 'Fail'."),
#                     "input_format": "First line contains integer marks.",
#                     "output_format": "Print result.",
#                     "sample_input": "45",
#                     "sample_output": "Pass",
#                     "constraints": "0 ≤ marks ≤ 100",
#                     "tests": [
#                         {"input": "45", "output": "Pass"},
#                         {"input": "39", "output": "Fail"},
#                         {"input": "40", "output": "Pass"}
#                     ]
#                 },

#                 {
#                     "id": "py-cond-e-4",
#                     "title": "Check Divisible by 5",
#                     "task": ("Given integer n, print 'Yes' if divisible by 5 else 'No'."),
#                     "input_format": "First line contains integer n.",
#                     "output_format": "Print Yes or No.",
#                     "sample_input": "10",
#                     "sample_output": "Yes",
#                     "constraints": "-10^9 ≤ n ≤ 10^9",
#                     "tests": [
#                         {"input": "10", "output": "Yes"},
#                         {"input": "7", "output": "No"},
#                         {"input": "0", "output": "Yes"}
#                     ]
#                 },

#                 {
#                     "id": "py-cond-e-5",
#                     "title": "Number Range",
#                     "task": ("Given integer n, print 'In Range' if 10 ≤ n ≤ 50 else 'Out of Range'."),
#                     "input_format": "First line contains integer n.",
#                     "output_format": "Print result.",
#                     "sample_input": "25",
#                     "sample_output": "In Range",
#                     "constraints": "-10^9 ≤ n ≤ 10^9",
#                     "tests": [
#                         {"input": "25", "output": "In Range"},
#                         {"input": "5", "output": "Out of Range"},
#                         {"input": "50", "output": "In Range"}
#                     ]
#                 }

#             ],

#             "Medium": [

#                 {
#                     "id": "py-cond-m-1",
#                     "title": "Largest of Three Numbers",
#                     "task": ("Given three integers, print the largest."),
#                     "input_format": "First line contains three space-separated integers.",
#                     "output_format": "Print largest number.",
#                     "sample_input": "3 9 5",
#                     "sample_output": "9",
#                     "constraints": "-10^9 ≤ values ≤ 10^9",
#                     "tests": [
#                         {"input": "3 9 5", "output": "9"},
#                         {"input": "10 2 1", "output": "10"},
#                         {"input": "-1 -5 -3", "output": "-1"}
#                     ]
#                 },

#                 {
#                     "id": "py-cond-m-2",
#                     "title": "Leap Year",
#                     "task": ("Given year, print 'Leap Year' if it is a leap year else 'Not Leap Year'."),
#                     "input_format": "First line contains integer year.",
#                     "output_format": "Print result.",
#                     "sample_input": "2020",
#                     "sample_output": "Leap Year",
#                     "constraints": "1 ≤ year ≤ 10^5",
#                     "tests": [
#                         {"input": "2020", "output": "Leap Year"},
#                         {"input": "1900", "output": "Not Leap Year"},
#                         {"input": "2000", "output": "Leap Year"}
#                     ]
#                 },

#                 {
#                     "id": "py-cond-m-3",
#                     "title": "Grade Calculator",
#                     "task": ("Given marks, print Grade A if >=90, B if >=75, C if >=50, else D."),
#                     "input_format": "First line contains integer marks.",
#                     "output_format": "Print grade.",
#                     "sample_input": "85",
#                     "sample_output": "B",
#                     "constraints": "0 ≤ marks ≤ 100",
#                     "tests": [
#                         {"input": "95", "output": "A"},
#                         {"input": "80", "output": "B"},
#                         {"input": "60", "output": "C"},
#                         {"input": "30", "output": "D"}
#                     ]
#                 },

#                 {
#                     "id": "py-cond-m-4",
#                     "title": "Triangle Validity",
#                     "task": ("Given three sides a, b, c, print 'Valid' if they can form a triangle else 'Invalid'."),
#                     "input_format": "First line contains three space-separated integers.",
#                     "output_format": "Print Valid or Invalid.",
#                     "sample_input": "3 4 5",
#                     "sample_output": "Valid",
#                     "constraints": "1 ≤ values ≤ 10^6",
#                     "tests": [
#                         {"input": "3 4 5", "output": "Valid"},
#                         {"input": "1 2 3", "output": "Invalid"},
#                         {"input": "5 5 5", "output": "Valid"}
#                     ]
#                 }

#             ]
#         },

#         "Lists": {

#             "Very Easy": [

#                 {
#                     "id": "py-list-ve-1",
#                     "title": "Print List Length",
#                     "task": "Given a list of integers, print its length.",
#                     "input_format": "First line contains space-separated integers.",
#                     "output_format": "Print length of list.",
#                     "sample_input": "1 2 3 4",
#                     "sample_output": "4",
#                     "constraints": "1 ≤ size ≤ 10^5",
#                     "tests": [
#                         {"input": "1 2 3 4", "output": "4"},
#                         {"input": "5", "output": "1"},
#                         {"input": "10 20", "output": "2"}
#                     ]
#                 },

#                 {
#                     "id": "py-list-ve-2",
#                     "title": "Print First Element",
#                     "task": "Print the first element of the list.",
#                     "input_format": "First line contains space-separated integers.",
#                     "output_format": "Print first element.",
#                     "sample_input": "5 6 7",
#                     "sample_output": "5",
#                     "constraints": "List size ≥ 1",
#                     "tests": [
#                         {"input": "5 6 7", "output": "5"},
#                         {"input": "10", "output": "10"},
#                         {"input": "-1 2 3", "output": "-1"}
#                     ]
#                 },

#                 {
#                     "id": "py-list-ve-3",
#                     "title": "Print Last Element",
#                     "task": "Print the last element of the list.",
#                     "input_format": "First line contains space-separated integers.",
#                     "output_format": "Print last element.",
#                     "sample_input": "5 6 7",
#                     "sample_output": "7",
#                     "constraints": "List size ≥ 1",
#                     "tests": [
#                         {"input": "5 6 7", "output": "7"},
#                         {"input": "10", "output": "10"},
#                         {"input": "-1 2 3", "output": "3"}
#                     ]
#                 },

#                 {
#                     "id": "py-list-ve-4",
#                     "title": "Sum of List",
#                     "task": "Given a list of integers, print the sum.",
#                     "input_format": "First line contains space-separated integers.",
#                     "output_format": "Print sum.",
#                     "sample_input": "1 2 3",
#                     "sample_output": "6",
#                     "constraints": "1 ≤ size ≤ 10^5",
#                     "tests": [
#                         {"input": "1 2 3", "output": "6"},
#                         {"input": "5", "output": "5"},
#                         {"input": "-1 1", "output": "0"}
#                     ]
#                 },

#                 {
#                     "id": "py-list-ve-5",
#                     "title": "Maximum Element",
#                     "task": "Print maximum element of the list.",
#                     "input_format": "Space-separated integers.",
#                     "output_format": "Print maximum.",
#                     "sample_input": "1 5 3",
#                     "sample_output": "5",
#                     "constraints": "1 ≤ size ≤ 10^5",
#                     "tests": [
#                         {"input": "1 5 3", "output": "5"},
#                         {"input": "-1 -5 -3", "output": "-1"},
#                         {"input": "10", "output": "10"}
#                     ]
#                 },

#                 {
#                     "id": "py-list-ve-6",
#                     "title": "Minimum Element",
#                     "task": "Print minimum element of the list.",
#                     "input_format": "Space-separated integers.",
#                     "output_format": "Print minimum.",
#                     "sample_input": "1 5 3",
#                     "sample_output": "1",
#                     "constraints": "1 ≤ size ≤ 10^5",
#                     "tests": [
#                         {"input": "1 5 3", "output": "1"},
#                         {"input": "-1 -5 -3", "output": "-5"},
#                         {"input": "10", "output": "10"}
#                     ]
#                 },

#                 {
#                     "id": "py-list-ve-7",
#                     "title": "Count Elements",
#                     "task": "Print number of elements in list.",
#                     "input_format": "Space-separated integers.",
#                     "output_format": "Print count.",
#                     "sample_input": "1 2 3",
#                     "sample_output": "3",
#                     "constraints": "1 ≤ size ≤ 10^5",
#                     "tests": [
#                         {"input": "1 2 3", "output": "3"},
#                         {"input": "9", "output": "1"},
#                         {"input": "5 6", "output": "2"}
#                     ]
#                 },

#                 {
#                     "id": "py-list-ve-8",
#                     "title": "Print Sorted List",
#                     "task": "Print list in ascending order.",
#                     "input_format": "Space-separated integers.",
#                     "output_format": "Print sorted list separated by space.",
#                     "sample_input": "3 1 2",
#                     "sample_output": "1 2 3",
#                     "constraints": "1 ≤ size ≤ 10^5",
#                     "tests": [
#                         {"input": "3 1 2", "output": "1 2 3"},
#                         {"input": "5 4 3", "output": "3 4 5"},
#                         {"input": "1", "output": "1"}
#                     ]
#                 },

#                 {
#                     "id": "py-list-ve-9",
#                     "title": "Print Reversed List",
#                     "task": "Print list in reverse order.",
#                     "input_format": "Space-separated integers.",
#                     "output_format": "Print reversed list.",
#                     "sample_input": "1 2 3",
#                     "sample_output": "3 2 1",
#                     "constraints": "1 ≤ size ≤ 10^5",
#                     "tests": [
#                         {"input": "1 2 3", "output": "3 2 1"},
#                         {"input": "5", "output": "5"},
#                         {"input": "9 8", "output": "8 9"}
#                     ]
#                 },

#                 {
#                     "id": "py-list-ve-10",
#                     "title": "Check Element Exists",
#                     "task": "Given list and number x, print True if x exists else False.",
#                     "input_format": "First line list. Second line integer x.",
#                     "output_format": "Print True or False.",
#                     "sample_input": "1 2 3\n2",
#                     "sample_output": "True",
#                     "constraints": "1 ≤ size ≤ 10^5",
#                     "tests": [
#                         {"input": "1 2 3\n2", "output": "True"},
#                         {"input": "1 2 3\n5", "output": "False"},
#                         {"input": "5\n5", "output": "True"}
#                     ]
#                 },

#                 {
#                     "id": "py-list-ve-11",
#                     "title": "Count Occurrences",
#                     "task": "Given list and number x, print number of times x appears.",
#                     "input_format": "First line list. Second line x.",
#                     "output_format": "Print count.",
#                     "sample_input": "1 2 2 3\n2",
#                     "sample_output": "2",
#                     "constraints": "1 ≤ size ≤ 10^5",
#                     "tests": [
#                         {"input": "1 2 2 3\n2", "output": "2"},
#                         {"input": "5 5 5\n5", "output": "3"},
#                         {"input": "1 2 3\n4", "output": "0"}
#                     ]
#                 },

#                 {
#                     "id": "py-list-ve-12",
#                     "title": "Multiply All Elements",
#                     "task": "Print product of all elements in list.",
#                     "input_format": "Space-separated integers.",
#                     "output_format": "Print product.",
#                     "sample_input": "1 2 3",
#                     "sample_output": "6",
#                     "constraints": "1 ≤ size ≤ 10^4",
#                     "tests": [
#                         {"input": "1 2 3", "output": "6"},
#                         {"input": "5", "output": "5"},
#                         {"input": "2 2 2", "output": "8"}
#                     ]
#                 }

#             ],

#             "Easy": [

#                 {
#                     "id": "py-list-e-1",
#                     "title": "Remove Duplicates",
#                     "task": "Remove duplicates and print unique elements.",
#                     "input_format": "Space-separated integers.",
#                     "output_format": "Print unique elements.",
#                     "sample_input": "1 2 2 3",
#                     "sample_output": "1 2 3",
#                     "constraints": "1 ≤ size ≤ 10^5",
#                     "tests": [
#                         {"input": "1 2 2 3", "output": "1 2 3"},
#                         {"input": "5 5 5", "output": "5"},
#                         {"input": "1 2 3", "output": "1 2 3"}
#                     ]
#                 },

#                 {
#                     "id": "py-list-e-2",
#                     "title": "Second Largest",
#                     "task": "Print second largest element in list.",
#                     "input_format": "Space-separated integers.",
#                     "output_format": "Print second largest.",
#                     "sample_input": "1 5 3",
#                     "sample_output": "3",
#                     "constraints": "List size ≥ 2",
#                     "tests": [
#                         {"input": "1 5 3", "output": "3"},
#                         {"input": "10 20", "output": "10"},
#                         {"input": "4 4 5", "output": "4"}
#                     ]
#                 },

#                 {
#                     "id": "py-list-e-3",
#                     "title": "Sum of Even Numbers",
#                     "task": "Print sum of even numbers in list.",
#                     "input_format": "Space-separated integers.",
#                     "output_format": "Print sum.",
#                     "sample_input": "1 2 3 4",
#                     "sample_output": "6",
#                     "constraints": "1 ≤ size ≤ 10^5",
#                     "tests": [
#                         {"input": "1 2 3 4", "output": "6"},
#                         {"input": "2 4 6", "output": "12"},
#                         {"input": "1 3 5", "output": "0"}
#                     ]
#                 },

#                 {
#                     "id": "py-list-e-4",
#                     "title": "Rotate Left by One",
#                     "task": "Rotate list left by one position.",
#                     "input_format": "Space-separated integers.",
#                     "output_format": "Print rotated list.",
#                     "sample_input": "1 2 3",
#                     "sample_output": "2 3 1",
#                     "constraints": "1 ≤ size ≤ 10^5",
#                     "tests": [
#                         {"input": "1 2 3", "output": "2 3 1"},
#                         {"input": "5", "output": "5"},
#                         {"input": "4 5 6 7", "output": "5 6 7 4"}
#                     ]
#                 },

#                 {
#                     "id": "py-list-e-5",
#                     "title": "Rotate Right by One",
#                     "task": "Rotate list right by one position.",
#                     "input_format": "Space-separated integers.",
#                     "output_format": "Print rotated list.",
#                     "sample_input": "1 2 3",
#                     "sample_output": "3 1 2",
#                     "constraints": "1 ≤ size ≤ 10^5",
#                     "tests": [
#                         {"input": "1 2 3", "output": "3 1 2"},
#                         {"input": "5", "output": "5"},
#                         {"input": "4 5 6 7", "output": "7 4 5 6"}
#                     ]
#                 },

#                 {
#                     "id": "py-list-e-6",
#                     "title": "Find Index of Element",
#                     "task": "Given list and x, print index of x (0-based).",
#                     "input_format": "First line list. Second line x.",
#                     "output_format": "Print index.",
#                     "sample_input": "1 2 3\n2",
#                     "sample_output": "1",
#                     "constraints": "Element exists.",
#                     "tests": [
#                         {"input": "1 2 3\n2", "output": "1"},
#                         {"input": "5 6 7\n7", "output": "2"},
#                         {"input": "10 20\n10", "output": "0"}
#                     ]
#                 },

#                 {
#                     "id": "py-list-e-7",
#                     "title": "Merge Two Lists",
#                     "task": "Merge two lists and print result.",
#                     "input_format": "First line list1. Second line list2.",
#                     "output_format": "Print merged list.",
#                     "sample_input": "1 2\n3 4",
#                     "sample_output": "1 2 3 4",
#                     "constraints": "1 ≤ size ≤ 10^5",
#                     "tests": [
#                         {"input": "1 2\n3 4", "output": "1 2 3 4"},
#                         {"input": "5\n6 7", "output": "5 6 7"},
#                         {"input": "1\n2", "output": "1 2"}
#                     ]
#                 },

#                 {
#                     "id": "py-list-e-8",
#                     "title": "Check Sorted",
#                     "task": "Print True if list is sorted ascending else False.",
#                     "input_format": "Space-separated integers.",
#                     "output_format": "Print True or False.",
#                     "sample_input": "1 2 3",
#                     "sample_output": "True",
#                     "constraints": "1 ≤ size ≤ 10^5",
#                     "tests": [
#                         {"input": "1 2 3", "output": "True"},
#                         {"input": "3 2 1", "output": "False"},
#                         {"input": "1 1 2", "output": "True"}
#                     ]
#                 }

#             ],

#             "Medium": [

#                 {
#                     "id": "py-list-m-1",
#                     "title": "Find Missing Number",
#                     "task": "Given numbers from 1 to n with one missing, find missing number.",
#                     "input_format": "First line n. Second line n-1 numbers.",
#                     "output_format": "Print missing number.",
#                     "sample_input": "5\n1 2 3 5",
#                     "sample_output": "4",
#                     "constraints": "1 ≤ n ≤ 10^5",
#                     "tests": [
#                         {"input": "5\n1 2 3 5", "output": "4"},
#                         {"input": "3\n1 3", "output": "2"},
#                         {"input": "2\n1", "output": "2"}
#                     ]
#                 },

#                 {
#                     "id": "py-list-m-2",
#                     "title": "Two Sum",
#                     "task": "Given list and target, print True if two numbers sum to target.",
#                     "input_format": "First line list. Second line target.",
#                     "output_format": "Print True or False.",
#                     "sample_input": "1 2 3 4\n5",
#                     "sample_output": "True",
#                     "constraints": "1 ≤ size ≤ 10^5",
#                     "tests": [
#                         {"input": "1 2 3 4\n5", "output": "True"},
#                         {"input": "1 2 3\n7", "output": "False"},
#                         {"input": "2 7 11 15\n9", "output": "True"}
#                     ]
#                 },

#                 {
#                     "id": "py-list-m-3",
#                     "title": "Maximum Subarray Sum",
#                     "task": "Print maximum sum of any contiguous subarray.",
#                     "input_format": "Space-separated integers.",
#                     "output_format": "Print maximum sum.",
#                     "sample_input": "-2 1 -3 4 -1 2 1 -5 4",
#                     "sample_output": "6",
#                     "constraints": "1 ≤ size ≤ 10^5",
#                     "tests": [
#                         {"input": "-2 1 -3 4 -1 2 1 -5 4", "output": "6"},
#                         {"input": "1 2 3", "output": "6"},
#                         {"input": "-1 -2 -3", "output": "-1"}
#                     ]
#                 },

#                 {
#                     "id": "py-list-m-4",
#                     "title": "Find Majority Element",
#                     "task": "Print element appearing more than n/2 times.",
#                     "input_format": "Space-separated integers.",
#                     "output_format": "Print majority element.",
#                     "sample_input": "2 2 1 2 2",
#                     "sample_output": "2",
#                     "constraints": "Majority element always exists.",
#                     "tests": [
#                         {"input": "2 2 1 2 2", "output": "2"},
#                         {"input": "3 3 4", "output": "3"},
#                         {"input": "1 1 1 2 2", "output": "1"}
#                     ]
#                 },

#                 {
#                     "id": "py-list-m-5",
#                     "title": "Rotate by k Positions",
#                     "task": "Rotate list right by k positions.",
#                     "input_format": "First line list. Second line integer k.",
#                     "output_format": "Print rotated list.",
#                     "sample_input": "1 2 3 4 5\n2",
#                     "sample_output": "4 5 1 2 3",
#                     "constraints": "1 ≤ size ≤ 10^5",
#                     "tests": [
#                         {"input": "1 2 3 4 5\n2", "output": "4 5 1 2 3"},
#                         {"input": "1 2 3\n1", "output": "3 1 2"},
#                         {"input": "5\n3", "output": "5"}
#                     ]
#                 }

#             ]
#         },

#         "Loops": {

#             "Very Easy": [

#                 {
#                     "id": "py-loop-ve-1",
#                     "title": "Print 1 to N",
#                     "task": "Given integer n, print numbers from 1 to n separated by space.",
#                     "input_format": "First line contains integer n.",
#                     "output_format": "Print numbers from 1 to n.",
#                     "sample_input": "5",
#                     "sample_output": "1 2 3 4 5",
#                     "constraints": "1 ≤ n ≤ 10^5",
#                     "tests": [
#                         {"input": "5", "output": "1 2 3 4 5"},
#                         {"input": "1", "output": "1"},
#                         {"input": "3", "output": "1 2 3"}
#                     ]
#                 },

#                 {
#                     "id": "py-loop-ve-2",
#                     "title": "Print N to 1",
#                     "task": "Given integer n, print numbers from n to 1 separated by space.",
#                     "input_format": "First line contains integer n.",
#                     "output_format": "Print numbers from n to 1.",
#                     "sample_input": "5",
#                     "sample_output": "5 4 3 2 1",
#                     "constraints": "1 ≤ n ≤ 10^5",
#                     "tests": [
#                         {"input": "5", "output": "5 4 3 2 1"},
#                         {"input": "1", "output": "1"},
#                         {"input": "3", "output": "3 2 1"}
#                     ]
#                 },

#                 {
#                     "id": "py-loop-ve-3",
#                     "title": "Print Even Numbers",
#                     "task": "Given n, print all even numbers from 1 to n.",
#                     "input_format": "First line contains integer n.",
#                     "output_format": "Print even numbers.",
#                     "sample_input": "6",
#                     "sample_output": "2 4 6",
#                     "constraints": "1 ≤ n ≤ 10^5",
#                     "tests": [
#                         {"input": "6", "output": "2 4 6"},
#                         {"input": "5", "output": "2 4"},
#                         {"input": "2", "output": "2"}
#                     ]
#                 },

#                 {
#                     "id": "py-loop-ve-4",
#                     "title": "Print Odd Numbers",
#                     "task": "Given n, print all odd numbers from 1 to n.",
#                     "input_format": "First line contains integer n.",
#                     "output_format": "Print odd numbers.",
#                     "sample_input": "6",
#                     "sample_output": "1 3 5",
#                     "constraints": "1 ≤ n ≤ 10^5",
#                     "tests": [
#                         {"input": "6", "output": "1 3 5"},
#                         {"input": "5", "output": "1 3 5"},
#                         {"input": "1", "output": "1"}
#                     ]
#                 },

#                 {
#                     "id": "py-loop-ve-5",
#                     "title": "Sum 1 to N",
#                     "task": "Given n, print sum of numbers from 1 to n.",
#                     "input_format": "First line contains integer n.",
#                     "output_format": "Print sum.",
#                     "sample_input": "5",
#                     "sample_output": "15",
#                     "constraints": "1 ≤ n ≤ 10^6",
#                     "tests": [
#                         {"input": "5", "output": "15"},
#                         {"input": "1", "output": "1"},
#                         {"input": "3", "output": "6"}
#                     ]
#                 },

#                 {
#                     "id": "py-loop-ve-6",
#                     "title": "Factorial",
#                     "task": "Given n, print factorial of n.",
#                     "input_format": "First line contains integer n.",
#                     "output_format": "Print n!.",
#                     "sample_input": "4",
#                     "sample_output": "24",
#                     "constraints": "0 ≤ n ≤ 10",
#                     "tests": [
#                         {"input": "4", "output": "24"},
#                         {"input": "0", "output": "1"},
#                         {"input": "5", "output": "120"}
#                     ]
#                 },

#                 {
#                     "id": "py-loop-ve-7",
#                     "title": "Multiplication Table",
#                     "task": "Given n, print multiplication table from 1 to 5.",
#                     "input_format": "First line contains integer n.",
#                     "output_format": "Print table values separated by space.",
#                     "sample_input": "2",
#                     "sample_output": "2 4 6 8 10",
#                     "constraints": "1 ≤ n ≤ 10^4",
#                     "tests": [
#                         {"input": "2", "output": "2 4 6 8 10"},
#                         {"input": "3", "output": "3 6 9 12 15"},
#                         {"input": "1", "output": "1 2 3 4 5"}
#                     ]
#                 },

#                 {
#                     "id": "py-loop-ve-8",
#                     "title": "Count Digits",
#                     "task": "Given integer n, count number of digits.",
#                     "input_format": "First line contains integer n.",
#                     "output_format": "Print digit count.",
#                     "sample_input": "1234",
#                     "sample_output": "4",
#                     "constraints": "-10^9 ≤ n ≤ 10^9",
#                     "tests": [
#                         {"input": "1234", "output": "4"},
#                         {"input": "0", "output": "1"},
#                         {"input": "-567", "output": "3"}
#                     ]
#                 }

#             ],

#             "Easy": [

#                 {
#                     "id": "py-loop-e-1",
#                     "title": "Sum of Digits",
#                     "task": "Given integer n, print sum of its digits.",
#                     "input_format": "First line contains integer n.",
#                     "output_format": "Print sum of digits.",
#                     "sample_input": "123",
#                     "sample_output": "6",
#                     "constraints": "-10^9 ≤ n ≤ 10^9",
#                     "tests": [
#                         {"input": "123", "output": "6"},
#                         {"input": "100", "output": "1"},
#                         {"input": "9", "output": "9"}
#                     ]
#                 },

#                 {
#                     "id": "py-loop-e-2",
#                     "title": "Reverse Number",
#                     "task": "Given integer n, print reversed number.",
#                     "input_format": "First line contains integer n.",
#                     "output_format": "Print reversed number.",
#                     "sample_input": "123",
#                     "sample_output": "321",
#                     "constraints": "-10^9 ≤ n ≤ 10^9",
#                     "tests": [
#                         {"input": "123", "output": "321"},
#                         {"input": "100", "output": "1"},
#                         {"input": "9", "output": "9"}
#                     ]
#                 },

#                 {
#                     "id": "py-loop-e-3",
#                     "title": "Check Prime",
#                     "task": "Given integer n, print True if prime else False.",
#                     "input_format": "First line contains integer n.",
#                     "output_format": "Print True or False.",
#                     "sample_input": "7",
#                     "sample_output": "True",
#                     "constraints": "1 ≤ n ≤ 10^5",
#                     "tests": [
#                         {"input": "7", "output": "True"},
#                         {"input": "4", "output": "False"},
#                         {"input": "2", "output": "True"}
#                     ]
#                 },

#                 {
#                     "id": "py-loop-e-4",
#                     "title": "Fibonacci N Terms",
#                     "task": "Given n, print first n Fibonacci numbers.",
#                     "input_format": "First line contains integer n.",
#                     "output_format": "Print Fibonacci sequence.",
#                     "sample_input": "5",
#                     "sample_output": "0 1 1 2 3",
#                     "constraints": "1 ≤ n ≤ 20",
#                     "tests": [
#                         {"input": "5", "output": "0 1 1 2 3"},
#                         {"input": "1", "output": "0"},
#                         {"input": "2", "output": "0 1"}
#                     ]
#                 },

#                 {
#                     "id": "py-loop-e-5",
#                     "title": "Armstrong Number",
#                     "task": "Given integer n, print True if Armstrong else False.",
#                     "input_format": "First line contains integer n.",
#                     "output_format": "Print True or False.",
#                     "sample_input": "153",
#                     "sample_output": "True",
#                     "constraints": "1 ≤ n ≤ 10^6",
#                     "tests": [
#                         {"input": "153", "output": "True"},
#                         {"input": "123", "output": "False"},
#                         {"input": "370", "output": "True"}
#                     ]
#                 },

#                 {
#                     "id": "py-loop-e-6",
#                     "title": "Print Divisors",
#                     "task": "Given n, print all divisors of n in ascending order.",
#                     "input_format": "First line contains integer n.",
#                     "output_format": "Print divisors.",
#                     "sample_input": "6",
#                     "sample_output": "1 2 3 6",
#                     "constraints": "1 ≤ n ≤ 10^5",
#                     "tests": [
#                         {"input": "6", "output": "1 2 3 6"},
#                         {"input": "5", "output": "1 5"},
#                         {"input": "1", "output": "1"}
#                     ]
#                 }

#             ],

#             "Medium": [

#                 {
#                     "id": "py-loop-m-1",
#                     "title": "LCM of Two Numbers",
#                     "task": "Given two integers, print their LCM.",
#                     "input_format": "First line contains two space-separated integers.",
#                     "output_format": "Print LCM.",
#                     "sample_input": "4 6",
#                     "sample_output": "12",
#                     "constraints": "1 ≤ values ≤ 10^5",
#                     "tests": [
#                         {"input": "4 6", "output": "12"},
#                         {"input": "5 7", "output": "35"},
#                         {"input": "3 9", "output": "9"}
#                     ]
#                 },

#                 {
#                     "id": "py-loop-m-2",
#                     "title": "GCD of Two Numbers",
#                     "task": "Given two integers, print their GCD.",
#                     "input_format": "First line contains two space-separated integers.",
#                     "output_format": "Print GCD.",
#                     "sample_input": "4 6",
#                     "sample_output": "2",
#                     "constraints": "1 ≤ values ≤ 10^5",
#                     "tests": [
#                         {"input": "4 6", "output": "2"},
#                         {"input": "5 7", "output": "1"},
#                         {"input": "9 3", "output": "3"}
#                     ]
#                 },

#                 {
#                     "id": "py-loop-m-3",
#                     "title": "Perfect Number",
#                     "task": "Given n, print True if perfect number else False.",
#                     "input_format": "First line contains integer n.",
#                     "output_format": "Print True or False.",
#                     "sample_input": "6",
#                     "sample_output": "True",
#                     "constraints": "1 ≤ n ≤ 10^5",
#                     "tests": [
#                         {"input": "6", "output": "True"},
#                         {"input": "28", "output": "True"},
#                         {"input": "10", "output": "False"}
#                     ]
#                 },

#                 {
#                     "id": "py-loop-m-4",
#                     "title": "Pattern Pyramid",
#                     "task": "Given n, print pyramid pattern of stars.",
#                     "input_format": "First line contains integer n.",
#                     "output_format": "Print pyramid.",
#                     "sample_input": "3",
#                     "sample_output": "  *\n ***\n*****",
#                     "constraints": "1 ≤ n ≤ 20",
#                     "tests": [
#                         {"input": "3", "output": "  *\n ***\n*****"},
#                         {"input": "1", "output": "*"},
#                         {"input": "2", "output": " *\n***"}
#                     ]
#                 }

#             ]
#         },

#         "Functions in python": {

#             "Very Easy": [

#                 {
#                     "id": "py-func-ve-1",
#                     "title": "Return Sum",
#                     "task": "Define a function that takes two integers and returns their sum. Print the result.",
#                     "input_format": "First line contains two space-separated integers.",
#                     "output_format": "Print sum.",
#                     "sample_input": "2 3",
#                     "sample_output": "5",
#                     "constraints": "-10^9 ≤ values ≤ 10^9",
#                     "tests": [
#                         {"input": "2 3", "output": "5"},
#                         {"input": "-1 5", "output": "4"},
#                         {"input": "0 0", "output": "0"}
#                     ]
#                 },

#                 {
#                     "id": "py-func-ve-2",
#                     "title": "Return Square",
#                     "task": "Define a function that takes integer n and returns n squared.",
#                     "input_format": "First line contains integer n.",
#                     "output_format": "Print square of n.",
#                     "sample_input": "4",
#                     "sample_output": "16",
#                     "constraints": "-10^6 ≤ n ≤ 10^6",
#                     "tests": [
#                         {"input": "4", "output": "16"},
#                         {"input": "-3", "output": "9"},
#                         {"input": "0", "output": "0"}
#                     ]
#                 },

#                 {
#                     "id": "py-func-ve-3",
#                     "title": "Check Even Function",
#                     "task": "Define a function that returns True if number is even else False.",
#                     "input_format": "First line contains integer n.",
#                     "output_format": "Print True or False.",
#                     "sample_input": "4",
#                     "sample_output": "True",
#                     "constraints": "-10^9 ≤ n ≤ 10^9",
#                     "tests": [
#                         {"input": "4", "output": "True"},
#                         {"input": "3", "output": "False"},
#                         {"input": "0", "output": "True"}
#                     ]
#                 },

#                 {
#                     "id": "py-func-ve-4",
#                     "title": "Maximum of Two",
#                     "task": "Define a function that returns maximum of two numbers.",
#                     "input_format": "First line contains two integers.",
#                     "output_format": "Print maximum.",
#                     "sample_input": "5 9",
#                     "sample_output": "9",
#                     "constraints": "-10^9 ≤ values ≤ 10^9",
#                     "tests": [
#                         {"input": "5 9", "output": "9"},
#                         {"input": "-1 -5", "output": "-1"},
#                         {"input": "7 7", "output": "7"}
#                     ]
#                 },

#                 {
#                     "id": "py-func-ve-5",
#                     "title": "Length Function",
#                     "task": "Define a function that takes a string and returns its length.",
#                     "input_format": "First line contains string s.",
#                     "output_format": "Print length.",
#                     "sample_input": "Python",
#                     "sample_output": "6",
#                     "constraints": "1 ≤ length ≤ 10^5",
#                     "tests": [
#                         {"input": "Python", "output": "6"},
#                         {"input": "A", "output": "1"},
#                         {"input": "Slashcoder", "output": "10"}
#                     ]
#                 },

#                 {
#                     "id": "py-func-ve-6",
#                     "title": "Multiply Function",
#                     "task": "Define a function that returns product of two numbers.",
#                     "input_format": "First line contains two integers.",
#                     "output_format": "Print product.",
#                     "sample_input": "4 5",
#                     "sample_output": "20",
#                     "constraints": "-10^6 ≤ values ≤ 10^6",
#                     "tests": [
#                         {"input": "4 5", "output": "20"},
#                         {"input": "-2 6", "output": "-12"},
#                         {"input": "0 10", "output": "0"}
#                     ]
#                 },

#                 {
#                     "id": "py-func-ve-7",
#                     "title": "Return Absolute Value",
#                     "task": "Define a function that returns absolute value of integer n.",
#                     "input_format": "First line contains integer n.",
#                     "output_format": "Print absolute value.",
#                     "sample_input": "-5",
#                     "sample_output": "5",
#                     "constraints": "-10^9 ≤ n ≤ 10^9",
#                     "tests": [
#                         {"input": "-5", "output": "5"},
#                         {"input": "10", "output": "10"},
#                         {"input": "0", "output": "0"}
#                     ]
#                 }

#             ],

#             "Easy": [

#                 {
#                     "id": "py-func-e-1",
#                     "title": "Factorial Function",
#                     "task": "Define a function that returns factorial of n.",
#                     "input_format": "First line contains integer n.",
#                     "output_format": "Print factorial.",
#                     "sample_input": "4",
#                     "sample_output": "24",
#                     "constraints": "0 ≤ n ≤ 10",
#                     "tests": [
#                         {"input": "4", "output": "24"},
#                         {"input": "0", "output": "1"},
#                         {"input": "5", "output": "120"}
#                     ]
#                 },

#                 {
#                     "id": "py-func-e-2",
#                     "title": "Prime Check Function",
#                     "task": "Define function that returns True if n is prime else False.",
#                     "input_format": "First line contains integer n.",
#                     "output_format": "Print True or False.",
#                     "sample_input": "7",
#                     "sample_output": "True",
#                     "constraints": "1 ≤ n ≤ 10^5",
#                     "tests": [
#                         {"input": "7", "output": "True"},
#                         {"input": "4", "output": "False"},
#                         {"input": "2", "output": "True"}
#                     ]
#                 },

#                 {
#                     "id": "py-func-e-3",
#                     "title": "Reverse String Function",
#                     "task": "Define function that returns reversed string.",
#                     "input_format": "First line contains string s.",
#                     "output_format": "Print reversed string.",
#                     "sample_input": "Code",
#                     "sample_output": "edoC",
#                     "constraints": "1 ≤ length ≤ 10^5",
#                     "tests": [
#                         {"input": "Code", "output": "edoC"},
#                         {"input": "A", "output": "A"},
#                         {"input": "123", "output": "321"}
#                     ]
#                 },

#                 {
#                     "id": "py-func-e-4",
#                     "title": "Sum of List Function",
#                     "task": "Define function that returns sum of list elements.",
#                     "input_format": "Space-separated integers.",
#                     "output_format": "Print sum.",
#                     "sample_input": "1 2 3",
#                     "sample_output": "6",
#                     "constraints": "1 ≤ size ≤ 10^5",
#                     "tests": [
#                         {"input": "1 2 3", "output": "6"},
#                         {"input": "5", "output": "5"},
#                         {"input": "-1 1", "output": "0"}
#                     ]
#                 }

#             ],

#             "Medium": [

#                 {
#                     "id": "py-func-m-1",
#                     "title": "Fibonacci Function",
#                     "task": "Define function that returns nth Fibonacci number.",
#                     "input_format": "First line contains integer n.",
#                     "output_format": "Print nth Fibonacci.",
#                     "sample_input": "6",
#                     "sample_output": "8",
#                     "constraints": "0 ≤ n ≤ 20",
#                     "tests": [
#                         {"input": "6", "output": "8"},
#                         {"input": "0", "output": "0"},
#                         {"input": "1", "output": "1"}
#                     ]
#                 },

#                 {
#                     "id": "py-func-m-2",
#                     "title": "GCD Function",
#                     "task": "Define function that returns GCD of two numbers.",
#                     "input_format": "First line contains two integers.",
#                     "output_format": "Print GCD.",
#                     "sample_input": "4 6",
#                     "sample_output": "2",
#                     "constraints": "1 ≤ values ≤ 10^5",
#                     "tests": [
#                         {"input": "4 6", "output": "2"},
#                         {"input": "5 7", "output": "1"},
#                         {"input": "9 3", "output": "3"}
#                     ]
#                 },

#                 {
#                     "id": "py-func-m-3",
#                     "title": "Palindrome Function",
#                     "task": "Define function that checks if string is palindrome.",
#                     "input_format": "First line contains string s.",
#                     "output_format": "Print True or False.",
#                     "sample_input": "madam",
#                     "sample_output": "True",
#                     "constraints": "1 ≤ length ≤ 10^5",
#                     "tests": [
#                         {"input": "madam", "output": "True"},
#                         {"input": "python", "output": "False"},
#                         {"input": "racecar", "output": "True"}
#                     ]
#                 },

#                 {
#                     "id": "py-func-m-4",
#                     "title": "Power Recursive",
#                     "task": "Define recursive function that returns a^b.",
#                     "input_format": "First line contains two integers.",
#                     "output_format": "Print power result.",
#                     "sample_input": "2 5",
#                     "sample_output": "32",
#                     "constraints": "-100 ≤ a ≤ 100\n0 ≤ b ≤ 10",
#                     "tests": [
#                         {"input": "2 5", "output": "32"},
#                         {"input": "5 0", "output": "1"},
#                         {"input": "-2 2", "output": "4"}
#                     ]
#                 }

#             ]
#         },

#         "Tuples & Dictionary": {

#             "Very Easy": [

#                 {
#                     "id": "py-td-ve-1",
#                     "title": "Create Tuple",
#                     "task": "Given space-separated integers, create a tuple and print it.",
#                     "input_format": "First line contains space-separated integers.",
#                     "output_format": "Print tuple.",
#                     "sample_input": "1 2 3",
#                     "sample_output": "(1, 2, 3)",
#                     "constraints": "1 ≤ size ≤ 10^5",
#                     "tests": [
#                         {"input": "1 2 3", "output": "(1, 2, 3)"},
#                         {"input": "5", "output": "(5,)"},
#                         {"input": "10 20", "output": "(10, 20)"}
#                     ]
#                 },

#                 {
#                     "id": "py-td-ve-2",
#                     "title": "Tuple Length",
#                     "task": "Given integers, create tuple and print its length.",
#                     "input_format": "Space-separated integers.",
#                     "output_format": "Print length.",
#                     "sample_input": "1 2 3",
#                     "sample_output": "3",
#                     "constraints": "1 ≤ size ≤ 10^5",
#                     "tests": [
#                         {"input": "1 2 3", "output": "3"},
#                         {"input": "5", "output": "1"},
#                         {"input": "1 2", "output": "2"}
#                     ]
#                 },

#                 {
#                     "id": "py-td-ve-3",
#                     "title": "Access Tuple Element",
#                     "task": "Given tuple and index i, print element at index i.",
#                     "input_format": "First line tuple elements. Second line index i.",
#                     "output_format": "Print element.",
#                     "sample_input": "10 20 30\n1",
#                     "sample_output": "20",
#                     "constraints": "0 ≤ i < size",
#                     "tests": [
#                         {"input": "10 20 30\n1", "output": "20"},
#                         {"input": "5\n0", "output": "5"},
#                         {"input": "1 2 3\n2", "output": "3"}
#                     ]
#                 },

#                 {
#                     "id": "py-td-ve-4",
#                     "title": "Create Dictionary",
#                     "task": "Given key and value, create dictionary and print it.",
#                     "input_format": "First line key. Second line value.",
#                     "output_format": "Print dictionary.",
#                     "sample_input": "name\nprince",
#                     "sample_output": "{'name': 'prince'}",
#                     "constraints": "Keys and values are strings.",
#                     "tests": [
#                         {"input": "name\nprince", "output": "{'name': 'prince'}"},
#                         {"input": "age\n21", "output": "{'age': '21'}"},
#                         {"input": "city\nDelhi", "output": "{'city': 'Delhi'}"}
#                     ]
#                 },

#                 {
#                     "id": "py-td-ve-5",
#                     "title": "Dictionary Length",
#                     "task": "Given n key-value pairs, print dictionary length.",
#                     "input_format": "First line integer n. Next n lines contain key value.",
#                     "output_format": "Print dictionary size.",
#                     "sample_input": "2\na 1\nb 2",
#                     "sample_output": "2",
#                     "constraints": "1 ≤ n ≤ 10^5",
#                     "tests": [
#                         {"input": "2\na 1\nb 2", "output": "2"},
#                         {"input": "1\nx 10", "output": "1"},
#                         {"input": "3\na 1\nb 2\nc 3", "output": "3"}
#                     ]
#                 },

#                 {
#                     "id": "py-td-ve-6",
#                     "title": "Check Key Exists",
#                     "task": "Given dictionary and key k, print True if k exists else False.",
#                     "input_format": "First line n. Next n lines key value. Last line key k.",
#                     "output_format": "Print True or False.",
#                     "sample_input": "2\na 1\nb 2\na",
#                     "sample_output": "True",
#                     "constraints": "1 ≤ n ≤ 10^5",
#                     "tests": [
#                         {"input": "2\na 1\nb 2\na", "output": "True"},
#                         {"input": "1\nx 10\ny", "output": "False"},
#                         {"input": "1\nk v\nk", "output": "True"}
#                     ]
#                 },

#                 {
#                     "id": "py-td-ve-7",
#                     "title": "Print Dictionary Keys",
#                     "task": "Given dictionary, print all keys separated by space.",
#                     "input_format": "First line n. Next n lines key value.",
#                     "output_format": "Print keys.",
#                     "sample_input": "2\na 1\nb 2",
#                     "sample_output": "a b",
#                     "constraints": "1 ≤ n ≤ 10^5",
#                     "tests": [
#                         {"input": "2\na 1\nb 2", "output": "a b"},
#                         {"input": "1\nx 10", "output": "x"},
#                         {"input": "3\na 1\nb 2\nc 3", "output": "a b c"}
#                     ]
#                 },

#                 {
#                     "id": "py-td-ve-8",
#                     "title": "Print Dictionary Values",
#                     "task": "Given dictionary, print all values separated by space.",
#                     "input_format": "First line n. Next n lines key value.",
#                     "output_format": "Print values.",
#                     "sample_input": "2\na 1\nb 2",
#                     "sample_output": "1 2",
#                     "constraints": "1 ≤ n ≤ 10^5",
#                     "tests": [
#                         {"input": "2\na 1\nb 2", "output": "1 2"},
#                         {"input": "1\nx 10", "output": "10"},
#                         {"input": "3\na 1\nb 2\nc 3", "output": "1 2 3"}
#                     ]
#                 }

#             ],

#             "Easy": [

#                 {
#                     "id": "py-td-e-1",
#                     "title": "Sum Dictionary Values",
#                     "task": "Given dictionary of integers, print sum of all values.",
#                     "input_format": "First line n. Next n lines key value.",
#                     "output_format": "Print sum.",
#                     "sample_input": "2\na 1\nb 2",
#                     "sample_output": "3",
#                     "constraints": "1 ≤ n ≤ 10^5",
#                     "tests": [
#                         {"input": "2\na 1\nb 2", "output": "3"},
#                         {"input": "1\nx 10", "output": "10"},
#                         {"input": "3\na 1\nb 2\nc 3", "output": "6"}
#                     ]
#                 },

#                 {
#                     "id": "py-td-e-2",
#                     "title": "Tuple Unpacking",
#                     "task": "Given two integers, create tuple and unpack into variables then print sum.",
#                     "input_format": "Two space-separated integers.",
#                     "output_format": "Print sum.",
#                     "sample_input": "5 10",
#                     "sample_output": "15",
#                     "constraints": "-10^9 ≤ values ≤ 10^9",
#                     "tests": [
#                         {"input": "5 10", "output": "15"},
#                         {"input": "-1 1", "output": "0"},
#                         {"input": "3 4", "output": "7"}
#                     ]
#                 },

#                 {
#                     "id": "py-td-e-3",
#                     "title": "Merge Two Dictionaries",
#                     "task": "Given two dictionaries, merge and print merged dictionary.",
#                     "input_format": "First n1 and pairs. Then n2 and pairs.",
#                     "output_format": "Print merged dictionary.",
#                     "sample_input": "1\na 1\n1\nb 2",
#                     "sample_output": "{'a': '1', 'b': '2'}",
#                     "constraints": "1 ≤ n ≤ 10^5",
#                     "tests": [
#                         {"input": "1\na 1\n1\nb 2", "output": "{'a': '1', 'b': '2'}"},
#                         {"input": "1\nx 10\n1\nx 20", "output": "{'x': '20'}"},
#                         {"input": "0\n0", "output": "{}"}
#                     ]
#                 },

#                 {
#                     "id": "py-td-e-4",
#                     "title": "Find Key with Maximum Value",
#                     "task": "Given dictionary, print key with maximum value.",
#                     "input_format": "First line n. Next n lines key value (integer).",
#                     "output_format": "Print key.",
#                     "sample_input": "2\na 10\nb 20",
#                     "sample_output": "b",
#                     "constraints": "1 ≤ n ≤ 10^5",
#                     "tests": [
#                         {"input": "2\na 10\nb 20", "output": "b"},
#                         {"input": "1\nx 5", "output": "x"},
#                         {"input": "3\na 1\nb 5\nc 3", "output": "b"}
#                     ]
#                 },

#                 {
#                     "id": "py-td-e-5",
#                     "title": "Count Frequency",
#                     "task": "Given list of integers, print frequency of each element.",
#                     "input_format": "Space-separated integers.",
#                     "output_format": "Print element frequency pairs.",
#                     "sample_input": "1 2 2 3",
#                     "sample_output": "{1: 1, 2: 2, 3: 1}",
#                     "constraints": "1 ≤ size ≤ 10^5",
#                     "tests": [
#                         {"input": "1 2 2 3", "output": "{1: 1, 2: 2, 3: 1}"},
#                         {"input": "5 5 5", "output": "{5: 3}"},
#                         {"input": "1 2 3", "output": "{1: 1, 2: 1, 3: 1}"}
#                     ]
#                 }

#             ],

#             "Medium": [

#                 {
#                     "id": "py-td-m-1",
#                     "title": "Group Anagrams",
#                     "task": "Given list of strings, group anagrams together and print grouped lists.",
#                     "input_format": "Space-separated strings.",
#                     "output_format": "Print grouped anagrams.",
#                     "sample_input": "eat tea tan ate nat bat",
#                     "sample_output": "[['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]",
#                     "constraints": "1 ≤ size ≤ 10^4",
#                     "tests": [
#                         {"input": "eat tea tan ate nat bat", "output": "[['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]"},
#                         {"input": "abc bca cab", "output": "[['abc', 'bca', 'cab']]"},
#                         {"input": "a b c", "output": "[['a'], ['b'], ['c']]"}
#                     ]
#                 },

#                 {
#                     "id": "py-td-m-2",
#                     "title": "Dictionary Inversion",
#                     "task": "Given dictionary, invert keys and values.",
#                     "input_format": "First line n. Next n lines key value.",
#                     "output_format": "Print inverted dictionary.",
#                     "sample_input": "2\na 1\nb 2",
#                     "sample_output": "{'1': 'a', '2': 'b'}",
#                     "constraints": "Values are unique.",
#                     "tests": [
#                         {"input": "2\na 1\nb 2", "output": "{'1': 'a', '2': 'b'}"},
#                         {"input": "1\nx 10", "output": "{'10': 'x'}"},
#                         {"input": "0", "output": "{}"}
#                     ]
#                 },

#                 {
#                     "id": "py-td-m-3",
#                     "title": "Tuple Sorting",
#                     "task": "Given list of tuples (a, b), sort by second element.",
#                     "input_format": "First line n. Next n lines two integers.",
#                     "output_format": "Print sorted tuples.",
#                     "sample_input": "3\n1 3\n2 1\n3 2",
#                     "sample_output": "[(2, 1), (3, 2), (1, 3)]",
#                     "constraints": "1 ≤ n ≤ 10^5",
#                     "tests": [
#                         {"input": "3\n1 3\n2 1\n3 2", "output": "[(2, 1), (3, 2), (1, 3)]"},
#                         {"input": "1\n5 4", "output": "[(5, 4)]"},
#                         {"input": "2\n1 2\n3 1", "output": "[(3, 1), (1, 2)]"}
#                     ]
#                 },

#                 {
#                     "id": "py-td-m-4",
#                     "title": "Top K Frequent Elements",
#                     "task": "Given list of integers and integer k, print k most frequent elements.",
#                     "input_format": "First line list. Second line k.",
#                     "output_format": "Print k elements.",
#                     "sample_input": "1 1 1 2 2 3\n2",
#                     "sample_output": "[1, 2]",
#                     "constraints": "1 ≤ size ≤ 10^5",
#                     "tests": [
#                         {"input": "1 1 1 2 2 3\n2", "output": "[1, 2]"},
#                         {"input": "4 4 4 5 5 6\n1", "output": "[4]"},
#                         {"input": "1 2 3\n3", "output": "[1, 2, 3]"}
#                     ]
#                 },

#                 {
#                     "id": "py-td-m-5",
#                     "title": "Dictionary Word Count",
#                     "task": "Given sentence, count occurrences of each word.",
#                     "input_format": "First line sentence.",
#                     "output_format": "Print word count dictionary.",
#                     "sample_input": "hello world hello",
#                     "sample_output": "{'hello': 2, 'world': 1}",
#                     "constraints": "1 ≤ length ≤ 10^5",
#                     "tests": [
#                         {"input": "hello world hello", "output": "{'hello': 2, 'world': 1}"},
#                         {"input": "a a a", "output": "{'a': 3}"},
#                         {"input": "one two three", "output": "{'one': 1, 'two': 1, 'three': 1}"}
#                     ]
#                 }

#             ]
#         },

#         "Getting started with algorithmic problems": {

#             "Very Easy": [

#                 {
#                     "id": "py-algo-ve-1",
#                     "title": "Find Maximum",
#                     "task": "Given space-separated integers, print the maximum value.",
#                     "input_format": "Space-separated integers.",
#                     "output_format": "Print maximum.",
#                     "sample_input": "1 5 3",
#                     "sample_output": "5",
#                     "constraints": "1 ≤ size ≤ 10^5",
#                     "tests": [
#                         {"input": "1 5 3", "output": "5"},
#                         {"input": "-1 -2 -3", "output": "-1"},
#                         {"input": "10", "output": "10"}
#                     ]
#                 },

#                 {
#                     "id": "py-algo-ve-2",
#                     "title": "Find Minimum",
#                     "task": "Given integers, print minimum value.",
#                     "input_format": "Space-separated integers.",
#                     "output_format": "Print minimum.",
#                     "sample_input": "1 5 3",
#                     "sample_output": "1",
#                     "constraints": "1 ≤ size ≤ 10^5",
#                     "tests": [
#                         {"input": "1 5 3", "output": "1"},
#                         {"input": "-1 -2 -3", "output": "-3"},
#                         {"input": "10", "output": "10"}
#                     ]
#                 },

#                 {
#                     "id": "py-algo-ve-3",
#                     "title": "Count Elements",
#                     "task": "Print number of elements.",
#                     "input_format": "Space-separated integers.",
#                     "output_format": "Print count.",
#                     "sample_input": "1 2 3",
#                     "sample_output": "3",
#                     "tests": [
#                         {"input": "1 2 3", "output": "3"},
#                         {"input": "5", "output": "1"},
#                         {"input": "7 8", "output": "2"}
#                     ]
#                 },

#                 {
#                     "id": "py-algo-ve-4",
#                     "title": "Linear Search",
#                     "task": "Given list and x, print True if x exists else False.",
#                     "input_format": "First line list. Second line x.",
#                     "output_format": "Print True or False.",
#                     "sample_input": "1 2 3\n2",
#                     "sample_output": "True",
#                     "tests": [
#                         {"input": "1 2 3\n2", "output": "True"},
#                         {"input": "1 2 3\n5", "output": "False"},
#                         {"input": "5\n5", "output": "True"}
#                     ]
#                 },

#                 {
#                     "id": "py-algo-ve-5",
#                     "title": "Sum of Elements",
#                     "task": "Print sum of list elements.",
#                     "input_format": "Space-separated integers.",
#                     "output_format": "Print sum.",
#                     "sample_input": "1 2 3",
#                     "sample_output": "6",
#                     "tests": [
#                         {"input": "1 2 3", "output": "6"},
#                         {"input": "5", "output": "5"},
#                         {"input": "-1 1", "output": "0"}
#                     ]
#                 },

#                 {
#                     "id": "py-algo-ve-6",
#                     "title": "Average",
#                     "task": "Print average of list elements.",
#                     "input_format": "Space-separated integers.",
#                     "output_format": "Print average as float.",
#                     "sample_input": "2 4 6",
#                     "sample_output": "4.0",
#                     "tests": [
#                         {"input": "2 4 6", "output": "4.0"},
#                         {"input": "5", "output": "5.0"},
#                         {"input": "1 2", "output": "1.5"}
#                     ]
#                 },

#                 {
#                     "id": "py-algo-ve-7",
#                     "title": "Reverse List",
#                     "task": "Print list in reverse order.",
#                     "input_format": "Space-separated integers.",
#                     "output_format": "Print reversed list.",
#                     "sample_input": "1 2 3",
#                     "sample_output": "3 2 1",
#                     "tests": [
#                         {"input": "1 2 3", "output": "3 2 1"},
#                         {"input": "5", "output": "5"},
#                         {"input": "9 8", "output": "8 9"}
#                     ]
#                 },

#                 {
#                     "id": "py-algo-ve-8",
#                     "title": "Sort List",
#                     "task": "Print sorted list in ascending order.",
#                     "input_format": "Space-separated integers.",
#                     "output_format": "Print sorted list.",
#                     "sample_input": "3 1 2",
#                     "sample_output": "1 2 3",
#                     "tests": [
#                         {"input": "3 1 2", "output": "1 2 3"},
#                         {"input": "5 4 3", "output": "3 4 5"},
#                         {"input": "1", "output": "1"}
#                     ]
#                 },

#                 {
#                     "id": "py-algo-ve-9",
#                     "title": "Find Second Element",
#                     "task": "Print second element of list.",
#                     "input_format": "Space-separated integers.",
#                     "output_format": "Print second element.",
#                     "sample_input": "1 2 3",
#                     "sample_output": "2",
#                     "tests": [
#                         {"input": "1 2 3", "output": "2"},
#                         {"input": "5 6", "output": "6"},
#                         {"input": "9 8 7", "output": "8"}
#                     ]
#                 },

#                 {
#                     "id": "py-algo-ve-10",
#                     "title": "Find Largest of Three",
#                     "task": "Given three integers, print largest.",
#                     "input_format": "Three space-separated integers.",
#                     "output_format": "Print largest.",
#                     "sample_input": "3 9 5",
#                     "sample_output": "9",
#                     "tests": [
#                         {"input": "3 9 5", "output": "9"},
#                         {"input": "1 2 3", "output": "3"},
#                         {"input": "-1 -2 -3", "output": "-1"}
#                     ]
#                 },

#                 {
#                     "id": "py-algo-ve-11",
#                     "title": "Check Even Count",
#                     "task": "Print count of even numbers in list.",
#                     "input_format": "Space-separated integers.",
#                     "output_format": "Print count.",
#                     "sample_input": "1 2 3 4",
#                     "sample_output": "2",
#                     "tests": [
#                         {"input": "1 2 3 4", "output": "2"},
#                         {"input": "2 4 6", "output": "3"},
#                         {"input": "1 3 5", "output": "0"}
#                     ]
#                 },

#                 {
#                     "id": "py-algo-ve-12",
#                     "title": "Check Odd Count",
#                     "task": "Print count of odd numbers.",
#                     "input_format": "Space-separated integers.",
#                     "output_format": "Print count.",
#                     "sample_input": "1 2 3 4",
#                     "sample_output": "2",
#                     "tests": [
#                         {"input": "1 2 3 4", "output": "2"},
#                         {"input": "2 4 6", "output": "0"},
#                         {"input": "1 3 5", "output": "3"}
#                     ]
#                 },

#                 {
#                     "id": "py-algo-ve-13",
#                     "title": "Find Index of Max",
#                     "task": "Print index (0-based) of maximum element.",
#                     "input_format": "Space-separated integers.",
#                     "output_format": "Print index.",
#                     "sample_input": "1 5 3",
#                     "sample_output": "1",
#                     "tests": [
#                         {"input": "1 5 3", "output": "1"},
#                         {"input": "10 20", "output": "1"},
#                         {"input": "7", "output": "0"}
#                     ]
#                 },

#                 {
#                     "id": "py-algo-ve-14",
#                     "title": "Check Sorted",
#                     "task": "Print True if list is sorted ascending else False.",
#                     "input_format": "Space-separated integers.",
#                     "output_format": "Print True or False.",
#                     "sample_input": "1 2 3",
#                     "sample_output": "True",
#                     "tests": [
#                         {"input": "1 2 3", "output": "True"},
#                         {"input": "3 2 1", "output": "False"},
#                         {"input": "1 1 2", "output": "True"}
#                     ]
#                 },

#                 {
#                     "id": "py-algo-ve-15",
#                     "title": "Count Positive Numbers",
#                     "task": "Print count of positive numbers in list.",
#                     "input_format": "Space-separated integers.",
#                     "output_format": "Print count.",
#                     "sample_input": "-1 2 3 -4",
#                     "sample_output": "2",
#                     "tests": [
#                         {"input": "-1 2 3 -4", "output": "2"},
#                         {"input": "1 2 3", "output": "3"},
#                         {"input": "-1 -2", "output": "0"}
#                     ]
#                 }

#             ],

#             "Easy": [

#                 {
#                     "id": "py-algo-e-1",
#                     "title": "Binary Search",
#                     "task": "Given sorted list and x, print index of x or -1 if not found.",
#                     "input_format": "First line sorted list. Second line x.",
#                     "output_format": "Print index or -1.",
#                     "sample_input": "1 2 3 4 5\n3",
#                     "sample_output": "2",
#                     "tests": [
#                         {"input": "1 2 3 4 5\n3", "output": "2"},
#                         {"input": "1 2 3\n5", "output": "-1"},
#                         {"input": "10\n10", "output": "0"}
#                     ]
#                 },

#                 {
#                     "id": "py-algo-e-2",
#                     "title": "Remove Duplicates",
#                     "task": "Remove duplicates and print unique elements sorted.",
#                     "input_format": "Space-separated integers.",
#                     "output_format": "Print unique sorted list.",
#                     "sample_input": "1 2 2 3",
#                     "sample_output": "1 2 3",
#                     "tests": [
#                         {"input": "1 2 2 3", "output": "1 2 3"},
#                         {"input": "5 5 5", "output": "5"},
#                         {"input": "3 1 2", "output": "1 2 3"}
#                     ]
#                 },

#                 {
#                     "id": "py-algo-e-3",
#                     "title": "Two Sum",
#                     "task": "Print True if two numbers sum to target.",
#                     "input_format": "First line list. Second line target.",
#                     "output_format": "Print True or False.",
#                     "sample_input": "1 2 3 4\n5",
#                     "sample_output": "True",
#                     "tests": [
#                         {"input": "1 2 3 4\n5", "output": "True"},
#                         {"input": "1 2 3\n7", "output": "False"},
#                         {"input": "2 7 11 15\n9", "output": "True"}
#                     ]
#                 },

#                 {
#                     "id": "py-algo-e-4",
#                     "title": "Check Palindrome Number",
#                     "task": "Print True if number is palindrome else False.",
#                     "input_format": "First line integer n.",
#                     "output_format": "Print True or False.",
#                     "sample_input": "121",
#                     "sample_output": "True",
#                     "tests": [
#                         {"input": "121", "output": "True"},
#                         {"input": "123", "output": "False"},
#                         {"input": "7", "output": "True"}
#                     ]
#                 },

#                 {
#                     "id": "py-algo-e-5",
#                     "title": "Find Missing Number",
#                     "task": "Given numbers 1..n with one missing, find missing.",
#                     "input_format": "First line n. Second line numbers.",
#                     "output_format": "Print missing number.",
#                     "sample_input": "5\n1 2 3 5",
#                     "sample_output": "4",
#                     "tests": [
#                         {"input": "5\n1 2 3 5", "output": "4"},
#                         {"input": "3\n1 3", "output": "2"},
#                         {"input": "2\n1", "output": "2"}
#                     ]
#                 },

#                 {
#                     "id": "py-algo-e-6",
#                     "title": "Maximum Difference",
#                     "task": "Print maximum difference between two elements (j > i).",
#                     "input_format": "Space-separated integers.",
#                     "output_format": "Print maximum difference.",
#                     "sample_input": "7 1 5 3 6 4",
#                     "sample_output": "5",
#                     "tests": [
#                         {"input": "7 1 5 3 6 4", "output": "5"},
#                         {"input": "7 6 4 3 1", "output": "0"},
#                         {"input": "1 2", "output": "1"}
#                     ]
#                 },

#                 {
#                     "id": "py-algo-e-7",
#                     "title": "Rotate List Left",
#                     "task": "Rotate list left by k positions.",
#                     "input_format": "First line list. Second line k.",
#                     "output_format": "Print rotated list.",
#                     "sample_input": "1 2 3 4 5\n2",
#                     "sample_output": "3 4 5 1 2",
#                     "tests": [
#                         {"input": "1 2 3 4 5\n2", "output": "3 4 5 1 2"},
#                         {"input": "1 2 3\n1", "output": "2 3 1"},
#                         {"input": "5\n3", "output": "5"}
#                     ]
#                 },

#                 {
#                     "id": "py-algo-e-8",
#                     "title": "Count Frequency",
#                     "task": "Print frequency of each element.",
#                     "input_format": "Space-separated integers.",
#                     "output_format": "Print frequency dictionary.",
#                     "sample_input": "1 2 2 3",
#                     "sample_output": "{1: 1, 2: 2, 3: 1}",
#                     "tests": [
#                         {"input": "1 2 2 3", "output": "{1: 1, 2: 2, 3: 1}"},
#                         {"input": "5 5 5", "output": "{5: 3}"},
#                         {"input": "1 2 3", "output": "{1: 1, 2: 1, 3: 1}"}
#                     ]
#                 },

#                 {
#                     "id": "py-algo-e-9",
#                     "title": "Check Subarray Sum Zero",
#                     "task": "Print True if any subarray has sum zero else False.",
#                     "input_format": "Space-separated integers.",
#                     "output_format": "Print True or False.",
#                     "sample_input": "4 2 -3 1 6",
#                     "sample_output": "True",
#                     "tests": [
#                         {"input": "4 2 -3 1 6", "output": "True"},
#                         {"input": "1 2 3", "output": "False"},
#                         {"input": "1 -1", "output": "True"}
#                     ]
#                 },

#                 {
#                     "id": "py-algo-e-10",
#                     "title": "Find Intersection",
#                     "task": "Given two lists, print their intersection.",
#                     "input_format": "First list. Second list.",
#                     "output_format": "Print common elements.",
#                     "sample_input": "1 2 3\n2 3 4",
#                     "sample_output": "2 3",
#                     "tests": [
#                         {"input": "1 2 3\n2 3 4", "output": "2 3"},
#                         {"input": "1 2\n3 4", "output": ""},
#                         {"input": "5 6 7\n7 8 9", "output": "7"}
#                     ]
#                 }

#             ],

#             "Medium": [

#                 {
#                     "id": "py-algo-m-1",
#                     "title": "Kadane's Algorithm",
#                     "task": "Print maximum subarray sum.",
#                     "input_format": "Space-separated integers.",
#                     "output_format": "Print max sum.",
#                     "sample_input": "-2 1 -3 4 -1 2 1 -5 4",
#                     "sample_output": "6",
#                     "tests": [
#                         {"input": "-2 1 -3 4 -1 2 1 -5 4", "output": "6"},
#                         {"input": "1 2 3", "output": "6"},
#                         {"input": "-1 -2 -3", "output": "-1"}
#                     ]
#                 },

#                 {
#                     "id": "py-algo-m-2",
#                     "title": "Longest Consecutive Sequence",
#                     "task": "Print length of longest consecutive sequence.",
#                     "input_format": "Space-separated integers.",
#                     "output_format": "Print length.",
#                     "sample_input": "100 4 200 1 3 2",
#                     "sample_output": "4",
#                     "tests": [
#                         {"input": "100 4 200 1 3 2", "output": "4"},
#                         {"input": "1 2 0 1", "output": "3"},
#                         {"input": "1", "output": "1"}
#                     ]
#                 },

#                 {
#                     "id": "py-algo-m-3",
#                     "title": "Merge Intervals",
#                     "task": "Given intervals, merge overlapping intervals.",
#                     "input_format": "First line n. Next n lines start end.",
#                     "output_format": "Print merged intervals.",
#                     "sample_input": "3\n1 3\n2 6\n8 10",
#                     "sample_output": "[(1, 6), (8, 10)]",
#                     "tests": [
#                         {"input": "3\n1 3\n2 6\n8 10", "output": "[(1, 6), (8, 10)]"},
#                         {"input": "1\n1 4", "output": "[(1, 4)]"},
#                         {"input": "2\n1 2\n3 4", "output": "[(1, 2), (3, 4)]"}
#                     ]
#                 },

#                 {
#                     "id": "py-algo-m-4",
#                     "title": "Product Except Self",
#                     "task": "Given list, print product of array except self.",
#                     "input_format": "Space-separated integers.",
#                     "output_format": "Print resulting list.",
#                     "sample_input": "1 2 3 4",
#                     "sample_output": "[24, 12, 8, 6]",
#                     "tests": [
#                         {"input": "1 2 3 4", "output": "[24, 12, 8, 6]"},
#                         {"input": "2 3", "output": "[3, 2]"},
#                         {"input": "1 1 1", "output": "[1, 1, 1]"}
#                     ]
#                 },

#                 {
#                     "id": "py-algo-m-5",
#                     "title": "Detect Cycle in Array",
#                     "task": "Given array of next indices, detect if cycle exists (Floyd's cycle).",
#                     "input_format": "Space-separated integers representing next index.",
#                     "output_format": "Print True if cycle exists else False.",
#                     "sample_input": "1 2 3 1",
#                     "sample_output": "True",
#                     "tests": [
#                         {"input": "1 2 3 1", "output": "True"},
#                         {"input": "1 2 3 4", "output": "False"},
#                         {"input": "0", "output": "True"}
#                     ]
#                 }

#             ]
#         }
#     },

#     "c": {

#         "Structure & Syntax": {

#             "Very Easy": [

#                 {
#                     "id": "c-ss-ve-1",
#                     "title": "Print Hello C",
#                     "task": (
#                         "Write a complete C program that prints the message "
#                         "'Hello C Programming' exactly as shown. "
#                         "Ensure proper use of #include, main function, and return statement."
#                     ),
#                     "input_format": "No input.",
#                     "output_format": "Print Hello C Programming",
#                     "sample_input": "",
#                     "sample_output": "Hello C Programming",
#                     "constraints": "No constraints.",
#                     "tests": [
#                         {"input": "", "output": "Hello C Programming"},
#                         {"input": "", "output": "Hello C Programming"},
#                         {"input": "", "output": "Hello C Programming"}
#                     ]
#                 },

#                 {
#                     "id": "c-ss-ve-2",
#                     "title": "Print Two Lines",
#                     "task": (
#                         "Write a valid C program that prints the following:\n"
#                         "C Language\n"
#                         "is Powerful\n"
#                         "Use proper newline characters."
#                     ),
#                     "input_format": "No input.",
#                     "output_format": "Print two lines exactly.",
#                     "sample_input": "",
#                     "sample_output": "C Language\nis Powerful",
#                     "constraints": "Use printf correctly.",
#                     "tests": [
#                         {"input": "", "output": "C Language\nis Powerful"},
#                         {"input": "", "output": "C Language\nis Powerful"},
#                         {"input": "", "output": "C Language\nis Powerful"}
#                     ]
#                 },

#                 {
#                     "id": "c-ss-ve-3",
#                     "title": "Print Integer",
#                     "task": (
#                         "Write a C program that declares an integer variable, "
#                         "assigns it the value 100, and prints it."
#                     ),
#                     "input_format": "No input.",
#                     "output_format": "Print 100",
#                     "sample_input": "",
#                     "sample_output": "100",
#                     "constraints": "Use correct format specifier.",
#                     "tests": [
#                         {"input": "", "output": "100"},
#                         {"input": "", "output": "100"},
#                         {"input": "", "output": "100"}
#                     ]
#                 },

#                 {
#                     "id": "c-ss-ve-4",
#                     "title": "Print Character",
#                     "task": (
#                         "Write a C program that declares a character variable "
#                         "with value 'A' and prints it."
#                     ),
#                     "input_format": "No input.",
#                     "output_format": "Print A",
#                     "sample_input": "",
#                     "sample_output": "A",
#                     "constraints": "Use %c format specifier.",
#                     "tests": [
#                         {"input": "", "output": "A"},
#                         {"input": "", "output": "A"},
#                         {"input": "", "output": "A"}
#                     ]
#                 },

#                 {
#                     "id": "c-ss-ve-5",
#                     "title": "Print Float",
#                     "task": (
#                         "Write a C program that declares a float variable "
#                         "with value 3.14 and prints it."
#                     ),
#                     "input_format": "No input.",
#                     "output_format": "Print 3.14",
#                     "sample_input": "",
#                     "sample_output": "3.14",
#                     "constraints": "Use %f format specifier.",
#                     "tests": [
#                         {"input": "", "output": "3.14"},
#                         {"input": "", "output": "3.14"},
#                         {"input": "", "output": "3.14"}
#                     ]
#                 }

#             ],

#             "Easy": [

#                 {
#                     "id": "c-ss-e-1",
#                     "title": "Sum Two Numbers",
#                     "task": (
#                         "Write a complete C program that reads two integers "
#                         "from input and prints their sum. "
#                         "Use proper syntax including stdio.h and main()."
#                     ),
#                     "input_format": "First line contains two integers.",
#                     "output_format": "Print sum of numbers.",
#                     "sample_input": "5 3",
#                     "sample_output": "8",
#                     "constraints": "-10^9 ≤ values ≤ 10^9",
#                     "tests": [
#                         {"input": "5 3", "output": "8"},
#                         {"input": "-1 5", "output": "4"},
#                         {"input": "0 0", "output": "0"},
#                         {"input": "1000000000 1", "output": "1000000001"}
#                     ]
#                 },

#                 {
#                     "id": "c-ss-e-2",
#                     "title": "Print Escape Sequences",
#                     "task": (
#                         "Write a C program that prints:\n"
#                         "Name:\tJohn\n"
#                         "Age:\t21\n"
#                         "Use proper escape sequences."
#                     ),
#                     "input_format": "No input.",
#                     "output_format": "Formatted output.",
#                     "sample_input": "",
#                     "sample_output": "Name:\tJohn\nAge:\t21",
#                     "constraints": "Use \\t and \\n correctly.",
#                     "tests": [
#                         {"input": "", "output": "Name:\tJohn\nAge:\t21"},
#                         {"input": "", "output": "Name:\tJohn\nAge:\t21"},
#                         {"input": "", "output": "Name:\tJohn\nAge:\t21"}
#                     ]
#                 },

#                 {
#                     "id": "c-ss-e-3",
#                     "title": "Read and Print Float",
#                     "task": (
#                         "Write a C program that reads a floating-point number "
#                         "from input and prints it exactly as entered."
#                     ),
#                     "input_format": "First line contains float value.",
#                     "output_format": "Print float.",
#                     "sample_input": "2.5",
#                     "sample_output": "2.5",
#                     "constraints": "-10^6 ≤ value ≤ 10^6",
#                     "tests": [
#                         {"input": "2.5", "output": "2.5"},
#                         {"input": "-3.14", "output": "-3.14"},
#                         {"input": "0.0", "output": "0.0"}
#                     ]
#                 },

#                 {
#                     "id": "c-ss-e-4",
#                     "title": "Multiple Variable Print",
#                     "task": (
#                         "Write a C program that reads an integer and a character "
#                         "and prints them separated by space."
#                     ),
#                     "input_format": "First line contains integer and character.",
#                     "output_format": "Print integer and character.",
#                     "sample_input": "5 A",
#                     "sample_output": "5 A",
#                     "constraints": "Proper format specifiers required.",
#                     "tests": [
#                         {"input": "5 A", "output": "5 A"},
#                         {"input": "10 Z", "output": "10 Z"},
#                         {"input": "0 B", "output": "0 B"}
#                     ]
#                 }

#             ],

#             "Medium": [

#                 {
#                     "id": "c-ss-m-1",
#                     "title": "Formatted Output",
#                     "task": (
#                         "Write a C program that reads two integers and prints:\n"
#                         "Sum: <sum>\n"
#                         "Product: <product>\n"
#                         "Ensure correct formatting."
#                     ),
#                     "input_format": "Two integers.",
#                     "output_format": "Formatted output.",
#                     "sample_input": "2 3",
#                     "sample_output": "Sum: 5\nProduct: 6",
#                     "constraints": "-10^6 ≤ values ≤ 10^6",
#                     "tests": [
#                         {"input": "2 3", "output": "Sum: 5\nProduct: 6"},
#                         {"input": "5 5", "output": "Sum: 10\nProduct: 25"},
#                         {"input": "0 10", "output": "Sum: 10\nProduct: 0"}
#                     ]
#                 }

#             ]

#         },

#         "Data Types": {

#             "Very Easy": [

#                 {
#                     "id": "c-dt-ve-1",
#                     "title": "Integer Input and Output",
#                     "task": (
#                         "Write a C program that reads an integer from input "
#                         "and prints the same integer. Use correct format specifier."
#                     ),
#                     "input_format": "First line contains an integer n.",
#                     "output_format": "Print the integer n.",
#                     "sample_input": "5",
#                     "sample_output": "5",
#                     "constraints": "-10^9 ≤ n ≤ 10^9",
#                     "tests": [
#                         {"input": "5", "output": "5"},
#                         {"input": "-10", "output": "-10"},
#                         {"input": "0", "output": "0"}
#                     ]
#                 },

#                 {
#                     "id": "c-dt-ve-2",
#                     "title": "Float Input and Output",
#                     "task": (
#                         "Write a C program that reads a float value "
#                         "and prints it exactly as entered."
#                     ),
#                     "input_format": "First line contains a float f.",
#                     "output_format": "Print f.",
#                     "sample_input": "3.14",
#                     "sample_output": "3.14",
#                     "constraints": "-10^6 ≤ f ≤ 10^6",
#                     "tests": [
#                         {"input": "3.14", "output": "3.14"},
#                         {"input": "-2.5", "output": "-2.5"},
#                         {"input": "0.0", "output": "0.0"}
#                     ]
#                 },

#                 {
#                     "id": "c-dt-ve-3",
#                     "title": "Character Input and Output",
#                     "task": (
#                         "Write a C program that reads a single character "
#                         "and prints it."
#                     ),
#                     "input_format": "First line contains a character c.",
#                     "output_format": "Print character c.",
#                     "sample_input": "A",
#                     "sample_output": "A",
#                     "constraints": "Input is a printable ASCII character.",
#                     "tests": [
#                         {"input": "A", "output": "A"},
#                         {"input": "z", "output": "z"},
#                         {"input": "5", "output": "5"}
#                     ]
#                 },

#                 {
#                     "id": "c-dt-ve-4",
#                     "title": "Double Precision Value",
#                     "task": (
#                         "Write a C program that reads a double value "
#                         "and prints it with full precision."
#                     ),
#                     "input_format": "First line contains a double d.",
#                     "output_format": "Print d.",
#                     "sample_input": "2.71828",
#                     "sample_output": "2.71828",
#                     "constraints": "-10^9 ≤ d ≤ 10^9",
#                     "tests": [
#                         {"input": "2.71828", "output": "2.71828"},
#                         {"input": "-3.14159", "output": "-3.14159"},
#                         {"input": "0.0", "output": "0.0"}
#                     ]
#                 },

#                 {
#                     "id": "c-dt-ve-5",
#                     "title": "Long Integer",
#                     "task": (
#                         "Write a C program that reads a long integer "
#                         "and prints it using correct format specifier."
#                     ),
#                     "input_format": "First line contains a long integer.",
#                     "output_format": "Print the long integer.",
#                     "sample_input": "1234567890",
#                     "sample_output": "1234567890",
#                     "constraints": "Fits in long type.",
#                     "tests": [
#                         {"input": "1234567890", "output": "1234567890"},
#                         {"input": "-999999999", "output": "-999999999"},
#                         {"input": "0", "output": "0"}
#                     ]
#                 }

#             ],

#             "Easy": [

#                 {
#                     "id": "c-dt-e-1",
#                     "title": "Type Casting Float to Int",
#                     "task": (
#                         "Write a C program that reads a float value, "
#                         "casts it to integer, and prints the integer part only."
#                     ),
#                     "input_format": "First line contains float f.",
#                     "output_format": "Print integer part of f.",
#                     "sample_input": "3.9",
#                     "sample_output": "3",
#                     "constraints": "-10^6 ≤ f ≤ 10^6",
#                     "tests": [
#                         {"input": "3.9", "output": "3"},
#                         {"input": "-2.7", "output": "-2"},
#                         {"input": "5.0", "output": "5"}
#                     ]
#                 },

#                 {
#                     "id": "c-dt-e-2",
#                     "title": "Add Int and Float",
#                     "task": (
#                         "Write a C program that reads an integer and a float, "
#                         "adds them, and prints the result as float."
#                     ),
#                     "input_format": "First line contains int and float.",
#                     "output_format": "Print sum as float.",
#                     "sample_input": "5 2.5",
#                     "sample_output": "7.5",
#                     "constraints": "-10^6 ≤ values ≤ 10^6",
#                     "tests": [
#                         {"input": "5 2.5", "output": "7.5"},
#                         {"input": "0 1.1", "output": "1.1"},
#                         {"input": "-2 2.0", "output": "0.0"}
#                     ]
#                 },

#                 {
#                     "id": "c-dt-e-3",
#                     "title": "Size of Data Types",
#                     "task": (
#                         "Write a C program that prints the size (in bytes) of int, "
#                         "float, char, and double using sizeof operator."
#                     ),
#                     "input_format": "No input.",
#                     "output_format": "Print four sizes separated by space.",
#                     "sample_input": "",
#                     "sample_output": "4 4 1 8",
#                     "constraints": "Typical 64-bit system assumed.",
#                     "tests": [
#                         {"input": "", "output": "4 4 1 8"},
#                         {"input": "", "output": "4 4 1 8"},
#                         {"input": "", "output": "4 4 1 8"}
#                     ]
#                 },

#                 {
#                     "id": "c-dt-e-4",
#                     "title": "Unsigned Integer",
#                     "task": (
#                         "Write a C program that reads an unsigned integer "
#                         "and prints it."
#                     ),
#                     "input_format": "First line contains unsigned integer.",
#                     "output_format": "Print unsigned integer.",
#                     "sample_input": "10",
#                     "sample_output": "10",
#                     "constraints": "0 ≤ value ≤ 2^32 - 1",
#                     "tests": [
#                         {"input": "10", "output": "10"},
#                         {"input": "0", "output": "0"},
#                         {"input": "4294967295", "output": "4294967295"}
#                     ]
#                 }

#             ],

#             "Medium": [

#                 {
#                     "id": "c-dt-m-1",
#                     "title": "Precision Formatting",
#                     "task": (
#                         "Write a C program that reads a double and prints it "
#                         "rounded to 2 decimal places."
#                     ),
#                     "input_format": "First line contains double d.",
#                     "output_format": "Print value rounded to 2 decimal places.",
#                     "sample_input": "3.14159",
#                     "sample_output": "3.14",
#                     "constraints": "-10^6 ≤ d ≤ 10^6",
#                     "tests": [
#                         {"input": "3.14159", "output": "3.14"},
#                         {"input": "2.71828", "output": "2.72"},
#                         {"input": "5.0", "output": "5.00"}
#                     ]
#                 },

#                 {
#                     "id": "c-dt-m-2",
#                     "title": "Overflow Demonstration",
#                     "task": (
#                         "Write a C program that reads an integer n, multiplies it "
#                         "by 1000, and prints the result. Assume possible overflow."
#                     ),
#                     "input_format": "First line contains integer n.",
#                     "output_format": "Print result of n * 1000.",
#                     "sample_input": "5",
#                     "sample_output": "5000",
#                     "constraints": "-10^6 ≤ n ≤ 10^6",
#                     "tests": [
#                         {"input": "5", "output": "5000"},
#                         {"input": "-2", "output": "-2000"},
#                         {"input": "0", "output": "0"}
#                     ]
#                 },

#                 {
#                     "id": "c-dt-m-3",
#                     "title": "Mixed Data Input",
#                     "task": (
#                         "Write a C program that reads an integer, float, "
#                         "and character in one line and prints them in the same order."
#                     ),
#                     "input_format": "One line containing int, float, char.",
#                     "output_format": "Print int float char.",
#                     "sample_input": "5 2.5 A",
#                     "sample_output": "5 2.5 A",
#                     "constraints": "Valid formatted input.",
#                     "tests": [
#                         {"input": "5 2.5 A", "output": "5 2.5 A"},
#                         {"input": "0 0.0 Z", "output": "0 0.0 Z"},
#                         {"input": "-1 -1.5 B", "output": "-1 -1.5 B"}
#                     ]
#                 }

#             ]
#         },

#         "Operators": {

#             "Very Easy": [

#                 {
#                     "id": "c-op-ve-1",
#                     "title": "Addition Operator",
#                     "task": ("Write a C program that reads two integers and prints their sum using the + operator."),
#                     "input_format": "Two space-separated integers.",
#                     "output_format": "Print sum.",
#                     "sample_input": "5 3",
#                     "sample_output": "8",
#                     "constraints": "-10^9 ≤ values ≤ 10^9",
#                     "tests": [
#                         {"input": "5 3", "output": "8"},
#                         {"input": "-5 10", "output": "5"},
#                         {"input": "0 0", "output": "0"}
#                     ]
#                 },

#                 {
#                     "id": "c-op-ve-2",
#                     "title": "Subtraction Operator",
#                     "task": ("Read two integers and print the result of a - b."),
#                     "input_format": "Two integers.",
#                     "output_format": "Print difference.",
#                     "sample_input": "10 4",
#                     "sample_output": "6",
#                     "constraints": "-10^9 ≤ values ≤ 10^9",
#                     "tests": [
#                         {"input": "10 4", "output": "6"},
#                         {"input": "4 10", "output": "-6"},
#                         {"input": "-5 -5", "output": "0"},
#                         {"input": "0 5", "output": "-5"}
#                     ]
#                 },

#                 {
#                     "id": "c-op-ve-3",
#                     "title": "Multiplication Operator",
#                     "task": ("Read two integers and print their product using * operator."),
#                     "input_format": "Two integers.",
#                     "output_format": "Print product.",
#                     "sample_input": "4 5",
#                     "sample_output": "20",
#                     "constraints": "-10^6 ≤ values ≤ 10^6",
#                     "tests": [
#                         {"input": "4 5", "output": "20"},
#                         {"input": "-2 6", "output": "-12"},
#                         {"input": "0 10", "output": "0"}
#                     ]
#                 },

#                 {
#                     "id": "c-op-ve-4",
#                     "title": "Division Operator",
#                     "task": (
#                         "Read two integers and print integer division result (a / b). "
#                         "Assume b is not zero."
#                     ),
#                     "input_format": "Two integers.",
#                     "output_format": "Print integer division result.",
#                     "sample_input": "7 2",
#                     "sample_output": "3",
#                     "constraints": "b ≠ 0",
#                     "tests": [
#                         {"input": "7 2", "output": "3"},
#                         {"input": "10 5", "output": "2"},
#                         {"input": "-9 2", "output": "-4"},
#                         {"input": "1 1", "output": "1"}
#                     ]
#                 },

#                 {
#                     "id": "c-op-ve-5",
#                     "title": "Modulus Operator",
#                     "task": ("Read two integers and print the remainder (a % b)."),
#                     "input_format": "Two integers.",
#                     "output_format": "Print remainder.",
#                     "sample_input": "5 2",
#                     "sample_output": "1",
#                     "constraints": "b ≠ 0",
#                     "tests": [
#                         {"input": "5 2", "output": "1"},
#                         {"input": "10 3", "output": "1"},
#                         {"input": "7 7", "output": "0"}
#                     ]
#                 }

#             ],

#             "Easy": [

#                 {
#                     "id": "c-op-e-1",
#                     "title": "Relational Operators",
#                     "task": ("Read two integers and print 1 if a > b else 0."),
#                     "input_format": "Two integers.",
#                     "output_format": "Print 1 or 0.",
#                     "sample_input": "5 3",
#                     "sample_output": "1",
#                     "constraints": "-10^9 ≤ values ≤ 10^9",
#                     "tests": [
#                         {"input": "5 3", "output": "1"},
#                         {"input": "2 7", "output": "0"},
#                         {"input": "4 4", "output": "0"},
#                         {"input": "-1 -5", "output": "1"}
#                     ]
#                 },

#                 {
#                     "id": "c-op-e-2",
#                     "title": "Logical AND",
#                     "task": ("Read two integers and print 1 if both are positive else 0."),
#                     "input_format": "Two integers.",
#                     "output_format": "Print 1 or 0.",
#                     "sample_input": "5 3",
#                     "sample_output": "1",
#                     "constraints": "-10^9 ≤ values ≤ 10^9",
#                     "tests": [
#                         {"input": "5 3", "output": "1"},
#                         {"input": "-1 3", "output": "0"},
#                         {"input": "0 5", "output": "0"}
#                     ]
#                 },

#                 {
#                     "id": "c-op-e-3",
#                     "title": "Ternary Operator",
#                     "task": ("Use ternary operator to print the larger of two integers."),
#                     "input_format": "Two integers.",
#                     "output_format": "Print larger value.",
#                     "sample_input": "10 20",
#                     "sample_output": "20",
#                     "constraints": "-10^9 ≤ values ≤ 10^9",
#                     "tests": [
#                         {"input": "10 20", "output": "20"},
#                         {"input": "-5 -2", "output": "-2"},
#                         {"input": "7 7", "output": "7"}
#                     ]
#                 },

#                 {
#                     "id": "c-op-e-4",
#                     "title": "Bitwise AND",
#                     "task": ("Read two integers and print result of bitwise AND."),
#                     "input_format": "Two integers.",
#                     "output_format": "Print a & b.",
#                     "sample_input": "5 3",
#                     "sample_output": "1",
#                     "constraints": "0 ≤ values ≤ 10^6",
#                     "tests": [
#                         {"input": "5 3", "output": "1"},
#                         {"input": "6 2", "output": "2"},
#                         {"input": "7 7", "output": "7"},
#                         {"input": "0 5", "output": "0"}
#                     ]
#                 }

#             ],

#             "Medium": [

#                 {
#                     "id": "c-op-m-1",
#                     "title": "Compound Expression",
#                     "task": (
#                         "Read three integers a, b, c and compute expression: "
#                         "(a + b) * c - (a % b)."
#                     ),
#                     "input_format": "Three integers.",
#                     "output_format": "Print computed result.",
#                     "sample_input": "2 3 4",
#                     "sample_output": "19",
#                     "constraints": "b ≠ 0",
#                     "tests": [
#                         {"input": "2 3 4", "output": "19"},
#                         {"input": "5 2 3", "output": "20"},
#                         {"input": "10 5 2", "output": "30"},
#                         {"input": "7 3 2", "output": "19"},
#                         {"input": "1 1 1", "output": "2"}
#                     ]
#                 },

#                 {
#                     "id": "c-op-m-2",
#                     "title": "Bitwise Shift",
#                     "task": (
#                         "Read integer n and shift it left by 2 positions. "
#                         "Print the result."
#                     ),
#                     "input_format": "Single integer.",
#                     "output_format": "Print n << 2.",
#                     "sample_input": "3",
#                     "sample_output": "12",
#                     "constraints": "0 ≤ n ≤ 10^6",
#                     "tests": [
#                         {"input": "3", "output": "12"},
#                         {"input": "1", "output": "4"},
#                         {"input": "0", "output": "0"},
#                         {"input": "5", "output": "20"}
#                     ]
#                 },

#                 {
#                     "id": "c-op-m-3",
#                     "title": "Operator Precedence",
#                     "task": (
#                         "Read integers a and b and print result of: a + b * a / b. "
#                         "Assume b ≠ 0. Follow C operator precedence."
#                     ),
#                     "input_format": "Two integers.",
#                     "output_format": "Print result.",
#                     "sample_input": "4 2",
#                     "sample_output": "8",
#                     "constraints": "b ≠ 0",
#                     "tests": [
#                         {"input": "4 2", "output": "8"},
#                         {"input": "6 3", "output": "12"},
#                         {"input": "5 5", "output": "10"},
#                         {"input": "9 3", "output": "18"}
#                     ]
#                 }

#             ]
#         },

#         "Input / Output": {

#             "Very Easy": [

#                 {
#                     "id": "c-io-ve-1",
#                     "title": "Read and Print Integer",
#                     "task": (
#                         "Write a C program that reads a single integer "
#                         "from standard input using scanf and prints it using printf."
#                     ),
#                     "input_format": "Single integer n.",
#                     "output_format": "Print n.",
#                     "sample_input": "25",
#                     "sample_output": "25",
#                     "constraints": "-10^9 ≤ n ≤ 10^9",
#                     "tests": [
#                         {"input": "25", "output": "25"},
#                         {"input": "-5", "output": "-5"},
#                         {"input": "0", "output": "0"}
#                     ]
#                 },

#                 {
#                     "id": "c-io-ve-2",
#                     "title": "Read Two Integers",
#                     "task": (
#                         "Write a C program that reads two integers separated by space "
#                         "and prints them separated by space."
#                     ),
#                     "input_format": "Two space-separated integers.",
#                     "output_format": "Print both integers.",
#                     "sample_input": "5 10",
#                     "sample_output": "5 10",
#                     "constraints": "-10^9 ≤ values ≤ 10^9",
#                     "tests": [
#                         {"input": "5 10", "output": "5 10"},
#                         {"input": "-1 2", "output": "-1 2"},
#                         {"input": "0 0", "output": "0 0"}
#                     ]
#                 },

#                 {
#                     "id": "c-io-ve-3",
#                     "title": "Read Float",
#                     "task": ("Read a float value using scanf and print it exactly as entered."),
#                     "input_format": "Single float value.",
#                     "output_format": "Print float.",
#                     "sample_input": "2.5",
#                     "sample_output": "2.5",
#                     "constraints": "-10^6 ≤ value ≤ 10^6",
#                     "tests": [
#                         {"input": "2.5", "output": "2.5"},
#                         {"input": "-3.14", "output": "-3.14"},
#                         {"input": "0.0", "output": "0.0"}
#                     ]
#                 },

#                 {
#                     "id": "c-io-ve-4",
#                     "title": "Read Character",
#                     "task": ("Write a program that reads a single character and prints it."),
#                     "input_format": "Single character.",
#                     "output_format": "Print character.",
#                     "sample_input": "A",
#                     "sample_output": "A",
#                     "constraints": "Printable ASCII.",
#                     "tests": [
#                         {"input": "A", "output": "A"},
#                         {"input": "z", "output": "z"},
#                         {"input": "5", "output": "5"}
#                     ]
#                 },

#                 {
#                     "id": "c-io-ve-5",
#                     "title": "Read Long Long",
#                     "task": (
#                         "Write a program that reads a long long integer "
#                         "and prints it using correct format specifier."
#                     ),
#                     "input_format": "Single long long integer.",
#                     "output_format": "Print value.",
#                     "sample_input": "922337203685477580",
#                     "sample_output": "922337203685477580",
#                     "constraints": "Value fits in long long.",
#                     "tests": [
#                         {"input": "922337203685477580", "output": "922337203685477580"},
#                         {"input": "-100000000000", "output": "-100000000000"},
#                         {"input": "0", "output": "0"}
#                     ]
#                 }

#             ],

#             "Easy": [

#                 {
#                     "id": "c-io-e-1",
#                     "title": "Formatted Output",
#                     "task": ("Read an integer and print it in the format:\nValue: <number>"),
#                     "input_format": "Single integer.",
#                     "output_format": "Formatted output.",
#                     "sample_input": "10",
#                     "sample_output": "Value: 10",
#                     "constraints": "-10^9 ≤ n ≤ 10^9",
#                     "tests": [
#                         {"input": "10", "output": "Value: 10"},
#                         {"input": "-5", "output": "Value: -5"},
#                         {"input": "0", "output": "Value: 0"}
#                     ]
#                 },

#                 {
#                     "id": "c-io-e-2",
#                     "title": "Precision Output",
#                     "task": ("Read a double and print it rounded to exactly 3 decimal places."),
#                     "input_format": "Single double.",
#                     "output_format": "Print rounded value.",
#                     "sample_input": "3.14159",
#                     "sample_output": "3.142",
#                     "constraints": "-10^6 ≤ value ≤ 10^6",
#                     "tests": [
#                         {"input": "3.14159", "output": "3.142"},
#                         {"input": "2.5", "output": "2.500"},
#                         {"input": "0.0", "output": "0.000"},
#                         {"input": "-1.2345", "output": "-1.235"}
#                     ]
#                 },

#                 {
#                     "id": "c-io-e-3",
#                     "title": "Multiple Data Types",
#                     "task": (
#                         "Read an integer, a float, and a character in one line "
#                         "and print them in separate lines."
#                     ),
#                     "input_format": "One line: int float char.",
#                     "output_format": "Print each on new line.",
#                     "sample_input": "5 2.5 A",
#                     "sample_output": "5\n2.5\nA",
#                     "constraints": "Valid input.",
#                     "tests": [
#                         {"input": "5 2.5 A", "output": "5\n2.5\nA"},
#                         {"input": "0 0.0 Z", "output": "0\n0.0\nZ"},
#                         {"input": "-1 -1.5 B", "output": "-1\n-1.5\nB"}
#                     ]
#                 },

#                 {
#                     "id": "c-io-e-4",
#                     "title": "Echo Input Until EOF",
#                     "task": (
#                         "Write a program that reads integers until EOF "
#                         "and prints them separated by space."
#                     ),
#                     "input_format": "Multiple integers (unknown count).",
#                     "output_format": "Print all integers.",
#                     "sample_input": "1 2 3",
#                     "sample_output": "1 2 3",
#                     "constraints": "1 ≤ total numbers ≤ 10^5",
#                     "tests": [
#                         {"input": "1 2 3", "output": "1 2 3"},
#                         {"input": "5", "output": "5"},
#                         {"input": "10 20 30 40", "output": "10 20 30 40"},
#                         {"input": "-1 -2", "output": "-1 -2"}
#                     ]
#                 }

#             ],

#             "Medium": [

#                 {
#                     "id": "c-io-m-1",
#                     "title": "Read Matrix and Print",
#                     "task": (
#                         "Read integers r and c, then read an r x c matrix. "
#                         "Print the matrix in same format."
#                     ),
#                     "input_format": (
#                         "First line: r c\n"
#                         "Next r lines contain c integers each."
#                     ),
#                     "output_format": "Print matrix.",
#                     "sample_input": "2 2\n1 2\n3 4",
#                     "sample_output": "1 2\n3 4",
#                     "constraints": "1 ≤ r, c ≤ 100",
#                     "tests": [
#                         {"input": "2 2\n1 2\n3 4", "output": "1 2\n3 4"},
#                         {"input": "1 3\n5 6 7", "output": "5 6 7"},
#                         {"input": "2 1\n9\n8", "output": "9\n8"}
#                     ]
#                 },

#                 {
#                     "id": "c-io-m-2",
#                     "title": "Formatted Table Output",
#                     "task": (
#                         "Read integer n and print multiplication table from 1 to 10 "
#                         "in format: n x i = result"
#                     ),
#                     "input_format": "Single integer n.",
#                     "output_format": "Print formatted table.",
#                     "sample_input": "2",
#                     "sample_output": "2 x 1 = 2\n...\n2 x 10 = 20",
#                     "constraints": "1 ≤ n ≤ 1000",
#                     "tests": [
#                         {"input": "2", "output": "2 x 1 = 2\n2 x 2 = 4\n2 x 3 = 6\n2 x 4 = 8\n2 x 5 = 10\n2 x 6 = 12\n2 x 7 = 14\n2 x 8 = 16\n2 x 9 = 18\n2 x 10 = 20"},
#                         {"input": "1", "output": "1 x 1 = 1\n1 x 2 = 2\n1 x 3 = 3\n1 x 4 = 4\n1 x 5 = 5\n1 x 6 = 6\n1 x 7 = 7\n1 x 8 = 8\n1 x 9 = 9\n1 x 10 = 10"},
#                         {"input": "5", "output": "5 x 1 = 5\n5 x 2 = 10\n5 x 3 = 15\n5 x 4 = 20\n5 x 5 = 25\n5 x 6 = 30\n5 x 7 = 35\n5 x 8 = 40\n5 x 9 = 45\n5 x 10 = 50"}
#                     ]
#                 },

#                 {
#                     "id": "c-io-m-3",
#                     "title": "Parse Comma-Separated Input",
#                     "task": (
#                         "Read three integers separated by commas (e.g., 1,2,3) "
#                         "and print their sum."
#                     ),
#                     "input_format": "Single line: a,b,c",
#                     "output_format": "Print sum.",
#                     "sample_input": "1,2,3",
#                     "sample_output": "6",
#                     "constraints": "-10^6 ≤ values ≤ 10^6",
#                     "tests": [
#                         {"input": "1,2,3", "output": "6"},
#                         {"input": "5,5,5", "output": "15"},
#                         {"input": "-1,1,0", "output": "0"},
#                         {"input": "10,20,30", "output": "60"}
#                     ]
#                 }

#             ]
#         },

#         "Conditionals": {

#             "Very Easy": [

#                 {
#                     "id": "c-cond-ve-1",
#                     "title": "Check Positive",
#                     "task": ("Write a C program that reads an integer n and prints 'Positive' if n > 0."),
#                     "input_format": "Single integer n.",
#                     "output_format": "Print Positive if n > 0.",
#                     "sample_input": "5",
#                     "sample_output": "Positive",
#                     "constraints": "-10^9 ≤ n ≤ 10^9",
#                     "tests": [
#                         {"input": "5", "output": "Positive"},
#                         {"input": "1", "output": "Positive"},
#                         {"input": "100", "output": "Positive"}
#                     ]
#                 },

#                 {
#                     "id": "c-cond-ve-2",
#                     "title": "Check Negative",
#                     "task": ("Write a C program that reads integer n and prints 'Negative' if n < 0."),
#                     "input_format": "Single integer n.",
#                     "output_format": "Print Negative if n < 0.",
#                     "sample_input": "-5",
#                     "sample_output": "Negative",
#                     "constraints": "-10^9 ≤ n ≤ 10^9",
#                     "tests": [
#                         {"input": "-5", "output": "Negative"},
#                         {"input": "-1", "output": "Negative"},
#                         {"input": "-100", "output": "Negative"},
#                         {"input": "-999999", "output": "Negative"}
#                     ]
#                 },

#                 {
#                     "id": "c-cond-ve-3",
#                     "title": "Check Zero",
#                     "task": ("Read integer n and print 'Zero' if n equals 0."),
#                     "input_format": "Single integer.",
#                     "output_format": "Print Zero.",
#                     "sample_input": "0",
#                     "sample_output": "Zero",
#                     "constraints": "-10^9 ≤ n ≤ 10^9",
#                     "tests": [
#                         {"input": "0", "output": "Zero"},
#                         {"input": "0", "output": "Zero"},
#                         {"input": "0", "output": "Zero"}
#                     ]
#                 },

#                 {
#                     "id": "c-cond-ve-4",
#                     "title": "Even or Odd",
#                     "task": ("Read integer n and print 'Even' if n is divisible by 2, else print 'Odd'."),
#                     "input_format": "Single integer.",
#                     "output_format": "Print Even or Odd.",
#                     "sample_input": "4",
#                     "sample_output": "Even",
#                     "constraints": "-10^9 ≤ n ≤ 10^9",
#                     "tests": [
#                         {"input": "4", "output": "Even"},
#                         {"input": "3", "output": "Odd"},
#                         {"input": "0", "output": "Even"},
#                         {"input": "-5", "output": "Odd"}
#                     ]
#                 },

#                 {
#                     "id": "c-cond-ve-5",
#                     "title": "Greater Than 10",
#                     "task": ("Read integer n and print 'Yes' if n > 10 else print 'No'."),
#                     "input_format": "Single integer.",
#                     "output_format": "Print Yes or No.",
#                     "sample_input": "15",
#                     "sample_output": "Yes",
#                     "constraints": "-10^9 ≤ n ≤ 10^9",
#                     "tests": [
#                         {"input": "15", "output": "Yes"},
#                         {"input": "10", "output": "No"},
#                         {"input": "-5", "output": "No"}
#                     ]
#                 }

#             ],

#             "Easy": [

#                 {
#                     "id": "c-cond-e-1",
#                     "title": "Largest of Two Numbers",
#                     "task": (
#                         "Read two integers a and b and print the larger value. "
#                         "If both are equal, print either."
#                     ),
#                     "input_format": "Two space-separated integers.",
#                     "output_format": "Print larger value.",
#                     "sample_input": "5 9",
#                     "sample_output": "9",
#                     "constraints": "-10^9 ≤ values ≤ 10^9",
#                     "tests": [
#                         {"input": "5 9", "output": "9"},
#                         {"input": "10 2", "output": "10"},
#                         {"input": "-1 -5", "output": "-1"},
#                         {"input": "7 7", "output": "7"}
#                     ]
#                 },

#                 {
#                     "id": "c-cond-e-2",
#                     "title": "Leap Year Check",
#                     "task": (
#                         "Read integer year and print 'Leap Year' if it is a leap year, "
#                         "otherwise print 'Not Leap Year'."
#                     ),
#                     "input_format": "Single integer year.",
#                     "output_format": "Print result.",
#                     "sample_input": "2020",
#                     "sample_output": "Leap Year",
#                     "constraints": "1 ≤ year ≤ 10^5",
#                     "tests": [
#                         {"input": "2020", "output": "Leap Year"},
#                         {"input": "1900", "output": "Not Leap Year"},
#                         {"input": "2000", "output": "Leap Year"},
#                         {"input": "2023", "output": "Not Leap Year"}
#                     ]
#                 },

#                 {
#                     "id": "c-cond-e-3",
#                     "title": "Pass or Fail",
#                     "task": (
#                         "Read integer marks and print 'Pass' if marks >= 40, "
#                         "else print 'Fail'."
#                     ),
#                     "input_format": "Single integer marks.",
#                     "output_format": "Print Pass or Fail.",
#                     "sample_input": "45",
#                     "sample_output": "Pass",
#                     "constraints": "0 ≤ marks ≤ 100",
#                     "tests": [
#                         {"input": "45", "output": "Pass"},
#                         {"input": "39", "output": "Fail"},
#                         {"input": "40", "output": "Pass"}
#                     ]
#                 },

#                 {
#                     "id": "c-cond-e-4",
#                     "title": "Grade Calculator",
#                     "task": (
#                         "Read marks and assign grade:\n"
#                         "A if >= 90\n"
#                         "B if >= 75\n"
#                         "C if >= 50\n"
#                         "D otherwise"
#                     ),
#                     "input_format": "Single integer marks.",
#                     "output_format": "Print grade.",
#                     "sample_input": "85",
#                     "sample_output": "B",
#                     "constraints": "0 ≤ marks ≤ 100",
#                     "tests": [
#                         {"input": "95", "output": "A"},
#                         {"input": "80", "output": "B"},
#                         {"input": "60", "output": "C"},
#                         {"input": "30", "output": "D"},
#                         {"input": "50", "output": "C"}
#                     ]
#                 }

#             ],

#             "Medium": [

#                 {
#                     "id": "c-cond-m-1",
#                     "title": "Largest of Three Numbers",
#                     "task": ("Read three integers and print the largest among them."),
#                     "input_format": "Three space-separated integers.",
#                     "output_format": "Print largest value.",
#                     "sample_input": "3 9 5",
#                     "sample_output": "9",
#                     "constraints": "-10^9 ≤ values ≤ 10^9",
#                     "tests": [
#                         {"input": "3 9 5", "output": "9"},
#                         {"input": "10 2 1", "output": "10"},
#                         {"input": "-1 -5 -3", "output": "-1"},
#                         {"input": "7 7 7", "output": "7"}
#                     ]
#                 },

#                 {
#                     "id": "c-cond-m-2",
#                     "title": "Triangle Validity",
#                     "task": (
#                         "Read three integers representing sides of a triangle. "
#                         "Print 'Valid' if they can form a triangle, otherwise print 'Invalid'."
#                     ),
#                     "input_format": "Three integers.",
#                     "output_format": "Print Valid or Invalid.",
#                     "sample_input": "3 4 5",
#                     "sample_output": "Valid",
#                     "constraints": "1 ≤ sides ≤ 10^6",
#                     "tests": [
#                         {"input": "3 4 5", "output": "Valid"},
#                         {"input": "1 2 3", "output": "Invalid"},
#                         {"input": "5 5 5", "output": "Valid"},
#                         {"input": "2 3 4", "output": "Valid"},
#                         {"input": "10 1 1", "output": "Invalid"}
#                     ]
#                 },

#                 {
#                     "id": "c-cond-m-3",
#                     "title": "Calculator Using Switch",
#                     "task": (
#                         "Read two integers and an operator (+, -, *, /). "
#                         "Perform the operation and print the result. "
#                         "Assume division by zero will not occur."
#                     ),
#                     "input_format": "a b operator",
#                     "output_format": "Print result.",
#                     "sample_input": "5 3 +",
#                     "sample_output": "8",
#                     "constraints": "-10^6 ≤ values ≤ 10^6",
#                     "tests": [
#                         {"input": "5 3 +", "output": "8"},
#                         {"input": "10 2 -", "output": "8"},
#                         {"input": "4 5 *", "output": "20"},
#                         {"input": "8 2 /", "output": "4"}
#                     ]
#                 }

#             ]
#         },

#         "Loops": {

#             "Very Easy": [

#                 {
#                     "id": "c-loop-ve-1",
#                     "title": "Print 1 to N",
#                     "task": (
#                         "Write a C program that reads an integer n and prints "
#                         "numbers from 1 to n separated by space using a loop."
#                     ),
#                     "input_format": "Single integer n.",
#                     "output_format": "Print numbers from 1 to n.",
#                     "sample_input": "5",
#                     "sample_output": "1 2 3 4 5",
#                     "constraints": "1 ≤ n ≤ 10^5",
#                     "tests": [
#                         {"input": "5", "output": "1 2 3 4 5"},
#                         {"input": "1", "output": "1"},
#                         {"input": "3", "output": "1 2 3"}
#                     ]
#                 },

#                 {
#                     "id": "c-loop-ve-2",
#                     "title": "Print N to 1",
#                     "task": ("Read integer n and print numbers from n down to 1."),
#                     "input_format": "Single integer.",
#                     "output_format": "Print numbers descending.",
#                     "sample_input": "5",
#                     "sample_output": "5 4 3 2 1",
#                     "constraints": "1 ≤ n ≤ 10^5",
#                     "tests": [
#                         {"input": "5", "output": "5 4 3 2 1"},
#                         {"input": "1", "output": "1"},
#                         {"input": "3", "output": "3 2 1"},
#                         {"input": "2", "output": "2 1"}
#                     ]
#                 },

#                 {
#                     "id": "c-loop-ve-3",
#                     "title": "Sum 1 to N",
#                     "task": ("Read integer n and print sum of numbers from 1 to n."),
#                     "input_format": "Single integer.",
#                     "output_format": "Print sum.",
#                     "sample_input": "5",
#                     "sample_output": "15",
#                     "constraints": "1 ≤ n ≤ 10^6",
#                     "tests": [
#                         {"input": "5", "output": "15"},
#                         {"input": "1", "output": "1"},
#                         {"input": "3", "output": "6"}
#                     ]
#                 },

#                 {
#                     "id": "c-loop-ve-4",
#                     "title": "Factorial",
#                     "task": ("Read integer n and print factorial of n using loop."),
#                     "input_format": "Single integer n.",
#                     "output_format": "Print n!.",
#                     "sample_input": "4",
#                     "sample_output": "24",
#                     "constraints": "0 ≤ n ≤ 12",
#                     "tests": [
#                         {"input": "4", "output": "24"},
#                         {"input": "0", "output": "1"},
#                         {"input": "5", "output": "120"},
#                         {"input": "1", "output": "1"}
#                     ]
#                 },

#                 {
#                     "id": "c-loop-ve-5",
#                     "title": "Print Even Numbers",
#                     "task": ("Read integer n and print all even numbers from 1 to n."),
#                     "input_format": "Single integer.",
#                     "output_format": "Print even numbers.",
#                     "sample_input": "6",
#                     "sample_output": "2 4 6",
#                     "constraints": "1 ≤ n ≤ 10^5",
#                     "tests": [
#                         {"input": "6", "output": "2 4 6"},
#                         {"input": "5", "output": "2 4"},
#                         {"input": "2", "output": "2"}
#                     ]
#                 }

#             ],

#             "Easy": [

#                 {
#                     "id": "c-loop-e-1",
#                     "title": "Reverse Number",
#                     "task": ("Read integer n and print its reverse using loop."),
#                     "input_format": "Single integer n.",
#                     "output_format": "Print reversed number.",
#                     "sample_input": "123",
#                     "sample_output": "321",
#                     "constraints": "-10^9 ≤ n ≤ 10^9",
#                     "tests": [
#                         {"input": "123", "output": "321"},
#                         {"input": "100", "output": "1"},
#                         {"input": "9", "output": "9"},
#                         {"input": "-456", "output": "-654"}
#                     ]
#                 },

#                 {
#                     "id": "c-loop-e-2",
#                     "title": "Count Digits",
#                     "task": ("Read integer n and print number of digits."),
#                     "input_format": "Single integer.",
#                     "output_format": "Print digit count.",
#                     "sample_input": "1234",
#                     "sample_output": "4",
#                     "constraints": "-10^9 ≤ n ≤ 10^9",
#                     "tests": [
#                         {"input": "1234", "output": "4"},
#                         {"input": "0", "output": "1"},
#                         {"input": "-567", "output": "3"}
#                     ]
#                 },

#                 {
#                     "id": "c-loop-e-3",
#                     "title": "Check Prime",
#                     "task": ("Read integer n and print 'Prime' if prime else 'Not Prime'."),
#                     "input_format": "Single integer n.",
#                     "output_format": "Print Prime or Not Prime.",
#                     "sample_input": "7",
#                     "sample_output": "Prime",
#                     "constraints": "1 ≤ n ≤ 10^5",
#                     "tests": [
#                         {"input": "7", "output": "Prime"},
#                         {"input": "4", "output": "Not Prime"},
#                         {"input": "2", "output": "Prime"},
#                         {"input": "1", "output": "Not Prime"}
#                     ]
#                 },

#                 {
#                     "id": "c-loop-e-4",
#                     "title": "Fibonacci N Terms",
#                     "task": ("Read integer n and print first n Fibonacci numbers."),
#                     "input_format": "Single integer n.",
#                     "output_format": "Print Fibonacci sequence.",
#                     "sample_input": "5",
#                     "sample_output": "0 1 1 2 3",
#                     "constraints": "1 ≤ n ≤ 20",
#                     "tests": [
#                         {"input": "5", "output": "0 1 1 2 3"},
#                         {"input": "1", "output": "0"},
#                         {"input": "2", "output": "0 1"}
#                     ]
#                 }

#             ],

#             "Medium": [

#                 {
#                     "id": "c-loop-m-1",
#                     "title": "Armstrong Number",
#                     "task": (
#                         "Read integer n and check whether it is an Armstrong number. "
#                         "Print 'Yes' if Armstrong else 'No'."
#                     ),
#                     "input_format": "Single integer n.",
#                     "output_format": "Print Yes or No.",
#                     "sample_input": "153",
#                     "sample_output": "Yes",
#                     "constraints": "1 ≤ n ≤ 10^6",
#                     "tests": [
#                         {"input": "153", "output": "Yes"},
#                         {"input": "370", "output": "Yes"},
#                         {"input": "123", "output": "No"},
#                         {"input": "9474", "output": "Yes"}
#                     ]
#                 },

#                 {
#                     "id": "c-loop-m-2",
#                     "title": "GCD of Two Numbers",
#                     "task": ("Read two integers and compute their GCD using loop."),
#                     "input_format": "Two integers.",
#                     "output_format": "Print GCD.",
#                     "sample_input": "4 6",
#                     "sample_output": "2",
#                     "constraints": "1 ≤ values ≤ 10^5",
#                     "tests": [
#                         {"input": "4 6", "output": "2"},
#                         {"input": "5 7", "output": "1"},
#                         {"input": "9 3", "output": "3"},
#                         {"input": "10 5", "output": "5"}
#                     ]
#                 },

#                 {
#                     "id": "c-loop-m-3",
#                     "title": "Pattern Pyramid",
#                     "task": ("Read integer n and print star pyramid pattern."),
#                     "input_format": "Single integer n.",
#                     "output_format": "Print pyramid pattern.",
#                     "sample_input": "3",
#                     "sample_output": "  *\n ***\n*****",
#                     "constraints": "1 ≤ n ≤ 20",
#                     "tests": [
#                         {"input": "3", "output": "  *\n ***\n*****"},
#                         {"input": "1", "output": "*"},
#                         {"input": "2", "output": " *\n***"},
#                         {"input": "4", "output": "   *\n  ***\n *****\n*******"}
#                     ]
#                 }

#             ]
#         },

#         "Functions": {

#             "Very Easy": [

#                 {
#                     "id": "c-func-ve-1",
#                     "title": "Function to Add Two Numbers",
#                     "task": (
#                         "Write a C program that defines a function "
#                         "add(int a, int b) which returns their sum. "
#                         "Call the function from main and print the result."
#                     ),
#                     "input_format": "Two integers.",
#                     "output_format": "Print sum.",
#                     "sample_input": "5 3",
#                     "sample_output": "8",
#                     "constraints": "-10^9 ≤ values ≤ 10^9",
#                     "tests": [
#                         {"input": "5 3", "output": "8"},
#                         {"input": "-1 5", "output": "4"},
#                         {"input": "0 0", "output": "0"}
#                     ]
#                 },

#                 {
#                     "id": "c-func-ve-2",
#                     "title": "Function to Square Number",
#                     "task": (
#                         "Define a function square(int n) that returns n*n. "
#                         "Read integer and print square using the function."
#                     ),
#                     "input_format": "Single integer.",
#                     "output_format": "Print square.",
#                     "sample_input": "4",
#                     "sample_output": "16",
#                     "constraints": "-10^6 ≤ n ≤ 10^6",
#                     "tests": [
#                         {"input": "4", "output": "16"},
#                         {"input": "-3", "output": "9"},
#                         {"input": "0", "output": "0"}
#                     ]
#                 },

#                 {
#                     "id": "c-func-ve-3",
#                     "title": "Check Even Using Function",
#                     "task": (
#                         "Define a function isEven(int n) that returns 1 if even else 0. "
#                         "Print 'Even' or 'Odd' based on return value."
#                     ),
#                     "input_format": "Single integer.",
#                     "output_format": "Print Even or Odd.",
#                     "sample_input": "4",
#                     "sample_output": "Even",
#                     "constraints": "-10^9 ≤ n ≤ 10^9",
#                     "tests": [
#                         {"input": "4", "output": "Even"},
#                         {"input": "3", "output": "Odd"},
#                         {"input": "0", "output": "Even"},
#                         {"input": "-5", "output": "Odd"}
#                     ]
#                 },

#                 {
#                     "id": "c-func-ve-4",
#                     "title": "Maximum of Two",
#                     "task": ("Write a function max(int a, int b) that returns the larger value."),
#                     "input_format": "Two integers.",
#                     "output_format": "Print maximum.",
#                     "sample_input": "5 9",
#                     "sample_output": "9",
#                     "constraints": "-10^9 ≤ values ≤ 10^9",
#                     "tests": [
#                         {"input": "5 9", "output": "9"},
#                         {"input": "-1 -5", "output": "-1"},
#                         {"input": "7 7", "output": "7"}
#                     ]
#                 },

#                 {
#                     "id": "c-func-ve-5",
#                     "title": "Print Message Using Function",
#                     "task": (
#                         "Write a void function printMsg() that prints "
#                         "'C Functions are Powerful'. Call it from main."
#                     ),
#                     "input_format": "No input.",
#                     "output_format": "Print message.",
#                     "sample_input": "",
#                     "sample_output": "C Functions are Powerful",
#                     "constraints": "Use void return type.",
#                     "tests": [
#                         {"input": "", "output": "C Functions are Powerful"},
#                         {"input": "", "output": "C Functions are Powerful"},
#                         {"input": "", "output": "C Functions are Powerful"}
#                     ]
#                 }

#             ],

#             "Easy": [

#                 {
#                     "id": "c-func-e-1",
#                     "title": "Factorial Using Function",
#                     "task": ("Write a function factorial(int n) that returns n! using loop."),
#                     "input_format": "Single integer n.",
#                     "output_format": "Print factorial.",
#                     "sample_input": "4",
#                     "sample_output": "24",
#                     "constraints": "0 ≤ n ≤ 12",
#                     "tests": [
#                         {"input": "4", "output": "24"},
#                         {"input": "0", "output": "1"},
#                         {"input": "5", "output": "120"},
#                         {"input": "1", "output": "1"}
#                     ]
#                 },

#                 {
#                     "id": "c-func-e-2",
#                     "title": "Prime Check Function",
#                     "task": ("Write a function isPrime(int n) that returns 1 if prime else 0."),
#                     "input_format": "Single integer n.",
#                     "output_format": "Print Prime or Not Prime.",
#                     "sample_input": "7",
#                     "sample_output": "Prime",
#                     "constraints": "1 ≤ n ≤ 10^5",
#                     "tests": [
#                         {"input": "7", "output": "Prime"},
#                         {"input": "4", "output": "Not Prime"},
#                         {"input": "2", "output": "Prime"},
#                         {"input": "1", "output": "Not Prime"}
#                     ]
#                 },

#                 {
#                     "id": "c-func-e-3",
#                     "title": "Swap Using Function",
#                     "task": ("Write a function to swap two numbers using call by reference (pointers)."),
#                     "input_format": "Two integers.",
#                     "output_format": "Print swapped values.",
#                     "sample_input": "5 10",
#                     "sample_output": "10 5",
#                     "constraints": "-10^9 ≤ values ≤ 10^9",
#                     "tests": [
#                         {"input": "5 10", "output": "10 5"},
#                         {"input": "-1 1", "output": "1 -1"},
#                         {"input": "0 0", "output": "0 0"}
#                     ]
#                 },

#                 {
#                     "id": "c-func-e-4",
#                     "title": "Recursive Fibonacci",
#                     "task": ("Write a recursive function to compute nth Fibonacci number."),
#                     "input_format": "Single integer n.",
#                     "output_format": "Print nth Fibonacci.",
#                     "sample_input": "6",
#                     "sample_output": "8",
#                     "constraints": "0 ≤ n ≤ 20",
#                     "tests": [
#                         {"input": "6", "output": "8"},
#                         {"input": "0", "output": "0"},
#                         {"input": "1", "output": "1"}
#                     ]
#                 }

#             ],

#             "Medium": [

#                 {
#                     "id": "c-func-m-1",
#                     "title": "GCD Using Recursion",
#                     "task": (
#                         "Write a recursive function to compute GCD "
#                         "of two integers using Euclidean algorithm."
#                     ),
#                     "input_format": "Two integers.",
#                     "output_format": "Print GCD.",
#                     "sample_input": "48 18",
#                     "sample_output": "6",
#                     "constraints": "1 ≤ values ≤ 10^5",
#                     "tests": [
#                         {"input": "48 18", "output": "6"},
#                         {"input": "5 7", "output": "1"},
#                         {"input": "9 3", "output": "3"},
#                         {"input": "100 10", "output": "10"}
#                     ]
#                 },

#                 {
#                     "id": "c-func-m-2",
#                     "title": "Power Function (Recursive)",
#                     "task": ("Write recursive function power(int a, int b) that returns a^b."),
#                     "input_format": "Two integers a and b.",
#                     "output_format": "Print a^b.",
#                     "sample_input": "2 5",
#                     "sample_output": "32",
#                     "constraints": "-100 ≤ a ≤ 100, 0 ≤ b ≤ 10",
#                     "tests": [
#                         {"input": "2 5", "output": "32"},
#                         {"input": "5 0", "output": "1"},
#                         {"input": "-2 2", "output": "4"},
#                         {"input": "3 3", "output": "27"}
#                     ]
#                 },

#                 {
#                     "id": "c-func-m-3",
#                     "title": "Palindrome Check Using Function",
#                     "task": (
#                         "Write a function that checks if a number is palindrome "
#                         "and returns 1 if true else 0."
#                     ),
#                     "input_format": "Single integer n.",
#                     "output_format": "Print Yes or No.",
#                     "sample_input": "121",
#                     "sample_output": "Yes",
#                     "constraints": "-10^9 ≤ n ≤ 10^9",
#                     "tests": [
#                         {"input": "121", "output": "Yes"},
#                         {"input": "123", "output": "No"},
#                         {"input": "7", "output": "Yes"},
#                         {"input": "1001", "output": "Yes"}
#                     ]
#                 }

#             ]
#         },

#         "Arrays": {

#             "Very Easy": [

#                 {
#                     "id": "c-arr-ve-1",
#                     "title": "Print Array Elements",
#                     "task": (
#                         "Write a C program that reads integer n, then reads n integers "
#                         "into an array and prints them in the same order."
#                     ),
#                     "input_format": "First line n. Second line n integers.",
#                     "output_format": "Print array elements.",
#                     "sample_input": "3\n1 2 3",
#                     "sample_output": "1 2 3",
#                     "constraints": "1 ≤ n ≤ 10^5",
#                     "tests": [
#                         {"input": "3\n1 2 3", "output": "1 2 3"},
#                         {"input": "1\n5", "output": "5"},
#                         {"input": "4\n9 8 7 6", "output": "9 8 7 6"}
#                     ]
#                 },

#                 {
#                     "id": "c-arr-ve-2",
#                     "title": "Sum of Array",
#                     "task": ("Read n and n integers into an array and print their sum."),
#                     "input_format": "n followed by n integers.",
#                     "output_format": "Print sum.",
#                     "sample_input": "3\n1 2 3",
#                     "sample_output": "6",
#                     "constraints": "1 ≤ n ≤ 10^5",
#                     "tests": [
#                         {"input": "3\n1 2 3", "output": "6"},
#                         {"input": "1\n5", "output": "5"},
#                         {"input": "4\n-1 1 -2 2", "output": "0"}
#                     ]
#                 },

#                 {
#                     "id": "c-arr-ve-3",
#                     "title": "Find Maximum Element",
#                     "task": ("Read n and array elements. Print the maximum value."),
#                     "input_format": "n followed by n integers.",
#                     "output_format": "Print maximum element.",
#                     "sample_input": "3\n1 5 3",
#                     "sample_output": "5",
#                     "constraints": "1 ≤ n ≤ 10^5",
#                     "tests": [
#                         {"input": "3\n1 5 3", "output": "5"},
#                         {"input": "1\n10", "output": "10"},
#                         {"input": "4\n-1 -2 -3 -4", "output": "-1"}
#                     ]
#                 },

#                 {
#                     "id": "c-arr-ve-4",
#                     "title": "Find Minimum Element",
#                     "task": ("Read n and array elements. Print the minimum value."),
#                     "input_format": "n followed by n integers.",
#                     "output_format": "Print minimum element.",
#                     "sample_input": "3\n1 5 3",
#                     "sample_output": "1",
#                     "constraints": "1 ≤ n ≤ 10^5",
#                     "tests": [
#                         {"input": "3\n1 5 3", "output": "1"},
#                         {"input": "1\n10", "output": "10"},
#                         {"input": "4\n-1 -2 -3 -4", "output": "-4"}
#                     ]
#                 },

#                 {
#                     "id": "c-arr-ve-5",
#                     "title": "Count Even Numbers",
#                     "task": ("Read n and array elements. Count how many numbers are even."),
#                     "input_format": "n followed by n integers.",
#                     "output_format": "Print count of even numbers.",
#                     "sample_input": "4\n1 2 3 4",
#                     "sample_output": "2",
#                     "constraints": "1 ≤ n ≤ 10^5",
#                     "tests": [
#                         {"input": "4\n1 2 3 4", "output": "2"},
#                         {"input": "3\n2 4 6", "output": "3"},
#                         {"input": "2\n1 3", "output": "0"}
#                     ]
#                 }

#             ],

#             "Easy": [

#                 {
#                     "id": "c-arr-e-1",
#                     "title": "Reverse Array",
#                     "task": ("Read n and array elements. Print the array in reverse order."),
#                     "input_format": "n followed by n integers.",
#                     "output_format": "Print reversed array.",
#                     "sample_input": "3\n1 2 3",
#                     "sample_output": "3 2 1",
#                     "constraints": "1 ≤ n ≤ 10^5",
#                     "tests": [
#                         {"input": "3\n1 2 3", "output": "3 2 1"},
#                         {"input": "1\n5", "output": "5"},
#                         {"input": "4\n9 8 7 6", "output": "6 7 8 9"},
#                         {"input": "2\n10 20", "output": "20 10"}
#                     ]
#                 },

#                 {
#                     "id": "c-arr-e-2",
#                     "title": "Search Element",
#                     "task": (
#                         "Read n, array elements and target x. "
#                         "Print index (0-based) if found else -1."
#                     ),
#                     "input_format": "n, array elements, then x.",
#                     "output_format": "Print index or -1.",
#                     "sample_input": "3\n1 2 3\n2",
#                     "sample_output": "1",
#                     "constraints": "1 ≤ n ≤ 10^5",
#                     "tests": [
#                         {"input": "3\n1 2 3\n2", "output": "1"},
#                         {"input": "3\n1 2 3\n5", "output": "-1"},
#                         {"input": "1\n10\n10", "output": "0"}
#                     ]
#                 },

#                 {
#                     "id": "c-arr-e-3",
#                     "title": "Second Largest Element",
#                     "task": ("Read n and array elements. Print second largest element."),
#                     "input_format": "n followed by n integers.",
#                     "output_format": "Print second largest.",
#                     "sample_input": "4\n1 5 3 9",
#                     "sample_output": "5",
#                     "constraints": "2 ≤ n ≤ 10^5",
#                     "tests": [
#                         {"input": "4\n1 5 3 9", "output": "5"},
#                         {"input": "3\n10 20 30", "output": "20"},
#                         {"input": "5\n5 5 5 5 6", "output": "5"},
#                         {"input": "2\n1 2", "output": "1"}
#                     ]
#                 },

#                 {
#                     "id": "c-arr-e-4",
#                     "title": "Rotate Array Left",
#                     "task": ("Read n and k. Rotate the array left by k positions."),
#                     "input_format": "n, array elements, then k.",
#                     "output_format": "Print rotated array.",
#                     "sample_input": "5\n1 2 3 4 5\n2",
#                     "sample_output": "3 4 5 1 2",
#                     "constraints": "1 ≤ n ≤ 10^5",
#                     "tests": [
#                         {"input": "5\n1 2 3 4 5\n2", "output": "3 4 5 1 2"},
#                         {"input": "3\n1 2 3\n1", "output": "2 3 1"},
#                         {"input": "1\n5\n3", "output": "5"},
#                         {"input": "4\n1 2 3 4\n4", "output": "1 2 3 4"}
#                     ]
#                 }

#             ],

#             "Medium": [

#                 {
#                     "id": "c-arr-m-1",
#                     "title": "Kadane's Algorithm",
#                     "task": (
#                         "Read n and array elements. Print maximum subarray sum "
#                         "using efficient approach."
#                     ),
#                     "input_format": "n followed by n integers.",
#                     "output_format": "Print max subarray sum.",
#                     "sample_input": "9\n-2 1 -3 4 -1 2 1 -5 4",
#                     "sample_output": "6",
#                     "constraints": "1 ≤ n ≤ 10^5",
#                     "tests": [
#                         {"input": "9\n-2 1 -3 4 -1 2 1 -5 4", "output": "6"},
#                         {"input": "3\n1 2 3", "output": "6"},
#                         {"input": "3\n-1 -2 -3", "output": "-1"},
#                         {"input": "5\n5 -2 3 4 -1", "output": "10"}
#                     ]
#                 },

#                 {
#                     "id": "c-arr-m-2",
#                     "title": "Two Sum",
#                     "task": (
#                         "Read n, array elements and target. "
#                         "Print 'Yes' if any two numbers sum to target else 'No'."
#                     ),
#                     "input_format": "n, array elements, then target.",
#                     "output_format": "Print Yes or No.",
#                     "sample_input": "4\n1 2 3 4\n5",
#                     "sample_output": "Yes",
#                     "constraints": "1 ≤ n ≤ 10^5",
#                     "tests": [
#                         {"input": "4\n1 2 3 4\n5", "output": "Yes"},
#                         {"input": "3\n1 2 3\n7", "output": "No"},
#                         {"input": "2\n5 5\n10", "output": "Yes"},
#                         {"input": "5\n1 1 1 1 1\n3", "output": "No"}
#                     ]
#                 },

#                 {
#                     "id": "c-arr-m-3",
#                     "title": "Merge Two Sorted Arrays",
#                     "task": (
#                         "Read two sorted arrays and merge them into a single "
#                         "sorted array."
#                     ),
#                     "input_format": (
#                         "First line n, then n elements.\n"
#                         "Second line m, then m elements."
#                     ),
#                     "output_format": "Print merged sorted array.",
#                     "sample_input": "3\n1 3 5\n3\n2 4 6",
#                     "sample_output": "1 2 3 4 5 6",
#                     "constraints": "1 ≤ n,m ≤ 10^5",
#                     "tests": [
#                         {"input": "3\n1 3 5\n3\n2 4 6", "output": "1 2 3 4 5 6"},
#                         {"input": "1\n1\n1\n2", "output": "1 2"},
#                         {"input": "2\n1 2\n2\n3 4", "output": "1 2 3 4"}
#                     ]
#                 }

#             ]
#         },

#         "Strings": {

#             "Very Easy": [

#                 {
#                     "id": "c-str-ve-1",
#                     "title": "Print String",
#                     "task": (
#                         "Write a C program that reads a string (without spaces) "
#                         "and prints it."
#                     ),
#                     "input_format": "Single word string.",
#                     "output_format": "Print the string.",
#                     "sample_input": "Hello",
#                     "sample_output": "Hello",
#                     "constraints": "1 ≤ length ≤ 100",
#                     "tests": [
#                         {"input": "Hello", "output": "Hello"},
#                         {"input": "CProgramming", "output": "CProgramming"},
#                         {"input": "A", "output": "A"}
#                     ]
#                 },

#                 {
#                     "id": "c-str-ve-2",
#                     "title": "String Length",
#                     "task": ("Read a string and print its length using strlen()."),
#                     "input_format": "Single word string.",
#                     "output_format": "Print length.",
#                     "sample_input": "Hello",
#                     "sample_output": "5",
#                     "constraints": "1 ≤ length ≤ 10^5",
#                     "tests": [
#                         {"input": "Hello", "output": "5"},
#                         {"input": "A", "output": "1"},
#                         {"input": "Programming", "output": "11"}
#                     ]
#                 },

#                 {
#                     "id": "c-str-ve-3",
#                     "title": "Count Vowels",
#                     "task": (
#                         "Read a string and count number of vowels "
#                         "(a, e, i, o, u both lowercase and uppercase)."
#                     ),
#                     "input_format": "Single word string.",
#                     "output_format": "Print vowel count.",
#                     "sample_input": "Hello",
#                     "sample_output": "2",
#                     "constraints": "1 ≤ length ≤ 10^5",
#                     "tests": [
#                         {"input": "Hello", "output": "2"},
#                         {"input": "AEIOU", "output": "5"},
#                         {"input": "xyz", "output": "0"},
#                         {"input": "Programming", "output": "3"}
#                     ]
#                 },

#                 {
#                     "id": "c-str-ve-4",
#                     "title": "Reverse String",
#                     "task": ("Read a string and print it reversed."),
#                     "input_format": "Single word string.",
#                     "output_format": "Print reversed string.",
#                     "sample_input": "Code",
#                     "sample_output": "edoC",
#                     "constraints": "1 ≤ length ≤ 10^5",
#                     "tests": [
#                         {"input": "Code", "output": "edoC"},
#                         {"input": "A", "output": "A"},
#                         {"input": "123", "output": "321"}
#                     ]
#                 },

#                 {
#                     "id": "c-str-ve-5",
#                     "title": "Compare Two Strings",
#                     "task": (
#                         "Read two strings and print 'Equal' if they are identical, "
#                         "else print 'Not Equal'."
#                     ),
#                     "input_format": "Two strings (separate lines).",
#                     "output_format": "Print Equal or Not Equal.",
#                     "sample_input": "Hello\nHello",
#                     "sample_output": "Equal",
#                     "constraints": "1 ≤ length ≤ 10^5",
#                     "tests": [
#                         {"input": "Hello\nHello", "output": "Equal"},
#                         {"input": "Hi\nhi", "output": "Not Equal"},
#                         {"input": "A\nB", "output": "Not Equal"}
#                     ]
#                 }

#             ],

#             "Easy": [

#                 {
#                     "id": "c-str-e-1",
#                     "title": "Check Palindrome",
#                     "task": ("Read a string and check whether it is palindrome. Print 'Yes' or 'No'."),
#                     "input_format": "Single word string.",
#                     "output_format": "Print Yes or No.",
#                     "sample_input": "madam",
#                     "sample_output": "Yes",
#                     "constraints": "1 ≤ length ≤ 10^5",
#                     "tests": [
#                         {"input": "madam", "output": "Yes"},
#                         {"input": "hello", "output": "No"},
#                         {"input": "racecar", "output": "Yes"},
#                         {"input": "a", "output": "Yes"}
#                     ]
#                 },

#                 {
#                     "id": "c-str-e-2",
#                     "title": "Count Words",
#                     "task": (
#                         "Read a sentence (may contain spaces) and count "
#                         "number of words."
#                     ),
#                     "input_format": "Single line sentence.",
#                     "output_format": "Print word count.",
#                     "sample_input": "C is powerful",
#                     "sample_output": "3",
#                     "constraints": "1 ≤ length ≤ 10^5",
#                     "tests": [
#                         {"input": "C is powerful", "output": "3"},
#                         {"input": "Hello", "output": "1"},
#                         {"input": "One two three four", "output": "4"}
#                     ]
#                 },

#                 {
#                     "id": "c-str-e-3",
#                     "title": "Convert to Uppercase",
#                     "task": (
#                         "Read a string and convert all lowercase characters "
#                         "to uppercase."
#                     ),
#                     "input_format": "Single word string.",
#                     "output_format": "Print uppercase string.",
#                     "sample_input": "hello",
#                     "sample_output": "HELLO",
#                     "constraints": "1 ≤ length ≤ 10^5",
#                     "tests": [
#                         {"input": "hello", "output": "HELLO"},
#                         {"input": "Code123", "output": "CODE123"},
#                         {"input": "aBcD", "output": "ABCD"}
#                     ]
#                 },

#                 {
#                     "id": "c-str-e-4",
#                     "title": "Remove Spaces",
#                     "task": ("Read a sentence and print it after removing all spaces."),
#                     "input_format": "Single line sentence.",
#                     "output_format": "Print modified string.",
#                     "sample_input": "C Programming Language",
#                     "sample_output": "CProgrammingLanguage",
#                     "constraints": "1 ≤ length ≤ 10^5",
#                     "tests": [
#                         {"input": "C Programming Language", "output": "CProgrammingLanguage"},
#                         {"input": "Hello World", "output": "HelloWorld"},
#                         {"input": "NoSpaces", "output": "NoSpaces"}
#                     ]
#                 }

#             ],

#             "Medium": [

#                 {
#                     "id": "c-str-m-1",
#                     "title": "Anagram Check",
#                     "task": ("Read two strings and check if they are anagrams. Print 'Yes' or 'No'."),
#                     "input_format": "Two strings (separate lines).",
#                     "output_format": "Print Yes or No.",
#                     "sample_input": "listen\nsilent",
#                     "sample_output": "Yes",
#                     "constraints": "1 ≤ length ≤ 10^5",
#                     "tests": [
#                         {"input": "listen\nsilent", "output": "Yes"},
#                         {"input": "hello\nworld", "output": "No"},
#                         {"input": "triangle\nintegral", "output": "Yes"},
#                         {"input": "abc\nabcd", "output": "No"}
#                     ]
#                 },

#                 {
#                     "id": "c-str-m-2",
#                     "title": "Longest Word",
#                     "task": (
#                         "Read a sentence and print the longest word in it. "
#                         "If multiple words have same maximum length, print first one."
#                     ),
#                     "input_format": "Single line sentence.",
#                     "output_format": "Print longest word.",
#                     "sample_input": "C programming is powerful",
#                     "sample_output": "programming",
#                     "constraints": "1 ≤ length ≤ 10^5",
#                     "tests": [
#                         {"input": "C programming is powerful", "output": "programming"},
#                         {"input": "I love C", "output": "love"},
#                         {"input": "One two three", "output": "three"}
#                     ]
#                 },

#                 {
#                     "id": "c-str-m-3",
#                     "title": "Substring Occurrence Count",
#                     "task": (
#                         "Read string s and substring sub. "
#                         "Count how many times sub appears in s."
#                     ),
#                     "input_format": "Two lines: s and sub.",
#                     "output_format": "Print occurrence count.",
#                     "sample_input": "abababa\naba",
#                     "sample_output": "2",
#                     "constraints": "1 ≤ length ≤ 10^5",
#                     "tests": [
#                         {"input": "abababa\naba", "output": "2"},
#                         {"input": "aaaaa\naa", "output": "2"},
#                         {"input": "hello\nlo", "output": "1"},
#                         {"input": "abc\nxyz", "output": "0"}
#                     ]
#                 }

#             ]
#         },

#         "Pointers": {

#             "Very Easy": [

#                 {
#                     "id": "c-ptr-ve-1",
#                     "title": "Print Value Using Pointer",
#                     "task": (
#                         "Write a C program that reads an integer, stores it in a variable, "
#                         "assigns its address to a pointer, and prints the value using the pointer."
#                     ),
#                     "input_format": "Single integer n.",
#                     "output_format": "Print value using pointer dereferencing.",
#                     "sample_input": "5",
#                     "sample_output": "5",
#                     "constraints": "-10^9 ≤ n ≤ 10^9",
#                     "tests": [
#                         {"input": "5", "output": "5"},
#                         {"input": "-10", "output": "-10"},
#                         {"input": "0", "output": "0"}
#                     ]
#                 },

#                 {
#                     "id": "c-ptr-ve-2",
#                     "title": "Modify Value Using Pointer",
#                     "task": (
#                         "Read an integer, use a pointer to increase its value by 10, "
#                         "and print the updated value."
#                     ),
#                     "input_format": "Single integer n.",
#                     "output_format": "Print updated value.",
#                     "sample_input": "5",
#                     "sample_output": "15",
#                     "constraints": "-10^9 ≤ n ≤ 10^9",
#                     "tests": [
#                         {"input": "5", "output": "15"},
#                         {"input": "0", "output": "10"},
#                         {"input": "-5", "output": "5"}
#                     ]
#                 },

#                 {
#                     "id": "c-ptr-ve-3",
#                     "title": "Swap Two Numbers Using Pointers",
#                     "task": (
#                         "Write a program that reads two integers and swaps them "
#                         "using pointer variables."
#                     ),
#                     "input_format": "Two integers.",
#                     "output_format": "Print swapped values.",
#                     "sample_input": "5 10",
#                     "sample_output": "10 5",
#                     "constraints": "-10^9 ≤ values ≤ 10^9",
#                     "tests": [
#                         {"input": "5 10", "output": "10 5"},
#                         {"input": "-1 1", "output": "1 -1"},
#                         {"input": "0 0", "output": "0 0"}
#                     ]
#                 },

#                 {
#                     "id": "c-ptr-ve-4",
#                     "title": "Pointer to Array",
#                     "task": (
#                         "Read n and n integers into an array. "
#                         "Use a pointer to print all array elements."
#                     ),
#                     "input_format": "n followed by n integers.",
#                     "output_format": "Print array elements.",
#                     "sample_input": "3\n1 2 3",
#                     "sample_output": "1 2 3",
#                     "constraints": "1 ≤ n ≤ 10^5",
#                     "tests": [
#                         {"input": "3\n1 2 3", "output": "1 2 3"},
#                         {"input": "1\n5", "output": "5"},
#                         {"input": "4\n9 8 7 6", "output": "9 8 7 6"}
#                     ]
#                 },

#                 {
#                     "id": "c-ptr-ve-5",
#                     "title": "Pointer Arithmetic",
#                     "task": (
#                         "Read n and n integers. Using pointer arithmetic, "
#                         "print the last element of the array."
#                     ),
#                     "input_format": "n followed by n integers.",
#                     "output_format": "Print last element.",
#                     "sample_input": "3\n1 2 3",
#                     "sample_output": "3",
#                     "constraints": "1 ≤ n ≤ 10^5",
#                     "tests": [
#                         {"input": "3\n1 2 3", "output": "3"},
#                         {"input": "1\n5", "output": "5"},
#                         {"input": "4\n9 8 7 6", "output": "6"}
#                     ]
#                 }

#             ],

#             "Easy": [

#                 {
#                     "id": "c-ptr-e-1",
#                     "title": "Sum of Array Using Pointer",
#                     "task": (
#                         "Read n and array elements. Use pointer traversal "
#                         "to compute and print sum."
#                     ),
#                     "input_format": "n followed by n integers.",
#                     "output_format": "Print sum.",
#                     "sample_input": "3\n1 2 3",
#                     "sample_output": "6",
#                     "constraints": "1 ≤ n ≤ 10^5",
#                     "tests": [
#                         {"input": "3\n1 2 3", "output": "6"},
#                         {"input": "1\n5", "output": "5"},
#                         {"input": "4\n-1 1 -2 2", "output": "0"},
#                         {"input": "2\n10 20", "output": "30"}
#                     ]
#                 },

#                 {
#                     "id": "c-ptr-e-2",
#                     "title": "Reverse Array Using Pointer",
#                     "task": ("Read n and array elements. Reverse array using pointer swapping."),
#                     "input_format": "n followed by n integers.",
#                     "output_format": "Print reversed array.",
#                     "sample_input": "3\n1 2 3",
#                     "sample_output": "3 2 1",
#                     "constraints": "1 ≤ n ≤ 10^5",
#                     "tests": [
#                         {"input": "3\n1 2 3", "output": "3 2 1"},
#                         {"input": "1\n5", "output": "5"},
#                         {"input": "4\n9 8 7 6", "output": "6 7 8 9"}
#                     ]
#                 },

#                 {
#                     "id": "c-ptr-e-3",
#                     "title": "Pointer to Pointer",
#                     "task": (
#                         "Read an integer. Create pointer to it and then pointer to pointer. "
#                         "Print the value using double dereferencing."
#                     ),
#                     "input_format": "Single integer.",
#                     "output_format": "Print value.",
#                     "sample_input": "10",
#                     "sample_output": "10",
#                     "constraints": "-10^9 ≤ n ≤ 10^9",
#                     "tests": [
#                         {"input": "10", "output": "10"},
#                         {"input": "-5", "output": "-5"},
#                         {"input": "0", "output": "0"}
#                     ]
#                 },

#                 {
#                     "id": "c-ptr-e-4",
#                     "title": "Function with Pointer Argument",
#                     "task": (
#                         "Write a function that accepts pointer to integer "
#                         "and doubles its value."
#                     ),
#                     "input_format": "Single integer.",
#                     "output_format": "Print doubled value.",
#                     "sample_input": "5",
#                     "sample_output": "10",
#                     "constraints": "-10^9 ≤ n ≤ 10^9",
#                     "tests": [
#                         {"input": "5", "output": "10"},
#                         {"input": "0", "output": "0"},
#                         {"input": "-3", "output": "-6"},
#                         {"input": "100", "output": "200"}
#                     ]
#                 }

#             ],

#             "Medium": [

#                 {
#                     "id": "c-ptr-m-1",
#                     "title": "Dynamic Memory with Pointer",
#                     "task": (
#                         "Read n. Dynamically allocate memory for n integers "
#                         "using malloc. Read values and print their sum."
#                     ),
#                     "input_format": "n followed by n integers.",
#                     "output_format": "Print sum.",
#                     "sample_input": "3\n1 2 3",
#                     "sample_output": "6",
#                     "constraints": "1 ≤ n ≤ 10^5",
#                     "tests": [
#                         {"input": "3\n1 2 3", "output": "6"},
#                         {"input": "1\n5", "output": "5"},
#                         {"input": "4\n-1 1 -2 2", "output": "0"}
#                     ]
#                 },

#                 {
#                     "id": "c-ptr-m-2",
#                     "title": "Sort Using Pointer",
#                     "task": (
#                         "Read n and array elements. Use pointer-based bubble sort "
#                         "to sort array in ascending order."
#                     ),
#                     "input_format": "n followed by n integers.",
#                     "output_format": "Print sorted array.",
#                     "sample_input": "3\n3 1 2",
#                     "sample_output": "1 2 3",
#                     "constraints": "1 ≤ n ≤ 10^4",
#                     "tests": [
#                         {"input": "3\n3 1 2", "output": "1 2 3"},
#                         {"input": "1\n5", "output": "5"},
#                         {"input": "4\n9 8 7 6", "output": "6 7 8 9"},
#                         {"input": "3\n-1 0 1", "output": "-1 0 1"}
#                     ]
#                 },

#                 {
#                     "id": "c-ptr-m-3",
#                     "title": "Function Pointer",
#                     "task": (
#                         "Create two functions: add and multiply. "
#                         "Use a function pointer to call the correct function "
#                         "based on user choice (1 for add, 2 for multiply)."
#                     ),
#                     "input_format": "a b choice",
#                     "output_format": "Print result.",
#                     "sample_input": "5 3 1",
#                     "sample_output": "8",
#                     "constraints": "-10^6 ≤ values ≤ 10^6",
#                     "tests": [
#                         {"input": "5 3 1", "output": "8"},
#                         {"input": "5 3 2", "output": "15"},
#                         {"input": "2 4 2", "output": "8"},
#                         {"input": "10 5 1", "output": "15"}
#                     ]
#                 }

#             ]
#         },

#         "Structures": {

#             "Very Easy": [

#                 {
#                     "id": "c-struct-ve-1",
#                     "title": "Basic Structure Print",
#                     "task": (
#                         "Define a structure Student with fields: id (int) and marks (int). "
#                         "Read id and marks and print them."
#                     ),
#                     "input_format": "Two integers: id and marks.",
#                     "output_format": "Print id and marks separated by space.",
#                     "sample_input": "1 90",
#                     "sample_output": "1 90",
#                     "constraints": "0 ≤ marks ≤ 100",
#                     "tests": [
#                         {"input": "1 90", "output": "1 90"},
#                         {"input": "2 75", "output": "2 75"},
#                         {"input": "3 100", "output": "3 100"}
#                     ]
#                 },

#                 {
#                     "id": "c-struct-ve-2",
#                     "title": "Structure with String",
#                     "task": (
#                         "Define a structure Person with name (string) and age (int). "
#                         "Read name and age and print them."
#                     ),
#                     "input_format": "Name and age.",
#                     "output_format": "Print name and age.",
#                     "sample_input": "John 21",
#                     "sample_output": "John 21",
#                     "constraints": "1 ≤ age ≤ 120",
#                     "tests": [
#                         {"input": "John 21", "output": "John 21"},
#                         {"input": "Alice 30", "output": "Alice 30"},
#                         {"input": "Bob 18", "output": "Bob 18"}
#                     ]
#                 },

#                 {
#                     "id": "c-struct-ve-3",
#                     "title": "Array of Structures",
#                     "task": (
#                         "Define structure Product with id and price. "
#                         "Read n products and print their ids."
#                     ),
#                     "input_format": "n followed by n lines: id price.",
#                     "output_format": "Print all ids separated by space.",
#                     "sample_input": "2\n1 100\n2 200",
#                     "sample_output": "1 2",
#                     "constraints": "1 ≤ n ≤ 1000",
#                     "tests": [
#                         {"input": "2\n1 100\n2 200", "output": "1 2"},
#                         {"input": "1\n5 50", "output": "5"},
#                         {"input": "3\n1 10\n2 20\n3 30", "output": "1 2 3"}
#                     ]
#                 },

#                 {
#                     "id": "c-struct-ve-4",
#                     "title": "Sum of Structure Fields",
#                     "task": (
#                         "Define structure Pair with two integers a and b. "
#                         "Read values and print their sum."
#                     ),
#                     "input_format": "Two integers.",
#                     "output_format": "Print sum.",
#                     "sample_input": "5 7",
#                     "sample_output": "12",
#                     "constraints": "-10^9 ≤ values ≤ 10^9",
#                     "tests": [
#                         {"input": "5 7", "output": "12"},
#                         {"input": "-1 1", "output": "0"},
#                         {"input": "10 20", "output": "30"}
#                     ]
#                 },

#                 {
#                     "id": "c-struct-ve-5",
#                     "title": "Structure Initialization",
#                     "task": (
#                         "Initialize a structure Point with x and y. "
#                         "Read x and y and print them."
#                     ),
#                     "input_format": "Two integers x y.",
#                     "output_format": "Print x y.",
#                     "sample_input": "3 4",
#                     "sample_output": "3 4",
#                     "constraints": "-10^6 ≤ values ≤ 10^6",
#                     "tests": [
#                         {"input": "3 4", "output": "3 4"},
#                         {"input": "0 0", "output": "0 0"},
#                         {"input": "-1 5", "output": "-1 5"}
#                     ]
#                 }

#             ],

#             "Easy": [

#                 {
#                     "id": "c-struct-e-1",
#                     "title": "Find Student with Highest Marks",
#                     "task": (
#                         "Define Student structure with name and marks. "
#                         "Read n students and print the name of student "
#                         "with highest marks."
#                     ),
#                     "input_format": "n followed by n lines: name marks.",
#                     "output_format": "Print name.",
#                     "sample_input": "2\nAlice 80\nBob 90",
#                     "sample_output": "Bob",
#                     "constraints": "1 ≤ n ≤ 1000",
#                     "tests": [
#                         {"input": "2\nAlice 80\nBob 90", "output": "Bob"},
#                         {"input": "1\nJohn 50", "output": "John"},
#                         {"input": "3\nA 10\nB 20\nC 15", "output": "B"},
#                         {"input": "2\nX 100\nY 100", "output": "X"}
#                     ]
#                 },

#                 {
#                     "id": "c-struct-e-2",
#                     "title": "Sort Structures by Age",
#                     "task": (
#                         "Define Person structure with name and age. "
#                         "Read n persons and sort them by age in ascending order."
#                     ),
#                     "input_format": "n followed by n lines: name age.",
#                     "output_format": "Print names in sorted order.",
#                     "sample_input": "3\nA 30\nB 20\nC 25",
#                     "sample_output": "B C A",
#                     "constraints": "1 ≤ n ≤ 1000",
#                     "tests": [
#                         {"input": "3\nA 30\nB 20\nC 25", "output": "B C A"},
#                         {"input": "1\nX 10", "output": "X"},
#                         {"input": "2\nP 50\nQ 40", "output": "Q P"}
#                     ]
#                 },

#                 {
#                     "id": "c-struct-e-3",
#                     "title": "Pointer to Structure",
#                     "task": (
#                         "Define structure Item with id and price. "
#                         "Use pointer to structure to print values."
#                     ),
#                     "input_format": "id price.",
#                     "output_format": "Print id and price.",
#                     "sample_input": "5 500",
#                     "sample_output": "5 500",
#                     "constraints": "Valid input.",
#                     "tests": [
#                         {"input": "5 500", "output": "5 500"},
#                         {"input": "1 100", "output": "1 100"},
#                         {"input": "10 999", "output": "10 999"}
#                     ]
#                 },

#                 {
#                     "id": "c-struct-e-4",
#                     "title": "Total Price of Products",
#                     "task": (
#                         "Define Product structure. Read n products with price "
#                         "and compute total price."
#                     ),
#                     "input_format": "n followed by n lines: id price.",
#                     "output_format": "Print total price.",
#                     "sample_input": "2\n1 100\n2 200",
#                     "sample_output": "300",
#                     "constraints": "1 ≤ n ≤ 1000",
#                     "tests": [
#                         {"input": "2\n1 100\n2 200", "output": "300"},
#                         {"input": "1\n5 50", "output": "50"},
#                         {"input": "3\n1 10\n2 20\n3 30", "output": "60"}
#                     ]
#                 }

#             ],

#             "Medium": [

#                 {
#                     "id": "c-struct-m-1",
#                     "title": "Nested Structures",
#                     "task": (
#                         "Define structure Date (day, month, year) and structure Person "
#                         "with name and Date of birth. Read data and print name and year."
#                     ),
#                     "input_format": "name day month year",
#                     "output_format": "Print name and year.",
#                     "sample_input": "John 1 1 2000",
#                     "sample_output": "John 2000",
#                     "constraints": "Valid date values.",
#                     "tests": [
#                         {"input": "John 1 1 2000", "output": "John 2000"},
#                         {"input": "Alice 5 6 1995", "output": "Alice 1995"},
#                         {"input": "Bob 10 12 1980", "output": "Bob 1980"}
#                     ]
#                 },

#                 {
#                     "id": "c-struct-m-2",
#                     "title": "Structure Array Search",
#                     "task": (
#                         "Define Student structure with id and marks. "
#                         "Read n students and search for student with given id."
#                     ),
#                     "input_format": "n, n lines id marks, then search_id.",
#                     "output_format": "Print marks or -1 if not found.",
#                     "sample_input": "2\n1 90\n2 80\n2",
#                     "sample_output": "80",
#                     "constraints": "1 ≤ n ≤ 1000",
#                     "tests": [
#                         {"input": "2\n1 90\n2 80\n2", "output": "80"},
#                         {"input": "1\n5 50\n5", "output": "50"},
#                         {"input": "1\n5 50\n6", "output": "-1"},
#                         {"input": "3\n1 10\n2 20\n3 30\n1", "output": "10"}
#                     ]
#                 },

#                 {
#                     "id": "c-struct-m-3",
#                     "title": "Structure Comparison",
#                     "task": (
#                         "Define structure Rectangle with length and width. "
#                         "Read two rectangles and print the one with larger area."
#                     ),
#                     "input_format": "l1 w1\nl2 w2",
#                     "output_format": "Print area of larger rectangle.",
#                     "sample_input": "2 3\n4 5",
#                     "sample_output": "20",
#                     "constraints": "1 ≤ values ≤ 10^6",
#                     "tests": [
#                         {"input": "2 3\n4 5", "output": "20"},
#                         {"input": "5 5\n3 3", "output": "25"},
#                         {"input": "1 10\n2 5", "output": "10"}
#                     ]
#                 }

#             ]
#         },

#         "Dynamic Memory": {

#             "Very Easy": [

#                 {
#                     "id": "c-dm-ve-1",
#                     "title": "Allocate and Print One Integer",
#                     "task": (
#                         "Write a program that dynamically allocates memory "
#                         "for one integer using malloc, reads a value, prints it, "
#                         "and frees the memory."
#                     ),
#                     "input_format": "Single integer.",
#                     "output_format": "Print integer.",
#                     "sample_input": "5",
#                     "sample_output": "5",
#                     "constraints": "-10^9 ≤ value ≤ 10^9",
#                     "tests": [
#                         {"input": "5", "output": "5"},
#                         {"input": "-10", "output": "-10"},
#                         {"input": "0", "output": "0"}
#                     ]
#                 },

#                 {
#                     "id": "c-dm-ve-2",
#                     "title": "Allocate Array Using malloc",
#                     "task": (
#                         "Read n. Dynamically allocate array of n integers "
#                         "using malloc. Read values and print them."
#                     ),
#                     "input_format": "n followed by n integers.",
#                     "output_format": "Print array elements.",
#                     "sample_input": "3\n1 2 3",
#                     "sample_output": "1 2 3",
#                     "constraints": "1 ≤ n ≤ 10^5",
#                     "tests": [
#                         {"input": "3\n1 2 3", "output": "1 2 3"},
#                         {"input": "1\n5", "output": "5"},
#                         {"input": "4\n9 8 7 6", "output": "9 8 7 6"}
#                     ]
#                 },

#                 {
#                     "id": "c-dm-ve-3",
#                     "title": "Sum Using calloc",
#                     "task": (
#                         "Read n. Allocate memory using calloc for n integers, "
#                         "read values and print their sum."
#                     ),
#                     "input_format": "n followed by n integers.",
#                     "output_format": "Print sum.",
#                     "sample_input": "3\n1 2 3",
#                     "sample_output": "6",
#                     "constraints": "1 ≤ n ≤ 10^5",
#                     "tests": [
#                         {"input": "3\n1 2 3", "output": "6"},
#                         {"input": "1\n5", "output": "5"},
#                         {"input": "4\n-1 1 -2 2", "output": "0"}
#                     ]
#                 }
#         }
#     }
# }       
