conversion_factors = {
    "Kilograms": 1,
    "Pounds": 0.45359237,
    "Milligrams": 0.000001,
    "Grams": 0.001,
    "Tonne": 1000,
}


def convert_weight(weight, from_unit, to_unit):

    # Convert the input into kilograms
    weight_in_kg = weight * conversion_factors[from_unit]

    # Convert kilograms into the desired unit
    result = weight_in_kg / conversion_factors[to_unit]

    return result
