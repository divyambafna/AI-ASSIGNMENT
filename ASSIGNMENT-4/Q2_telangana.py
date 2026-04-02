districts = [
"Adilabad","Komaram Bheem","Mancherial","Nirmal","Nizamabad","Kamareddy",
"Karimnagar","Jagitial","Peddapalli","Rajanna Sircilla","Siddipet",
"Medak","Sangareddy","Hyderabad","Medchal","Vikarabad","Rangareddy",
"Mahabubnagar","Narayanpet","Wanaparthy","Nagarkurnool","Jogulamba",
"Nalgonda","Suryapet","Yadadri","Khammam","Bhadradri","Mahabubabad",
"Warangal","Hanumakonda","Mulugu","Jangaon","Jayashankar"
]

colors = ["Red","Green","Blue","Yellow"]

neighbors = {
"Adilabad":["Komaram Bheem","Nirmal"],
"Nirmal":["Adilabad","Nizamabad"],
"Nizamabad":["Nirmal","Kamareddy"],
"Kamareddy":["Nizamabad","Medak"],
"Medak":["Kamareddy","Siddipet","Sangareddy"],
"Siddipet":["Medak","Karimnagar"],
"Karimnagar":["Siddipet","Jagitial","Peddapalli"],
"Jagitial":["Karimnagar"],
"Peddapalli":["Karimnagar","Mancherial"],
"Mancherial":["Peddapalli","Komaram Bheem"],
"Komaram Bheem":["Adilabad","Mancherial"]
}

def is_valid(district, color, solution):
    for neighbor in neighbors.get(district, []):
        if neighbor in solution and solution[neighbor] == color:
            return False
    return True

def solve(solution, districts):
    if len(solution) == len(districts):
        return solution

    district = districts[len(solution)]

    for color in colors:
        if is_valid(district, color, solution):
            solution[district] = color
            result = solve(solution, districts)
            if result:
                return result
            del solution[district]

    return solution

solution = solve({}, districts)

for d in solution:
    print(d, solution[d])