class Solution:

    """
    Encode a list of strings to a single string repersentation. The encoded string is then
    decoded back to the original list of strings.

    Questions I would ask the interviewer:
        1. Are we looking to compress the list of strings? Should the size of the output string be smaller then the input list.
        2. Do you want me to us the std libraries? In python I could just pickle and un-pickle the object.

    Assuming the answer is yes to #1 and no to #2 then here's my approach. My approach for prod would be to use protobuf and pass binary string.

    The simplist compression would be to grab the frequencies and encode the frequencies and positions in the list.

    We want this to work with ascii chars, but I can try ascii + unicode. 

    The delimiter is important because it need to carry a much information as possiable for the decode funciton in the smallest
    number of bits. 

    What I can do is pass a special ^_l^_ sequence to use to delimt. Let's do it uncompressed first.
    """

    def encode(self, strs: List[str]) -> str:
        return f"{len(strs)}^_"+"^_".join(strs) 


    def decode(self, s: str) -> List[str]:
        decoded = s.split("^_")
        if int(decoded[0]) == 0:
            return []
        return decoded[1:]
