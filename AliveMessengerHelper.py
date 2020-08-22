import AliveMessengerUUID

# Merge Multiple bytes into one binary string
# Necessary for e.g. elevation, it uses byte 12-14 to provide correct elevation data
def BitMerge(InputByteString,InputStartByteEndByte):
    BitStrings = ['0b']
    StartByte = InputStartByteEndByte[0]
    EndByte = InputStartByteEndByte[-1]
    while EndByte >= StartByte:
        # Convert from Binary to String
        BitsAsString = str(format(InputByteString[EndByte],'#010b'))
        # Remove 0b from the value
        BitString = BitsAsString.split('0b')
        # Pick the part behind 0b
        BitStrings.append(BitString[1])
        EndByte = EndByte - 1
        # Convert back to Binary(2)
        counter = 0
        MergedBinary = ""
        for n in BitStrings:
            MergedBinary += BitStrings[counter]
            counter = counter + 1
    return(int(MergedBinary,2))

def DateTime(InputByteString,InputTimeDateByteRange):
    result_date_time = BitMerge(InputByteString,InputTimeDateByteRange)
    return result_date_time
