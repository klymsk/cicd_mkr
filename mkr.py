import os

print("Поточна робоча директорія:", os.getcwd())

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

if __name__ == "__main__":
    dataTxt = readFile("data.txt")

    areaTxt = sortArea(dataTxt)
    for country in areaTxt:
        print(f'{country["country"]}: {country["area"]}')

    populationTxt = sortPopulation(dataTxt)
    for country in populationTxt:
        print(f'{country["country"]}: {country["population"]}')