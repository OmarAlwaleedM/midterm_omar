# Question 10 — Check if a URL is valid

def is_valid_url(url):
    """
    Checks if the passed parameter is a valid URL
    :param url: the string to check
    :return: True if valid URL, False otherwise
    """
    # 1. must be a string
    if type(url) != str:
        return False

    # 2. must start with http:// or https://
    if url[:7] != "http://" and url[:8] != "https://":
        return False

    # 3. must not contain spaces
    if " " in url:
        return False

    # 4. get the part after the protocol (e.g. "www.google.com/path")
    if url[:8] == "https://":
        after_protocol = url[8:]
    else:
        after_protocol = url[7:]

    # 5. the part after protocol can't be empty
    if len(after_protocol) == 0:
        return False

    # 6. must have at least one dot (for .com, .org, etc.)
    if "." not in after_protocol:
        return False

    # 7. dot can't be the first or last character of the domain
    if after_protocol[0] == "." or after_protocol[-1] == ".":
        return False

    return True


# --- Testing ---
print(is_valid_url("https://www.google.com"))       # True
print(is_valid_url("http://example.org/page"))       # True
print(is_valid_url("https://gutenberg.org"))         # True
print(is_valid_url("www.google.com"))                # False — no protocol
print(is_valid_url("https://"))                      # False — nothing after protocol
print(is_valid_url("https://hello world.com"))       # False — has a space
print(is_valid_url("just some text"))                # False — not a URL
print(is_valid_url("https://com."))                  # False — dot at the end
print(is_valid_url(12345))                           # False — not a string

# REASONING:
# A valid URL needs a few things:
# - A protocol (http:// or https://) — this is how browsers know it's a web address
# - A domain name after the protocol — can't just be "https://" with nothing
# - At least one dot in the domain — like .com, .org, .net
# - No spaces — URLs never have spaces
# - The dot can't be first or last — ".com" or "google." alone aren't valid domains

# Example output:
# True
# True
# True
# False
# False
# False
# False
# False
# False
