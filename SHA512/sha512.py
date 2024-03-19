# Basic functions
# For a list of inputs: returns the mod 2**w of the sum.
def add(nums: list, w: int) -> int:
    return sum(nums) % 2**w

# For inputs a, b, c: returns the parity of a, b, c.
def xor(a: int, b: int, c: int) -> int:
    return a ^ b ^ c

# Returns x shifted right by n positions.
def shr(x: int, n: int) -> int:
    return x >> n

# Returns x rotated right by n positions. w determines length.
def rotr(x: int, n: int, w: int) -> int:
    return (x >> n) | (x << w - n)

# For inputs a, b, c: the output is the majority of the bits.
#   majority(0, 0, 1) = 0
def majority(a: int, b: int, c: int) -> int:
    return (a & b) | (a & c) | (b & c)

# For inputs a, b, c: a determines whether b or c is selected.
#   choice(0, 0, 1) =  1
def choice(a: int, b: int, c: int) -> int:
    return (~a & c) | (a & b)

# Composite functions
# Σσ functions for 32-word operations
def ls0_32(word: int) -> int:
    return xor(rotr(word, 7, 32), rotr(word, 18, 32), shr(word, 3))

def ls1_32(word: int) -> int:
    return xor(rotr(word, 17, 32), rotr(word, 19, 32), shr(word, 10))

def us0_32(word: int) -> int:
    return xor(rotr(word, 2, 32), rotr(word, 13, 32), rotr(word, 22, 32))

def us1_32(word: int) -> int:
    return xor(rotr(word, 6, 32), rotr(word, 11, 32), rotr(word, 25, 32))

# Σσ functions for 64-word operations
def ls0_64(word: int) -> int:
    return xor(rotr(word, 1, 64), rotr(word, 8, 64), shr(word, 7))

def ls1_64(word: int) -> int:
    return xor(rotr(word, 19, 64), rotr(word, 61, 64), shr(word, 6))

def us0_64(word: int) -> int:
    return xor(rotr(word, 28, 64), rotr(word, 34, 64), rotr(word, 39, 64))

def us1_64(word: int) -> int:
    return xor(rotr(word, 14, 64), rotr(word, 18, 64), rotr(word, 41, 64))

# Processing
# Adds n 0s before a string.
def fill(x: str, n: int) -> str:
    return '0' * (n - len(x)) + x

