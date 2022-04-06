# About the project
This project is a web scarper developed for [The Guardian](https://www.theguardian.com/au) website. It finds and parses the articles on the website and ultimately saves them in a MongoDB database.

## Built With

- Python 3.9.12
- beautifulsoup
- pymongo
- requests


# Getting Started

## Installation
Download or clone the repository in your machine. In the Command Prompt in Windows or bash in Linux, go to folder that you cloned/copied the code. Then run `pip install -r requirements.txt` to install all requirements.

[requirements](requirements.txt) can be found in the project folder. You may want to run virtualenv before running pip.<br/>

# Configuration
You need to enter news categories urls in [categories](categories.md) file. There are already two sample urls in the file.
<br/>

There also certain variables thta need to be stored as environment variables for the security perspective.
- MONGO_USERNAME
- MONGO_PASSWORD
- MONGO_URI
- MONGO_DB
- MONGO_COLLECTION
<br/><br/>

# Usage
In the Command Prompt/bash run below command:

`python.exe app.py`

# Contributing
Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are greatly appreciated.

1. Fork the Project
2. Create your Feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request.

# License
Distributed under the MIT License. See [LICENSE](LICENSE) for more information.

# Change Log
To learn more about the changes in this version, please refer to [Change Log](CHANGELOG.md)

# Contact
Ali Hosseini on https://twitter.com/a1iie62 or Ali.Hoss3ini@gmail.com

Project Link: https://github.com/aliie62/captcha_solver

