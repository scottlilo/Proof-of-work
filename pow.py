import hashlib
import time

max_nonce  =2 ** 28 # 4 billion

def proof_of_work(header, difficulty_bits):

    target = 2 ** (256-difficulty_bits)

    for nonce in xrange(max_nonce):
        hash_result = hashlib.sha256(str(header)+str(nonce)).hexdigest()
        print hash_result
        if long(hash_result, 16) < target:
            print "\n \n Success with nonce %d" % nonce
            print "Hash is %s \n \n " % hash_result
            time.sleep(5)
            return (hash_result,nonce)

    print "Failed after %d (max_nonce) tries" % nonce
    return nonce


if __name__ == '__main__':

    nonce = 0
    hash_result = ''

    for difficulty_bits in xrange(32):

        difficulty = 2 ** difficulty_bits
        print "\n \n Difficulty: %ld (%d bits)" % (difficulty, difficulty_bits)
        time.sleep(5)
        print "Starting search... \n \n "
        start_time = time.time()
        new_block = 'test block with transactions' + hash_result
        (hash_result, nonce) = proof_of_work(new_block, difficulty_bits)
        end_time = time.time()
        elapsed_time = end_time - start_time
        print "Elapsed Time: %.4f seconds" % elapsed_time

        if elapsed_time > 0:
            hash_power = float(long(nonce)/elapsed_time)
            print "\n \n Hashing Power: %ld hashes per second \n \n " % hash_power