# Complete the function below.

def counts(nums, maxes):
    # Initialization of result list, that I will access by index as I calculate the value for each max
    result = [0] * len(maxes)

    # Dictionary mapping maxvalue --> maxindex in the original maxes array, necessary to return results in the correct order
    mdict = {}
    for mindex, melem in enumerate(maxes):
        if melem in mdict:
            mdict[melem].append(mindex)
        else:
            mdict[melem] = [mindex]

    # Sorting both arrays to allow for simple algorithm
    smaxes, snums = sorted(maxes), sorted(nums)
    nindex = 0
    for smindex, smelem in enumerate(smaxes):  # For all sorted maxes..
        mindexes = mdict[smelem]  # retrieve index in original arrays
        while nindex < len(snums) and snums[nindex] <= smelem:  # Go forward in the sorted nums array until all values before nindex are less or equal the current max element
            nindex += 1  # Nindex will be the amount of values in the nums array that are less or equal max element
        for mindex in mindexes:  # Now using the dictionary created at the beginning, I retrieve all the indexes where the max element under investigation was found
            result[
                mindex] = nindex  # and save at each index the amount of values in nums less or equal it, found at the previous step

    return result


assert counts([2,10,5,4,8],[3,1,7,8]) == [1,0,3,4]
assert counts([1,4,2,4],[3,5]) == [2,4]
assert counts([2,3,4],[4,5]) == [3,3]
assert counts([2,3,4,5],[4,5]) == [3,4]
assert counts([2,3,4],[4,5]) == [3,3]
assert counts([2,3,4],[1,2]) == [0,1]
assert counts([7,6,3],[2,1]) == [0,0]
assert counts([7,6,2,3],[2,1]) == [1,0]
assert counts([7,6,2,3],[]) == []
assert counts([7,6,2,3],[3,4,3]) == [2,2,2]
assert counts([7,6,2,3,4],[3,4,3]) == [2,3,2]








