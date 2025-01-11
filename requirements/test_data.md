Test Data for MyAnimeList Automation
Test Accounts
Note: Credentials are stored securely in .env file
Valid Test Account

Username: Stored in VALID_USERNAME env variable
Password: Stored in VALID_PASSWORD env variable

Invalid Test Credentials

Invalid Username: Stored in INVALID_USERNAME env variable
Invalid Password: Stored in INVALID_PASSWORD env variable
Account Status Variations Needed

New account (empty lists)
Established account (with existing lists)
Premium account (if applicable)

Test Anime Data
Search Test Data
Popular Titles (Expected to exist):

"Death Note"
"One Piece"
"Attack on Titan"

Special Characters:

".hack//Sign"
"5 Centimeters per Second"
"FLCL"

List Test Data
Anime for List Operations:

Currently Airing Show

Title: [Current Season Anime]
Episodes: Ongoing


Completed Show

Title: "Death Note"
Episodes: 37


Movie

Title: "Your Name"
Type: Movie



Test Manga Data
Search Test Data
Popular Titles:

"Naruto"
"One Punch Man"
"Berserk"

List Test Data
Manga for List Operations:

Ongoing Series

Title: [Current Publishing Manga]
Chapters: Ongoing


Completed Series

Title: "Death Note"
Chapters: 108



Expected Results
Login Tests

Valid Login: Should redirect to home page with user menu visible
Invalid Login: Should show error message
Empty Fields: Should show field validation messages

Search Tests

"Death Note" Search:

Should appear in top results
Should show both anime and manga versions
Should display correct rating and status



List Operations

Add to List:

Should show confirmation
Should appear in user's list
Should update user's stats



Test Environment Details
Browsers to Test

Chrome (latest)
Firefox (latest)
Edge (latest)

Viewport Sizes

Desktop: 1920x1080
Tablet: 768x1024
Mobile: 375x667

Network Conditions

Fast 4G
Slow 3G (for handling loading states)