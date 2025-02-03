CITY_COUNTRY_PAIRS = [("New York", "USA"), ("Los Angeles", "USA"), ("Chicago", "USA"), ("Houston", "USA"), ("Phoenix", "USA"), ("Philadelphia", "USA"), ("San Antonio", "USA"), ("San Diego", "USA"), ("Dallas", "USA"), ("San Jose", "USA"), ("Austin", "USA"), ("Jacksonville", "USA"), ("Fort Worth", "USA"), ("Columbus", "USA"), ("San Francisco", "USA"), ("Indianapolis", "USA"), ("Seattle", "USA"), ("Denver", "USA"), ("Washington D.C.", "USA"), ("Boston", "USA"), ("El Paso", "USA"), ("Nashville", "USA"), ("Detroit", "USA"), ("Oklahoma City", "USA"), ("Portland", "USA"), ("Las Vegas", "USA"), ("Memphis", "USA"), ("Louisville", "USA"), ("Baltimore", "USA"), ("Milwaukee", "USA"), ("Albuquerque", "USA"), ("Tucson", "USA"), ("Fresno", "USA"), ("Sacramento", "USA"), ("Kansas City", "USA"), ("Atlanta", "USA"), ("Miami", "USA"), ("Tampa", "USA"), ("New Orleans", "USA"), ("Orlando", "USA"), ("Charlotte", "USA"), ("Richmond", "USA"), ("Birmingham", "United Kingdom"), ("London", "United Kingdom"), ("Manchester", "United Kingdom"), ("Glasgow", "United Kingdom"), ("Liverpool", "United Kingdom"), ("Edinburgh", "United Kingdom"), ("Bristol", "United Kingdom"), ("Leeds", "United Kingdom"), ("Sheffield", "United Kingdom"), ("Nottingham", "United Kingdom"), ("Belfast", "United Kingdom"), ("Cardiff", "United Kingdom"), ("Berlin", "Germany"), ("Munich", "Germany"), ("Hamburg", "Germany"), ("Cologne", "Germany"), ("Frankfurt", "Germany"), ("Stuttgart", "Germany"), ("Düsseldorf", "Germany"), ("Leipzig", "Germany"), ("Dresden", "Germany"), ("Hannover", "Germany"), ("Nuremberg", "Germany"), ("Dortmund", "Germany"), ("Essen", "Germany"), ("Bremen", "Germany"), ("Duisburg", "Germany"), ("Paris", "France"), ("Lyon", "France"), ("Marseille", "France"), ("Toulouse", "France"), ("Nice", "France"), ("Nantes", "France"), ("Strasbourg", "France"), ("Montpellier", "France"), ("Bordeaux", "France"), ("Lille", "France"), ("Rennes", "France"), ("Reims", "France"), ("Le Havre", "France"), ("Saint-Étienne", "France"), ("Toulon", "France"), ("Tokyo", "Japan"), ("Osaka", "Japan"), ("Kyoto", "Japan"), ("Yokohama", "Japan"), ("Nagoya", "Japan"), ("Sapporo", "Japan"), ("Kobe", "Japan"), ("Fukuoka", "Japan"), ("Hiroshima", "Japan"), ("Sendai", "Japan"), ("Kawasaki", "Japan"), ("Saitama", "Japan"), ("Kumamoto", "Japan"), ("Shizuoka", "Japan"), ("Okayama", "Japan"), ("Sydney", "Australia"), ("Melbourne", "Australia"), ("Brisbane", "Australia"), ("Perth", "Australia"), ("Adelaide", "Australia"), ("Gold Coast", "Australia"), ("Canberra", "Australia"), ("Hobart", "Australia"), ("Darwin", "Australia"), ("Newcastle", "Australia"), ("Wollongong", "Australia"), ("Geelong", "Australia"), ("Cairns", "Australia"), ("Townsville", "Australia"), ("Toronto", "Canada"), ("Vancouver", "Canada"), ("Montreal", "Canada"), ("Calgary", "Canada"), ("Edmonton", "Canada"), ("Ottawa", "Canada"), ("Winnipeg", "Canada"), ("Quebec City", "Canada"), ("Hamilton", "Canada"), ("Kitchener", "Canada"), ("Halifax", "Canada"), ("Victoria", "Canada"), ("Saskatoon", "Canada"), ("Regina", "Canada"), ("Dubai", "United Arab Emirates"), ("Abu Dhabi", "United Arab Emirates"), ("Sharjah", "United Arab Emirates"), ("Ajman", "United Arab Emirates"), ("Fujairah", "United Arab Emirates"), ("Ras Al Khaimah", "United Arab Emirates"), ("Al Ain", "United Arab Emirates"), ("Rome", "Italy"), ("Milan", "Italy"), ("Naples", "Italy"), ("Turin", "Italy"), ("Palermo", "Italy"), ("Genoa", "Italy"), ("Bologna", "Italy"), ("Florence", "Italy"), ("Venice", "Italy"), ("Verona", "Italy"), ("Catania", "Italy"), ("Bari", "Italy"), ("Messina", "Italy"), ("Padua", "Italy"), ("Trieste", "Italy"), ("Moscow", "Russia"), ("Saint Petersburg", "Russia"), ("Novosibirsk", "Russia"), ("Yekaterinburg", "Russia"), ("Nizhny Novgorod", "Russia"), ("Kazan", "Russia"), ("Chelyabinsk", "Russia"), ("Omsk", "Russia"), ("Samara", "Russia"), ("Rostov-on-Don", "Russia"), ("Ufa", "Russia"), ("Krasnoyarsk", "Russia"), ("Perm", "Russia"), ("Volgograd", "Russia"), ("Voronezh", "Russia"), ("Bangkok", "Thailand"), ("Chiang Mai", "Thailand"), ("Pattaya", "Thailand"), ("Phuket", "Thailand"), ("Hat Yai", "Thailand"), ("Udon Thani", "Thailand"), ("Nakhon Ratchasima", "Thailand"), ("Singapore", "Singapore"), ("Beijing", "China"), ("Shanghai", "China"), ("Guangzhou", "China"), ("Shenzhen", "China"), ("Chengdu", "China"), ("Nanjing", "China"), ("Wuhan", "China"), ("Chongqing", "China"), ("Tianjin", "China"), ("Hangzhou", "China"), ("Xi'an", "China"), ("Mumbai", "India"), ("Delhi", "India"), ("Bangalore", "India"), ("Hyderabad", "India"), ("Chennai", "India"), ("Kolkata", "India"), ("Pune", "India"), ("Ahmedabad", "India"), ("Jaipur", "India"), ("Surat", "India"), ("Lucknow", "India"), ("Kanpur", "India"), ("Nagpur", "India"), ("Indore", "India"), ("Thane", "India")]


