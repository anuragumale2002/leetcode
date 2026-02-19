class Solution:
    def readBinaryWatch(self, turnedOn: int) -> list[str]:
        # Result list to store valid time strings
        res = []
        
        # Iterate through every possible hour (0-11)
        for h in range(12):
            # Iterate through every possible minute (0-59)
            for m in range(60):
                # Count set bits in both hour and minute
                if (bin(h).count('1') + bin(m).count('1')) == turnedOn:
                    # Format: no leading zero for hour, 
                    # two-digit zero-padded for minute
                    res.append(f"{h}:{m:02d}")
                    
        return res