# Pads the message into 512/1024 length block with the last 64/128 bits reserved for message size.
#   For message m: m + '1' + len(m) where len(pad(m)) == 512n or 1024n.
def pad(x: str, block: int) -> str:
    return x + '1' + '0' * ((block - 1 - len(x) % block) - block//8) + fill(bin(len(x))[2:], block//8)

# Splits m into len(m)/length words.
def split_words(m: str, length: int) -> list:
    words = []
    num_words = len(m)//length
    for n in range(0, num_words):
        words.append(m[n * length : (n + 1) * length])

    return words

# Splits an array of words into a 2-dimensional array of blocks and words
def split_blocks(words: list, size: int) -> list:
    return [words[i : i + size] for i in range(0, len(words), size)]
    
# Encodes a string into UTF-8
def binary_val(string: str) -> str:
    bin_val = ""
    byte_list = bytearray(string, 'utf-8')

    for byte in byte_list:
        b = bin(byte)[2:]
        bin_val += fill(b, len(b) + 8 - (len(b) % 8))
    
    return bin_val

def bitlen(bitstring):
    return len(bitstring) * 8

# Specialized
# Adds the elements of two lists at each respective index
def bilist_sum(a: list, b: list, w: int) -> list:
    c = []
    for i in range(0, max(len(a), len(b))):
        c.append(add([a[i], b[i]], w))
    return c

# Converts a list of integers into a hex string with specific padding
def hex_list(l: list, n: int) -> str:
    s = ""
    for val in l:
        s += fill(hex(val)[2:], n)
    return s

def sha512(message: str) -> str:
    # Declare Constants
    K_BLOCK_LENGTH = 1024
    K_WORD_LENGTH = 64
    K_SCHEDULE_LENGTH = 80

    # Get constants
    k = [4794697086780616226, 8158064640168781261, 13096744586834688815, 16840607885511220156, 4131703408338449720,
         6480981068601479193, 10538285296894168987, 12329834152419229976, 15566598209576043074, 1334009975649890238,
         2608012711638119052, 6128411473006802146, 8268148722764581231, 9286055187155687089, 11230858885718282805,
         13951009754708518548, 16472876342353939154, 17275323862435702243, 1135362057144423861, 2597628984639134821,
         3308224258029322869, 5365058923640841347, 6679025012923562964, 8573033837759648693, 10970295158949994411,
         12119686244451234320, 12683024718118986047, 13788192230050041572, 14330467153632333762, 15395433587784984357,
         489312712824947311, 1452737877330783856, 2861767655752347644, 3322285676063803686, 5560940570517711597,
         5996557281743188959, 7280758554555802590, 8532644243296465576, 9350256976987008742, 10552545826968843579,
         11727347734174303076, 12113106623233404929, 14000437183269869457, 14369950271660146224, 15101387698204529176,
         15463397548674623760, 17586052441742319658, 1182934255886127544, 1847814050463011016, 2177327727835720531,
         2830643537854262169, 3796741975233480872, 4115178125766777443, 5681478168544905931, 6601373596472566643,
         7507060721942968483, 8399075790359081724, 8693463985226723168, 9568029438360202098, 10144078919501101548,
         10430055236837252648, 11840083180663258601, 13761210420658862357, 14299343276471374635, 14566680578165727644,
         15097957966210449927, 16922976911328602910, 17689382322260857208, 500013540394364858, 748580250866718886,
         1242879168328830382, 1977374033974150939, 2944078676154940804, 3659926193048069267, 4368137639120453308,
         4836135668995329356, 5532061633213252278, 6448918945643986474, 6902733635092675308, 7801388544844847127]
    h = [7640891576956012808, 13503953896175478587, 4354685564936845355, 11912009170470909681,
         5840696475078001361, 11170449401992604703, 2270897969802886507, 6620516959819538809]

    # Separte blocks
    blocks = split_blocks([int(word, 2) for word in split_words(pad(binary_val(message), K_BLOCK_LENGTH), K_WORD_LENGTH)], 16)
    print(f"No of blocks: {len(blocks)}")
    block_count = 0
    # For each block compress
    for block in blocks:
        # Expand message schedule
        block_count += 1
        for t in range(len(block), K_SCHEDULE_LENGTH):
            block.append(add([ls1_64(block[t - 2]), block[t - 7], ls0_64(block[t - 15]), block[t - 16]], K_WORD_LENGTH))

        i = h.copy() # Save initial hashes

        # Compress
        for t in range(0, K_SCHEDULE_LENGTH):
            t1 = add([us1_64(h[4]), choice(h[4], h[5], h[6]), h[7], block[t], k[t]], K_WORD_LENGTH)
            t2 = add([us0_64(h[0]), majority(h[0], h[1], h[2])], K_WORD_LENGTH)

            h.pop()
            h = [add([t1, t2], K_WORD_LENGTH)] + h
            h[4] = add([h[4], t1], K_WORD_LENGTH)

            print(f"Round {t}: {' '.join(map(lambda val: fill(hex(val)[2:], 16), h))}")

        # Add initial hash values to compressed hash values
        h = bilist_sum(h, i, K_WORD_LENGTH)
        print(f"\nBlock {block_count}: {' '.join(map(lambda val: fill(hex(val)[2:], 16), h))}\n")
    # Convert list of hashes to hex string
    return hex_list(h, 16)

if __name__ == "__main__":
    msg = input("Enter the String:")
    hash = sha512(msg)
    print(f"Final Hash Value :{hash}")