import random
from faker import Faker
from datetime import date, timedelta

# Initialize Faker
fake = Faker()

# Helper Functions
def random_date(start_year=1950, end_year=2005):
    """Generate a random date between start_year and end_year."""
    start = date(start_year, 1, 1)
    end = date(end_year, 12, 31)
    random_days = random.randint(0, (end - start).days)
    return start + timedelta(days=random_days)

def calculate_bmi(height, weight):
    """Calculate BMI from height (m) and weight (kg)."""
    return round(weight / (height ** 2), 2)

def clean_phone_number(phone_number):
    """Remove all non-numeric characters from the phone number and standardize it."""
    # Remove all non-numeric characters
    cleaned = ''.join(filter(str.isdigit, phone_number))
    # Optionally, add a '+' at the beginning for international format
    return f"+{cleaned}" if cleaned else ""

def get_gender_specific_name(gender):
    """Generate a name based on gender."""
    if gender == 'Male':
        return fake.name_male()
    elif gender == 'Female':
        return fake.name_female()
    else:
        return fake.name_nonbinary()  # For 'Non-binary' or 'Prefer not to say'

def generate_email(name):
    """Generate an email address based on the name."""
    # Split the name into first and last names
    parts = name.split()
    first_name = parts[0].lower()
    last_name = parts[-1].lower() if len(parts) > 1 else ""
    domain = random.choice(['gmail.com', 'yahoo.com', 'outlook.com', 'hotmail.com'])

    # Create email in the format: firstname.lastname@domain.com
    if last_name:
        return f"{first_name}.{last_name}@{domain}"
    else:
        return f"{first_name}@{domain}"

