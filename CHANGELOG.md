
# Change Log
All notable changes to this project will be documented in this file.
 
The format is based on [Keep a Changelog](http://keepachangelog.com/)
and this project adheres to [Semantic Versioning](http://semver.org/).
 

 
## [1.1.0] - 2022-04-06
 
### Added
- [Change Log](CHANGELOG.md)
- [requirements.txt](requirements.txt)
- Error handling
- Environment variables
   
### Changed
- Moved out db app initiation from the file name check if block in app.py.
- Python version to 3.9.12.
- Improved main() function.
- Renamed create_urls to create_todays_links.
- Renamed find_articles to find_article_links.
- Improved the variable names. 
- Improved code cleanness
 
### Fixed
- The broken web elements due to the web site update.

## Removed
- __connect() function; it's now part of insert_many() nethod.

