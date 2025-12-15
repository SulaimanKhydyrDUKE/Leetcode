#from my assessment at eBay
def count_state_changes(arr):
    if not arr:
        return 0

    changes = 0
    for i in range(1, len(arr)):
        if arr[i].upper() != arr[i - 1].upper():
            changes += 1

    return changes
