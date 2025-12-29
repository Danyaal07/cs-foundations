Input = ["h","e","l","l","o"]
start = 0
end = len(Input) - 1
while start < end:
    Input[start], Input[end] = Input[end], Input[start]
    start += 1
    end -= 1
print(Input)  # Output: ["o","l","l","e","h"]