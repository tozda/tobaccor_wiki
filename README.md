# tobaccor_wiki
This script generates TiddlWiki tiddler (*.tid) file ready to be imported into TiddlyWiki. This tiddler file contains selected information on tobacco downloaded form https://www.tobaccoreviews.com/ site.

The process:
1. Open TR and search for the particular tobacco. Copy the URL.
2. Run the 'main.py' script
3. Provide copied URL as input to the script
4. Wait till script completes
5. Open your TiddlyWiki
6. Click "import" icon and look for 'tobacco.tid' file located at the same directory as 'main.py' script
7. Import tiddler

# The file structure
1. 'main.py' - główny skrypt
2. 'utensylia.py' - biblioteka funkcji pomocniczych
3. 'tw_template.txt' - generyczny szablon tiddlera w oparciu o który tworzony jest plik wyjściowy
4. 'tobacco.tid' - plik wyjściowy. Tiddler TiddlyWiki zawierający informacje o konkretnym tytoniu zaimportowane ze strony tobaccoreview.com
