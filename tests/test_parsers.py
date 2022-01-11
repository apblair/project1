# write tests for parsers
import hashlib

from seqparser import (
        FastaParser,
        FastqParser)


def test_freebie_parser_1():
    """
    This one is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert True


def test_freebie_parser_2():
    """
    This too is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert 1 != 2

def test_FastaParser():
    """
    Write your unit test for your FastaParser
    class here. You should generate an instance of
    your FastaParser class and assert that it properly
    reads in the example Fasta File.
    """
    fasta_file = './data/test.fa'
    fasta_rec = FastaParser(fasta_file)
    
    fasta_rec_length = 2
    for fasta_tuple in fasta_rec:
        assert type(fasta_tuple) is tuple,  "fail: fasta record is not a tuple."
        assert len(fasta_tuple) == fasta_rec_length, "fail: fasta record does not contain a tuple of length 2."
    
    unit_test_file = "./tests/unit_test.fa"
    with open(unit_test_file,"w") as unit_test_fa:
        for header,seq in fasta_rec:
            unit_test_fa.write(header+'\n'+seq+'\n')
    unit_test_fa.close()
    unit_test_m5 = hashlib.md5(open(unit_test_file,'rb').read()).hexdigest()
    og_m5 = hashlib.md5(open(fasta_file,'rb').read()).hexdigest()
    assert unit_test_m5 == og_m5

def test_FastqParser():
    """
    Write your unit test for your FastqParser
    class here. You should generate an instance of
    your FastqParser class and assert that it properly
    reads in the example Fastq File.
    """
    fastq_file = './data/test.fq'
    fastq_rec = FastqParser(fastq_file)

    fastq_rec_length = 3
    for fastq_tuple in fastq_rec:
        assert type(fastq_tuple) is tuple, "fail: fastq record is not a tuple."
        assert len(fastq_tuple) == fastq_rec_length, "fail: fastq record does not contain a tuple of length 3."

    unit_test_file = "./tests/unit_test.fq"
    with open(unit_test_file,"w") as unit_test_fq:
        for header,seq,qual in fastq_rec:
            unit_test_fq.write(header+seq+qual)
    unit_test_fq.close()
    unit_test_m5 = hashlib.md5(open(unit_test_file,'rb').read()).hexdigest()
    og_m5 = hashlib.md5(open(fastq_file,'rb').read()).hexdigest()
    assert unit_test_m5 == og_m5

test_FastaParser()
test_FastqParser()