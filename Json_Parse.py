import json
import webbrowser

file = open ('Pizza.json')
array = json.load(file)

f=open('index.html','w',encoding='utf-16')

message='''<html>
<head>
<title>Pizza</title>
</head>

<body>
<h1>Pizza</h1>
'''
for pizza in array:
    name = pizza["name"]
    message+=f"<h2>Name: {name}</h2>"
    Ingredients = pizza["Ingredients"]
    message+=f"<p>Ingredients: {Ingredients}<p>"
    Cooking =pizza["Cooking"]
    message+=f"<p>Preparations: {Cooking}</p>"
    Steps= pizza["steps"]
    message+=f"<p>How to cook: {Steps}</p>"
    


message += """
</body>

</html>"""
f.write(message)
f.close()

webbrowser.open_new_tab('index.html')



Moviee = open ('Movies.json')
Movie_array = json.load(Moviee)

f=open('Movies.html','w',encoding='utf-16')
Movies='''<html>
<head>
<title>Movies</title>
</head>

<body>
<h1>Movies</h1>
'''
for Movie in Movie_array[:10]:
    title = Movie["Title"]
    Movies+=f"<h2>Title: {title}</h2>"
    Year = Movie["Year"]
    Movies+=f"<p>Year: {Year}</p>"
    Rated = Movie["Rated"]
    Movies+=f"<p>Rated: {Rated}</p>"
    img = Movie["Poster"]
    Movies+=f"<img src=\"{img}\">"
    Plot =Movie["Plot"]
    Movies+=f"<p>Plot: {Plot}</p>"
    
    

Movies += """
</body>

</html>"""
f.write(Movies)
f.close()

webbrowser.open_new_tab('Movies.html')

