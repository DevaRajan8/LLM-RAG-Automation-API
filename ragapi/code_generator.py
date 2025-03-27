def generate_code(function_name):
    """
    Generates a structured Python script that imports and executes the given function.
    """
    code = f"""from automation_functions import {function_name}

def main():
    try:
        # Execute the function and capture any result if returned
        result = {function_name}()
        print("{function_name} executed successfully.")
        if result is not None:
            print("Result:", result)
    except Exception as e:
        print(f"Error executing function: {{e}}")

if __name__ == "__main__":
    main()
"""
    return code
