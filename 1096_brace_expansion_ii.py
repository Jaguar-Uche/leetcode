class Solution:
    def braceExpansionII(self, expression: str) -> list[str]:
        def parse(i):
            result = set()
            current = {""}

            while i < len(expression) and expression[i] != '}':
                if expression[i] == '{':
                    group, i = parse(i + 1)

                elif expression[i].isalpha():
                    group = {expression[i]}
                    i += 1

                else:
                    # comma
                    result.update(current)
                    current = {""}
                    i += 1
                    continue

                # Concatenation:
                # combine everything currently built
                # with everything from the new group
                current = {
                    a + b
                    for a in current
                    for b in group
                }

            result.update(current)

            # Skip '}'
            if i < len(expression) and expression[i] == '}':
                i += 1

            return result, i

        result, _ = parse(0)

        return sorted(result)