import requests
from bs4 import BeautifulSoup
import os
from duckduckgo_search import DDGS

#1. Creating index.md:
response = requests.get('https://www.nationalgeographic.com/animals/mammals/facts/domestic-dog')
html_content = response.text
soup = BeautifulSoup(html_content, 'html.parser')

headings = soup.find_all("h2")
paragraphs = soup.find_all("p")

path1 = os.path.join(os.getcwd(), "index.md")
with open(path1, 'w') as f2:
    f2.write("# Dogs\n\n")
    f2.write(f"{headings[0].text}\n\n")
    f2.write(f"{paragraphs[6].text}\n\n")
    f2.write(f"{paragraphs[6].text}\n\n")
    
    f2.write(f"[List of the most popular dogs breeds](list.md)\n\n")
    f2.write("![photo](https://www.alcazar.in/UserUploads/Editted-Images/yWGlBiEHBzLJWmS9GeJi.jpg)")
print("index.md - finished")
    
    
#2. Creating list.md:
response = requests.get('https://www.alcazar.in/blog/a-complete-dog-breed-list')
html_content = response.text
soup = BeautifulSoup(html_content, 'html.parser')
list_of_dogs = soup.find_all('td')
n = len(list_of_dogs)
column_names = list_of_dogs[0:7]

i = 7
with open('list.md', 'w') as f:
    f.write("# _List of the most popular dogs breeds:_\n\n")
    
    while i < n:
        start = i
        end = i + 7
        
        f.write(f"### {list_of_dogs[i].text}. {list_of_dogs[i + 1].text}\n\n")
        
        for el in range(start + 2, end):
            f.write(f"**{column_names[el%7].text}:** {list_of_dogs[el].text}\n\n")
        f.write("\n")
        
        dog_name = list_of_dogs[i+1].text
        dog_name = dog_name.replace(' ', '_')
        file_name = f"dogs-informations/{dog_name}.md"
        f.write(f"[More information about {list_of_dogs[i+1].text}]({file_name})\n\n\n\n")

        i = end
print("list.md - finished")  
        
#3. List with photos
list_of_photos = soup.find_all("img")
list_of_photos = [el for el in list_of_photos if "Editted-Images" in str(el)]
list_of_photos = [str(el).split("\"")[7] for el in list_of_photos]
list_of_photos = [f"https://www.alcazar.in{el}" for el in list_of_photos]


#4. Creating sites with all breeds:
from duckduckgo_search import DDGS
for i in range(8, len(list_of_dogs), 7):
    #print(list_of_dogs[i].text)
    dog_name = list_of_dogs[i].text
    
    path1 = os.path.join(os.getcwd(), "dogs-informations", f"{dog_name.replace(' ', '_')}.md")
    with open(path1, 'w') as f3:
        f3.write(f"# {dog_name}\n\n")
    
        f3.write(f"### {dog_name} - description:\n\n")
        
        print(f"{dog_name} description...", end="")
        results = DDGS().text(f"{dog_name} description", max_results=1)
        f3.write(results[0]['body'])
        f3.write(f"[\[read more\]]({results[0]['href']})\n\n**Source:** __[{results[0]['title']}]({results[0]['href']})__\n\n")
        
        f3.write(f"### {dog_name} - training:\n\n")
        results = DDGS().text(f"{dog_name} training", max_results=3)
        for j in range(3):
            f3.write(f"* {results[j]['body']}")
            f3.write(f"[\[read more\]]({results[j]['href']})\n\n")
        
        f3.write(f"### {dog_name} - character:\n\n")
        results = DDGS().text(f"{dog_name} character", max_results=2)
        for j in range(2):
            f3.write(f"* {results[j]['body']}")
            f3.write(f"[\[read more\]]({results[j]['href']})\n\n")
        
        
        link = list_of_photos[int(i/7) - 1]
        f3.write(f"![photo]({link})")
        
    print(int(i/7) - 1, end=",\n")

