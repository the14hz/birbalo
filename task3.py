def rearrange_by_frequency(nums: list[int]) -> list[int]:
    frequency = {}
    for num in nums:
        frequency[num] = frequency.get(num, 0) + 1

    sorted_items = sorted(frequency.items(), key=lambda x: x[1], reverse=True)

    result = []
    for num, freq in sorted_items:
        result.extend([num] * freq)

    return result


print(rearrange_by_frequency([4, 5, 6, 5, 4, 3, 4]))
# Kutilgan natija: [4, 4, 4, 5, 5, 3, 6]