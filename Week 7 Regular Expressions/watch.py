import re


def main():

    # Print the parsed input
    print(parse(input("HTML: ")))

# Define a function that parses the input and returns its shorter, shareable youtu.be
def parse(s):
    if matches := re.search(r"src=\"https?\://(?:www\.)?youtube\.com/embed/(\w+)", s):
        return ("https://youtu.be/" + matches.group(1))


if __name__ == "__main__":
    main()
