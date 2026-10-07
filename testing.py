def remove_invalid_parentheses(s: str) -> list[str]:
    def is_valid(text: str) -> bool:
        balance = 0

        for char in text:
            if char == '(':
                balance += 1
            elif char == ')':
                balance -= 1

            if balance < 0:
                return False

        return balance == 0

    level = {s}

    while True:
        answers = []

        for text in level:
            if is_valid(text):
                answers.append(text)

        if answers:
            return answers

        next_level = set()

        for text in level:
            for i in range(len(text)):
                if text[i] in '()':
                    candidate = text[:i] + text[i + 1:]
                    next_level.add(candidate)

        level = next_level

print(remove_invalid_parentheses('())()()(()'))
