def find_majority_elements(nums):
    if not nums:
        return []

    # Initialize candidate elements and their counts
    candidate1, candidate2 = None, None
    count1, count2 = 0, 0

    # Phase 1: Find the two most frequent elements
    for num in nums:
        if num == candidate1:
            count1 += 1
        elif num == candidate2:
            count2 += 1
        elif count1 == 0:
            candidate1, count1 = num, 1
        elif count2 == 0:
            candidate2, count2 = num, 1
        else:
            count1 -= 1
            count2 -= 1

    # Phase 2: Count the occurrences of the two candidates
    count1, count2 = 0, 0
    for num in nums:
        if num == candidate1:
            count1 += 1
        elif num == candidate2:
            count2 += 1

    n = len(nums)
    result = []

    # Check if candidates appear more than n/3 times
    if count1 > n // 3:
        result.append(candidate1)
    if count2 > n // 3:
        result.append(candidate2)

    return result

# Example usage:
nums = [3, 2, 3]
result = find_majority_elements(nums)
print(result)  # Output: [3]
