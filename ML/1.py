def quests_is_ok(quest, quests, passed):
    if quests[quest] == -1:
        return False

    if quest in passed:
        return True

    passed.add(quest)
    return quests_is_ok(quests[quest], quests, passed)



n = int(input())
quests = [0] + [int(i) for i in input().split()]

for quest in range(1, n + 1):
    passed = set()
    impossible = quests_is_ok(quest, quests, passed)
    if impossible:
        break

print("No" if impossible else "Yes")