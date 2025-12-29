def is_palindrome(Input):
    Input = Input.lower()
    left = 0
    right = len(Input) - 1
    while left <= right:
        if Input[left] == Input[right] and Input[left].isalnum() and Input[right].isalnum():
            left += 1
            right -= 1
        elif not Input[left].isalnum():
            left += 1
        elif not Input[right].isalnum():
            right -= 1
        else:
            return False
    return True


print(is_palindrome("A man, a plan, a canal: Panama"))  # True
print(is_palindrome("race a car"))                        # False
print(is_palindrome(""))                                  # True
print(is_palindrome(".,!"))                               # True