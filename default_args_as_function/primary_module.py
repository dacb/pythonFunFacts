"""
Demonstration of module import w/ function w/ default args as function

Please see the accompanying module_to_be_imported.py for the function
function_to_supply_default_value which supplies the default value
for my_function, below.

"""


def my_function(
        named_parameter_with_default=function_to_supply_default_value()):
    print("hai!")


def main():
    my_function()

if __name__ == "__main__":
    main()