def get_education_level(age):
    """Assign education level based on age."""
    if age < 18:
        return 'High School'
    elif 18 <= age < 25:
        return random.choice(['High School', "Bachelor"])
    elif 25 <= age < 30:
        return random.choice(["Bachelor", "Master"])
    else:
        return random.choice(["Bachelor", "Master", 'PhD'])

def get_employment_status(age):
    """Assign employment status based on age."""
    if age < 18:
        return 'Student'
    elif 18 <= age < 60:
        return random.choice(['Employed', 'Self-employed', 'Unemployed'])
    else:
        return 'Retired'

def get_num_children(marital_status):
    """Assign number of children based on marital status."""
    if marital_status in ['Married', 'Divorced', 'Widowed']:
        # Higher chance (70%) of having children
        return random.randint(0, 5) if random.random() < 0.7 else 0
    else:
        # Lower chance (10%) of having children
        return random.randint(0, 5) if random.random() < 0.1 else 0

def generate_country_specific_phone_number(country):
    """Generate a phone number based on the country."""
    if country == "United States":
        return "+1" + "".join([str(random.randint(0, 9)) for _ in range(10)])  # USA format: +1XXXXXXXXXX
    elif country == "United Kingdom":
        return "+44" + "".join([str(random.randint(0, 9)) for _ in range(10)])  # UK format: +44XXXXXXXXXX
    elif country == "Germany":
        return "+49" + "".join([str(random.randint(0, 9)) for _ in range(10)])  # Germany format: +49XXXXXXXXXX
    elif country == "France":
        return "+33" + "".join([str(random.randint(0, 9)) for _ in range(9)])  # France format: +33XXXXXXXXX
    elif country == "Japan":
        return "+81" + "".join([str(random.randint(0, 9)) for _ in range(10)])  # Japan format: +81XXXXXXXXXX
    elif country == "Australia":
        return "+61" + "".join([str(random.randint(0, 9)) for _ in range(9)])  # Australia format: +61XXXXXXXXX
    elif country == "Canada":
        return "+1" + "".join([str(random.randint(0, 9)) for _ in range(10)])  # Canada format: +1XXXXXXXXXX
    elif country == "United Arab Emirates":
        return "+971" + "".join([str(random.randint(0, 9)) for _ in range(9)])  # UAE format: +971XXXXXXXXX
    elif country == "Italy":
        return "+39" + "".join([str(random.randint(0, 9)) for _ in range(10)])  # Italy format: +39XXXXXXXXXX
    elif country == "Russia":
        return "+7" + "".join([str(random.randint(0, 9)) for _ in range(10)])  # Russia format: +7XXXXXXXXXX
    elif country == "Thailand":
        return "+66" + "".join([str(random.randint(0, 9)) for _ in range(9)])  # Thailand format: +66XXXXXXXXX
    elif country == "Singapore":
        return "+65" + "".join([str(random.randint(0, 9)) for _ in range(8)])  # Singapore format: +65XXXXXXX
    elif country == "China":
        return "+86" + "".join([str(random.randint(0, 9)) for _ in range(11)])  # China format: +86XXXXXXXXXXX
    elif country == "India":
        return "+91" + "".join([str(random.randint(0, 9)) for _ in range(10)])  # India format: +91XXXXXXXXXX
    else:
        return "+" + "".join([str(random.randint(0, 9)) for _ in range(12)])  # Default format: +XXXXXXXXXXXX

# Lists for ENUM fields
GENDERS = ['Male', 'Female', 'Non-binary', 'Prefer not to say']
GENDER_WEIGHTS = [35, 35, 15, 15]  # Probabilities for Male, Female, Non-binary, Prefer not to say
MARITAL_STATUSES = ['Single', 'Married', 'Divorced', 'Widowed']
EMPLOYMENT_STATUSES = ['Employed', 'Self-employed', 'Unemployed', 'Retired', 'Student']
HEALTH_STATUSES = ['Excellent', 'Good', 'Fair', 'Poor']
BLOOD_GROUPS = ['A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-']
ALCOHOL_CONSUMPTION = ['Never', 'Rarely', 'Occasionally', 'Often']

