from heapq import heappop, heappush
import re


SPELL_COSTS = {
    "Magic Missile": 53,
    "Drain": 73,
    "Shield": 113,
    "Poison": 173,
    "Recharge": 229,
}


def next_spells(mana, t_s, t_p, t_r):
    spells = list()
    for spell, cost in SPELL_COSTS.items():
        if mana >= cost:
            if spell == "Recharge" and t_r == 1:
                spells.append((spell, cost))
            elif spell == "Poison" and t_p == 1:
                spells.append((spell, cost))
            elif spell == "Shield" and t_s == 1:
                spells.append((spell, cost))
            else:
                spells.append((spell, cost))
    return spells


def turn(spell, HP_w, mana, HP_b, damage, t_s, t_p, t_r, hardmode):
    # WIZARD'S TURN
    if hardmode:
        HP_w -= 1
        if HP_w <= 0:
            return HP_w, mana, HP_b, t_s, t_p, t_r
    mana, HP_b, t_s, t_p, t_r = effects(mana, HP_b, t_s, t_p, t_r)

    match spell:
        case "Magic Missile":
            HP_b -= 4
        case "Drain":
            HP_b -= 2
            HP_w += 2
        case "Shield":
            t_s = 7
        case "Poison":
            t_p = 6
        case "Recharge":
            t_r = 5
    mana -= SPELL_COSTS[spell]

    # BOSS' TURN
    mana, HP_b, t_s, t_p, t_r = effects(mana, HP_b, t_s, t_p, t_r)

    if HP_b <= 0:
        return HP_w, mana, HP_b, t_s, t_p, t_r

    HP_w -= damage - 7 * (t_s > 0)
    return HP_w, mana, HP_b, t_s, t_p, t_r


def effects(mana, HP_b, t_s, t_p, t_r):
    t_s = max(t_s - 1, 0)

    HP_b -= 3 * (t_p > 0)
    t_p = max(t_p - 1, 0)

    mana += 101 * (t_r > 0)
    t_r = max(t_r - 1, 0)
    return mana, HP_b, t_s, t_p, t_r


def min_mana(HP_w, mana, HP_b, damage, t_s, t_p, t_r, hardmode=False):  # Dijkstra
    mana_spent = 0
    state = (mana_spent, HP_w, mana, HP_b, t_s, t_p, t_r)
    turns = [state]
    played = {state}
    while turns:
        mana_spent, HP_w, mana, HP_b, t_s, t_p, t_r = heappop(turns)

        if HP_b <= 0:
            break

        for spell, spell_cost in next_spells(mana, t_s, t_p, t_r):
            next_HP_w, next_mana, next_HP_b, next_t_s, next_t_p, next_t_r = turn(
                spell, HP_w, mana, HP_b, damage, t_s, t_p, t_r, hardmode
            )
            state = (
                mana_spent + spell_cost,
                next_HP_w,
                next_mana,
                next_HP_b,
                next_t_s,
                next_t_p,
                next_t_r,
            )
            if next_HP_w > 0 and (state not in played):
                played.add(state)
                heappush(turns, state)
    return mana_spent


with open("data") as f:
    HP_b, damage = tuple(map(int, re.findall(r"\d+", f.read())))

HP_w, mana = 50, 500
t_s, t_p, t_r = 0, 0, 0

# ==== PART 1 ====
print(min_mana(HP_w, mana, HP_b, damage, t_s, t_p, t_r))

# ==== PART 2 ====
print(min_mana(HP_w, mana, HP_b, damage, t_s, t_p, t_r, hardmode=True))
