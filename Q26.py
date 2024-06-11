string = input("Enter a string: ")
prefix = input("Enter the prefix to check: ")
suffix = input("Enter the suffix to check: ")

starts_with_prefix = string.startswith(prefix)
ends_with_suffix = string.endswith(suffix)

print(f"The string starts with the prefix '{prefix}': {starts_with_prefix}")
print(f"The string ends with the suffix '{suffix}': {ends_with_suffix}")
