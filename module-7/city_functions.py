#Colton Kohler
#Module7.2 Assignment
#12/1/2024
def city_country(city, country, population=None, language=None):
    """Return a string in the form City, Country - population xxx, Language."""
    result = f"{city.title()}, {country.title()}"
    if population:
        result += f" - population {population}"
    if language:
        result += f", {language.title()}"
    return result

# Calling the function
print(city_country("sapporo", "japan"))
print(city_country("cape town", "south africa", 4773000))
print(city_country("london", "england", 8866000, "english"))