def declare_winner(fighter1, fighter2, first_attacker):
    fighter1_health = fighter1[1]
    fighter1_damage = fighter1[2]
    fighter2_health = fighter2[1]
    fighter2_damage = fighter2[2]
    while fighter1_health and fighter2_health > 0:
        if first_attacker == "lew":
            fighter2_health -= fighter1_damage
            if fighter2_health > 0:
                fighter1_health -= fighter2_damage


declare_winner(Fighter("Lew", 10, 2),Fighter("Harry", 5, 4), "Lew"), "Lew")