# Dataset Generator
This Python script generates a synthetic dataset of 10,000 individuals with realistic and diverse attributes, including personal, financial, health, and lifestyle data, while ensuring logical consistency and country-specific details, exporting the results as `SQL INSERT statements` for database use.

The quantity of the dataset can be adjusted to your needs by simply changing the range value in the `for` loop.
```
for i in range(1, 10001):
        ___ ___ ____
        _____ ______
        ____ _______
```
This synthetic dataset is designed to simulate realistic individual profiles with a wide range of attributes, making it suitable for applications such as database testing, machine learning, or software development. 

Certain features in the dataset are represented using `enumerated (ENUM) values` to ensure consistency and categorization, such as  `gender ('Male', 'Female', 'Non-binary', 'Prefer not to say')`, `marital status ('Single', 'Married', 'Divorced', 'Widowed')`, and `employment status ('Employed', 'Self-employed', 'Unemployed', etc.)`. 

Other fields, like `health status`, `blood group`, and `alcohol consumption` habits, also use predefined categories to reflect real-world scenarios.

Additionally, numerical attributes such as `age`, `income`, `height`, `weight`, and `credit score` are generated within plausible ranges, while logical constraints ensure coherence—for example, `education level` is tied to `age`, and `vehicle ownership` depends on whether the individual has a `driver’s license`. 
