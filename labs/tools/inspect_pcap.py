"""Print the instructor-decoded fields without solving the Lab 0 mapping."""
from pathlib import Path
from labs.common.pcap import iter_decoded_packets
ROOT=Path(__file__).resolve().parents[2]
PCAP=ROOT/'labs'/'data'/'canonical_smoke.pcap'
def main():
    for i,p in enumerate(iter_decoded_packets(PCAP)):
        print(i,p)
if __name__=='__main__': main()
