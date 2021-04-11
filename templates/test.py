import requests


# url = 'https://img4.goodfon.com/wallpaper/nbig/c/93/hi-tech-technology-projector-katushki-kinoplenka-movie-retro.jpg'
url = 'https://s2.best-wallpaper.net/wallpaper/3840x2160/1712/Movie-projector-retro-style_3840x2160.jpg'
r = requests.get(url, allow_redirects=True)

open('projector_2.jpg', 'wb').write(r.content)