import winsound

# Function to perform Merge Sort with sound effects
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0
        print("Merging left:", L)
        print("Merging right:", R)

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
            # Play sound effect for swap
            winsound.Beep(1000, 100)  # Adjust frequency and duration as needed

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

        print("Merged array:", arr)

def get_input():
    input_str = input("Enter a list of numbers separated by spaces: ")
    user_list = [int(item) for item in input_str.split()]  # Convert each number to an integer
    return user_list

def main():
    user_array = get_input()
    print("Given array is:", user_array)
    merge_sort(user_array)
    print("Sorted array is:", user_array)

if __name__ == "__main__":
    main()