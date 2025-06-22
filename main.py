def fairCandySwap(aliceSizes, bobSizes):
    alice = sum(aliceSizes)
    bob = sum(bobSizes)

    val = (alice - bob) / 2

    for i in bobSizes:
        if i + val in aliceSizes:
            return [int(i+val),int(i)]

aliceSizes = [1,1]
bobSizes = [2,2]
print(fairCandySwap(aliceSizes,bobSizes))