from num2words import num2words

# ZERO = ("zero",)

# ONES = {
#     1: ("jeden",),
#     2: ("dwa",),
#     3: ("trzy",),
#     4: ("cztery",),
#     5: ("pięć",),
#     6: ("sześć",),
#     7: ("siedem",),
#     8: ("osiem",),
#     9: ("dziewięć",),
# }

# TENS = {
#     0: ("dziesięć",),
#     1: ("jedenaście",),
#     2: ("dwanaście",),
#     3: ("trzynaście",),
#     4: ("czternaście",),
#     5: ("piętnaście",),
#     6: ("szesnaście",),
#     7: ("siedemnaście",),
#     8: ("osiemnaście",),
#     9: ("dziewiętnaście",),
# }

# TWENTIES = {
#     2: ("dwadzieścia",),
#     3: ("trzydzieści",),
#     4: ("czterdzieści",),
#     5: ("pięćdziesiąt",),
#     6: ("sześćdziesiąt",),
#     7: ("siedemdziesiąt",),
#     8: ("osiemdziesiąt",),
#     9: ("dziewięćdziesiąt",),
# }

# HUNDREDS = {
#     1: ("sto",),
#     2: ("dwieście",),
#     3: ("trzysta",),
#     4: ("czterysta",),
#     5: ("pięćset",),
#     6: ("sześćset",),
#     7: ("siedemset",),
#     8: ("osiemset",),
#     9: ("dziewięćset",),
# }

# THOUSANDS = {
#     1: ("tysiąc", "tysiące", "tysięcy"),  # 10^3
#     2: ("milion", "miliony", "milionów"),  # 10^6
# }


def number_to_words(n, lang="pl"):
    if type(n) != int or (type(n) == int and n < 0):
        raise Exception("Argument n must be positive integer number.")
    return num2words(n, lang=lang)
    # elif n >= 1000000000:
    #     raise NotImplementedError("Argument n must be less than 10^9.")
    # elif n == 0:
    #     return ZERO[0]

#     words = []
#     splitted = split_number_by_three_digits(n)  # 2985311 -> [2, 985, 311]
#     i = len(splitted)
#     for x in splitted:
#         i -= 1

#         if x == 0:
#             continue

#         units, tens, hundreds = extract_digits(x)



#         if hundreds > 0:
#             words.append(HUNDREDS[hundreds][0])

#         if tens > 1:
#             words.append(TWENTIES[tens][0])

#         if tens == 1:
#             words.append(TENS[units][0])
#         elif units > 0 and not (i > 0 and x == 1):
#             words.append(ONES[units][0])

#         if i > 0:
#             words.append(pluralize(x, THOUSANDS[i]))

#     return " ".join(words)


# def pluralize(n, forms):
#     if type(n) != int or (type(n) == int and n < 0):
#         raise Exception("Argument n must be positive integer number.")
#     if type(forms) != tuple and len(forms) != 3:
#         raise Exception(
#             "Argument forms must be tuple with three forms of plural text."
#         )

#     if n == 1:
#         form = 0
#     elif 5 > n % 10 > 1 and (n % 100 < 10 or n % 100 > 20):
#         form = 1
#     else:
#         form = 2
#     return forms[form]


# def split_number_by_three_digits(n):
#     if type(n) != int or (type(n) == int and n < 0):
#         raise Exception("Argument n must be positive integer number.")
#     n = str(n)
#     x = 3
#     length = len(n)
#     splitted = []
#     if length > x:
#         start = length % x
#         if start > 0:
#             result = n[:start]
#             splitted.append(int(result))
#         for i in range(start, length, x):
#             next_i = i + x
#             result = n[i:next_i]
#             splitted.append(int(result))
#     else:
#         splitted.append(int(n))
#     return splitted


# def extract_digits(n):
#     if type(n) != int or (type(n) == int and n < 0):
#         raise Exception("Argument n must be positive integer number.")
#     elif n >= 1000:
#         raise Exception("Argument n must be less than 1000.")
#     return [int(x) for x in reversed(list(f"{n:03}"))]
