def twice_as_old(dad_years_old, son_years_old):
    if not son_years_old == dad_years_old / 2:
        son_years_old += 1
        dad_years_old += 1
    return son_years_old