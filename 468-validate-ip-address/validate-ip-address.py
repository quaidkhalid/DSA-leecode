class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        # check for ipv4
        def check_ipv4(ip):
            parts = ip.split('.')
            if len(parts) != 4:
                return False
            for part in parts:
                if not part.isdigit():
                    return False
                if not 0 <= int(part) <= 255:
                    return False
                if part[0] == '0' and len(part) > 1:
                    return False             
            return True
        
        # check for ipv6
        def check_ipv6(ip):
            parts = ip.split(':')
            if len(parts) != 8:
                return False
            for part in parts:
                if len(part) == 0 or len(part) > 4:
                    return False
                for char in part:
                    if not (char.isdigit() or 'a' <= char <= 'f' or 'A' <= char <= 'F'):
                        return False
            return True
        
        if check_ipv4(queryIP):
            return 'IPv4'

        elif check_ipv6(queryIP):
            return 'IPv6'
        else:
            return "Neither"
        