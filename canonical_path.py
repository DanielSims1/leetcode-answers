class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        for part in path.split("/"):
            if part == "." or part == "":
                continue
            elif part == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(part)
        return  "/" + "/".join(stack)

if __name__ == "__main__":
    s = Solution()

    path = "/a//b.."
    print(f"absolute  path: {path}")
    print(f"canonical path: {s.simplifyPath(path)}")
