class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split('/')
        res = []
        for _ in path:
            if _ == '' or _ == '/' or _ == '.': continue
            elif _ == '..': 
                if res: res.pop(-1)
            else: res += [_]
                
        return '/' + '/'.join(res)