# Generate 1000 rows of clean data
data = []
for i in range(1, 10001):  # Change to 1000 for full dataset
    # Assign gender based on weighted probabilities
    gender = random.choices(GENDERS, weights=GENDER_WEIGHTS)[0]
    name = get_gender_specific_name(gender)  # Ensure name matches gender

    # Generate consistent city and country using predefined pairs
    city, country = random.choice(CITY_COUNTRY_PAIRS)

    dob = random_date(1950, 2005)
    age = date.today().year - dob.year
    income = round(random.uniform(30000, 150000), 2)
    marital_status = random.choice(MARITAL_STATUSES)
    employment_status = get_employment_status(age)  # Logic-based employment status
    num_children = get_num_children(marital_status)  # Probability-based number of children
    education_level = get_education_level(age)  # Logic-based education level
    health_status = random.choice(HEALTH_STATUSES)
    height = round(random.uniform(1.50, 2.00), 2)
    weight = round(random.uniform(50, 120), 2)
    bmi = calculate_bmi(height, weight)
    has_dl = random.choice([True, False])
    owns_vehicle = random.choice([True, False]) if has_dl else False  # Vehicle ownership depends on DL
    blood_group = random.choice(BLOOD_GROUPS)
    smoker = random.choice([True, False])
    alcohol_consumption = random.choice(ALCOHOL_CONSUMPTION)
    last_physical_checkup = random_date(2020, 2023)
    email = generate_email(name)  # Generate email based on name
    phone_number = generate_country_specific_phone_number(country)  # Generate country-specific phone number
    allergies = random.choice(['None', 'Pollen', 'Nuts', 'Dairy', 'Shellfish'])
    credit_score = random.randint(300, 850)
    life_insurance = random.choice([True, False])
    health_insurance = random.choice([True, False])

    # Append row as a tuple
    data.append((
        name, age, gender, dob, city, country, income, marital_status, employment_status,
        num_children, education_level, health_status, height, weight, has_dl, owns_vehicle,
        blood_group, smoker, alcohol_consumption, last_physical_checkup, email, phone_number,
        allergies, credit_score, life_insurance, health_insurance
    ))

# Write SQL INSERT statements to a .txt file
with open("sql_insert_statements.txt", "w") as file:
    file.write("INSERT INTO Individuals (Name, Age, Gender, DOB, City, Country, Income, Marital_Status, Employment_Status, Num_Children, Education_Level, Health_Status, Height, Weight, Has_DL, Owns_Vehicle, Blood_Group, Smoker, Alcohol_Consumption, Last_Physical_Checkup, Email, Phone_Number, Allergies, Credit_Score, Life_Insurance, Health_Insurance) VALUES\n")
    for row in data[:-1]:
        file.write(f"('{row[0]}', {row[1]}, '{row[2]}', '{row[3]}', '{row[4]}', '{row[5]}', {row[6]}, '{row[7]}', '{row[8]}', {row[9]}, '{row[10]}', '{row[11]}', {row[12]}, {row[13]}, {row[14]}, {row[15]}, '{row[16]}', {row[17]}, '{row[18]}', '{row[19]}', '{row[20]}', '{row[21]}', '{row[22]}', {row[23]}, {row[24]}, {row[25]}),\n")
    # Last row without trailing comma
    file.write(f"('{data[-1][0]}', {data[-1][1]}, '{data[-1][2]}', '{data[-1][3]}', '{data[-1][4]}', '{data[-1][5]}', {data[-1][6]}, '{data[-1][7]}', '{data[-1][8]}', {data[-1][9]}, '{data[-1][10]}', '{data[-1][11]}', {data[-1][12]}, {data[-1][13]}, {data[-1][14]}, {data[-1][15]}, '{data[-1][16]}', {data[-1][17]}, '{data[-1][18]}', '{data[-1][19]}', '{data[-1][20]}', '{data[-1][21]}', '{data[-1][22]}', {data[-1][23]}, {data[-1][24]}, {data[-1][25]});\n")
