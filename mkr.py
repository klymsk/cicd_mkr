def readFile(path):
    with open(path, "r") as file:
        data = []
        for line in file:
            country, area, population = line.strip().split(",")
            
            data.append({
                "country": country,
                "area": int(area),
                "population": int(population)
            })
    
    return data

def sortArea(data):
    return sorted(data, key = lambda x: x["area"], reverse = True)

def sortPopulation(data):
    return sorted(data, key = lambda x: x["population"], reverse = True)