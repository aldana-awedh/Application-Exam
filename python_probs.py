# Added colon after function name 
def brew_coffee(cups):
    return cups * 12

# Used == instead of =
def calculate_total(price, tip_percentage):
    if tip_percentage == 0:
        return price
    else:
        return price + (price * tip_percentage / 100)

# Added indentation for line of code within if statement 
# For if statement, changed comparison to ['caffeine'] > strongest_coffee['caffeine'] instad of ['caffeine'] > strongest_coffee
# to compare caffeine content
def find_strongest_coffee(coffees):
    strongest_coffee = coffees[0]
    for coffee in coffees:
        if coffee['caffeine'] > strongest_coffee['caffeine']:
            strongest_coffee = coffee
    return strongest_coffee

# Repaced () with [] when indexing 
def merge_coffee_orders(order1, order2):
    merged_orders = []
    i = j = 0
    while i < len(order1) and j < len(order2):
        if order1[i]['price'] < order2[j]['price']:
            merged_orders.append(order1[i])
            i += 1
        elif order1[i]['price'] == order2[j]['price']:
            merged_orders.append(order1[i])
            merged_orders.append(order2[j])
            i += 1
            j += 1
        else:
            merged_orders.append(order2[j])
            j += 1
    merged_orders += order1[i:]
    merged_orders += order2[j:]

    return merged_orders

# Remove first elif statement because keeping "and" does not make sense since bean1 cannot be both bigger and smaller than bean 2
# and changing to "or" leads to getting stuck in the while loop when bean1 + bean2 != 100 
def perfect_coffee_blend(beans1, beans2):
    total_weight = 0
    while total_weight != 100:
        if beans1 + beans2 == 100:
            total_weight = beans1 + beans2
        elif beans1 + beans2 < 50 or beans1 + beans2 > 150:
            return "Blend out of range!"
        else:
            total_weight = beans1 - beans2

    return "Perfect blend achieved!"
