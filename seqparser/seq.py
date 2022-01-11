# DNA -> RNA Transcription
import re

def transcribe(seq: str) -> str:
    """
    transcribes DNA to RNA by replacing
    all `T` to `U`
    """
    # seq=re.sub('A','U',seq) # example of how to use regex
    # seq=re.sub('T','A',seq)
    transcribe_dict ={'C':'G','G':'C','T':'A','A':'U'}
    seq_list = list(seq)
    for base in range(len(seq_list)):
        seq_list[base] = transcribe_dict[seq_list[base]]
    return "".join(seq_list)

def reverse_transcribe(seq: str) -> str:
    """
    transcribes DNA to RNA by replacing
    all `T` to `U` then reverses the sequence
    """
    return transcribe(seq)[::-1]