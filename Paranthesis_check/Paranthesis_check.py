
def paranthesis_check(str):
    stack = []
    for i in str:
        if i == "(" or i == "[" or i == "{":
            stack.append(i)
        else:
            if not stack:
                return False
            
            tmp = stack.pop()
            if tmp == ")":
                if i != "(":
                    return False
            if tmp == "]" and i != "[":
                return False
            if tmp == "}" and i != "{":
                return False
            
            if tmp == "(":
                if i != ")":
                    return False
            if tmp == "[" and i != "]":
                return False
            if tmp == "{" and i != "}":
                return False
            
    if stack:
        return False
    return True


str1 = "(){}[]"
print(paranthesis_check(str1))

str1="{{([])}}"
print(paranthesis_check(str1))

str1 = "[]{)(}"
print(paranthesis_check(str1))

str1 = "[({)}]"
print(paranthesis_check(str1))

str1 = "[({})]"
print(paranthesis_check(str1))

            
