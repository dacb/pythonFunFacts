"""
Demonstration of module import w/ function w/ default args as function

Please see the accompanying module_to_be_imported.py for the function
function_to_supply_default_value which supplies the default value
for my_function, below.

"""

from module_to_be_imported import function_to_supply_default_value as default


def my_function(named_parameter_with_default=default()):
    print("default parameter value is %d" % named_parameter_with_default)


def main():
    my_function()


if __name__ == "__main__":
    main()
