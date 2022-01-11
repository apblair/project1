# DNA -> RNA Transcription
import re

def transcribe(seq: str) -> str:
    """
    transcribes DNA to RNA by replacing
    all `T` to `U`
    """
    seq=re.sub('A','U',seq)
    seq=re.sub('T','A',seq)
    seq=re.sub('G','C',seq)
    seq=re.sub('C','G',seq)
    return seq

def reverse_transcribe(seq: str) -> str:
    """
    transcribes DNA to RNA by replacing
    all `T` to `U` then reverses the sequence
    """
    return transcribe(seq)[::-1]