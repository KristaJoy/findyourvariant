
import random
from .app import db

def find_variants(name, year):

    cities_data = db.session.query('SELECT * FROM CitiesData')
    jobs_data = db.session.query('SELECT * FROM Jobs')
    
    #Create a list of cities and pick 3 random
    cities_data['Location'] = cities_data['City'].str.cat(cities_data['Country'], sep =", ")
    cities_list = cities_data['Location'].values.tolist()
    random_cities = random.choices(cities_list, k=3)

    #Create a list of jobs and pick 3 random
    job_list = jobs_data['Job'].values.tolist()
    random_jobs = random.choices(job_list, k=3)

    #Create 3 four digit codes
    four_digits = random.randint(1000,9999,3)
    
    # Generate a list of years off their birth year and pick 3 random
    year_list = list(range(int(year) + 17, 2021))
    random_years = random.choices(year_list, k=3)

    # Find first letter of name
    first_letter = name[0].upper()
    name = name.upper()

    # Create dictionary of data
    # data = {
    #     "name": name,
    #     "jobs": random_jobs,
    #     "cities": random_cities,
    #     "year": random_years,
    #     "initial": first_letter,
    #     "numbers": four_digits
    #     }
    v_data = {
        "one": f"<p>{name} VAR # {first_letter}{four_digits[0]}<br>{random_jobs[0]} in {random_cities[0]} in {random_years[0]}</p>",
        "two": f"<p>{name} VAR # {first_letter}{four_digits[1]}<br>{random_jobs[1]} in {random_cities[1]} in {random_years[1]}</p>",
        "three": f"<p>{name} VAR # {first_letter}{four_digits[2]}<br>{random_jobs[2]} in {random_cities[2]} in {random_years[2]}</p>",
    }


    return v_data
