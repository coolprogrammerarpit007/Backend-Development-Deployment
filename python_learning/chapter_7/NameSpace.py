# Namespaces and scope in Python are fundamental concepts that describe the visibility and lifetime of variables and their names in a program. The global and nonlocal keywords are tools to work with variables defined in different scopes.

# Namespaces in Python
# A namespace is a system that maps names (like variable names) to objects. Each namespace is like a container where names are unique and hold references to objects. Python has several namespaces including:

# Built-in Namespace: contains names of built-in functions and exceptions.

# Global Namespace: contains names defined at the top level of a module or script.

# Local Namespace: the namespace for names defined inside a function.

# When a variable name is accessed, Python looks it up in these namespaces starting from the innermost local scope outward to the global and then built-in scopes.

# Scope in Python
# Scope refers to the region in the code where a namespace can be accessed. There are mainly three types of scope:

# Local Scope: Variables created inside a function which cannot be accessed outside it.

# Global Scope: Variables created in the main body of the code, accessible everywhere.

# Enclosing (Nonlocal) Scope: In nested functions, the scope of the outer function which can be accessed by the inner function.

# Local variables are limited to their function, whereas global variables exist throughout the module. Enclosing scopes occur in nested functions, where an inner function can access variables of its outer function.

# Global Keyword
# The global keyword is used inside a function to declare that a variable refers to a global variable (defined outside any function). This allows you to:

# Access a global variable within a function.

# Modify the value of a global variable inside a function.

# Example:

x = 10

def my_function():
    global x
    x = 20
    print(x)  # 20

my_function()
print(x)      # 20


# Here, the global keyword inside my_function makes the x variable refer to the global variable x, so the change persists outside the function.

# Nonlocal Keyword
# The nonlocal keyword is used in nested functions to indicate that a variable refers to a variable in the nearest enclosing scope (outer function), not in the global scope.

# Allows inner functions to modify variables in the outer function.

# Useful for nested functions sharing state.

# Example:

def outer():
    x = 10
    
    def inner():
        nonlocal x
        x = 20
        print(x)  # 20
    
    inner()
    print(x)  # 20

outer()


# Without nonlocal, the assignment inside inner() would create a new local variable x instead of modifying the outer x.

# Summary
# Namespaces map names to objects; different namespaces exist at built-in, global, and local levels.

# Scope defines where a variable name is visible; local, global, and enclosing scopes apply.

# The global keyword lets you modify global variables within functions.

# The nonlocal keyword lets nested functions modify variables from their nearest enclosing function scope.

# These tools combined give Python flexible but understandable rules for variable visibility and lifetime across different code contexts.


