import random
from .app import db
from sqlalchemy.sql import text
import pandas as pd

# Run function to find variants!
def find_variants(name, year):

    cities = db.engine.execute(text("SELECT City, Country FROM CitiesData"))
    cities_db = []
    for c in cities:
        cities_db.append(c)
    #print(cities_db)
  
    jobs = db.engine.execute(text("SELECT Job FROM Jobs"))
    jobs_db = []
    for j in jobs:
        jobs_db.append(j)
    #print(jobs_db)
  
   
    cities_data = pd.DataFrame(cities_db, columns=['City', 'Country'])
    jobs_data = pd.DataFrame(jobs_db, columns=['Job'])
    # print(cities_data)
    # print(jobs_data)

    #Create a list of cities and pick 3 random
    cities_data['Location'] = cities_data['City'].str.cat(cities_data['Country'], sep =", ")
    cities_list = cities_data['Location'].values.tolist()
    random_cities = random.choices(cities_list, k=3)
    print(random_cities)

    #Create a list of jobs and pick 3 random
    job_list = jobs_data['Job'].values.tolist()
    random_jobs = random.choices(job_list, k=3)
    print(random_jobs)

    #Create 3 four digit codes
    #four_digits = random.randint(1000,9999-1,3)
    four_digits = []
    for i in range(0,3):
        n = random.randint(1000,9999)
        four_digits.append(n)
    print(four_digits)
    
    # Generate a list of years off their birth year and pick 3 random
    if year is None:
        year = "1940"

    year_list = list(range(int(year), 2021))
    random_years = random.choices(year_list, k=3)
    
    # Find first letter of name
    if name is None:
        name = "Loki"

    first_letter = name[0].upper()
    name = name.upper()

    # Create dictionary of results
    v_data = {
        "one": f"<br>{name} VAR # {first_letter}{four_digits[0]} <br> <h6>{random_jobs[0]} in {random_cities[0]} in {random_years[0]}</h6>",
        "two": f"{name} VAR # {first_letter}{four_digits[1]} <br> <h6>{random_jobs[1]} in {random_cities[1]} in {random_years[1]}</h6>",
        "three": f"{name} VAR # {first_letter}{four_digits[2]} <br> <h6>{random_jobs[2]} in {random_cities[2]} in {random_years[2]}</h6><br>",
    }


    return v_data
