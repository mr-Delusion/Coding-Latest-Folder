def myfunction(n):
    print("Running the function...\n")
    
    # First Loop: O(n)
    print("First Loop:")
    for i in range(0, n + 1):
        print("First Loop")

    # Second Loop: O(log n)
    print("\nSecond Loop:")
    j = 1
    while j <= n + 1:
        print("Second Loop", j)
        j = j * 2

    # Third Loop: O(1)
    print("\nThird Loop:")
    for i in range(0, 100):
        print("Third Loop")

    # Print Time Complexities
    print("\nTime Complexities:")
    print("First Loop: O(n)")
    print("Second Loop: O(log n)")
    print("Third Loop: O(1)")
    print("Total Time Complexity: O(n)")  # Dominant term

# Example usage
myfunction(10)
