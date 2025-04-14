import requests
import os

# Créer le dossier images s'il n'existe pas
if not os.path.exists('images'):
    os.makedirs('images')

# URLs des images à télécharger
image_urls = {
    'hero-bg.jpg': 'https://images.unsplash.com/photo-1464822759023-fed622ff2c3b?auto=format&fit=crop&w=1920&h=1080',
    'hike1.jpg': 'https://images.unsplash.com/photo-1464822759023-fed622ff2c3b?auto=format&fit=crop&w=800&h=600',
    'hike2.jpg': 'https://images.unsplash.com/photo-1506905925346-21bda4d32df4?auto=format&fit=crop&w=800&h=600',
    'hike3.jpg': 'https://images.unsplash.com/photo-1501785888041-af3ef285b470?auto=format&fit=crop&w=800&h=600',
    'gallery1.jpg': 'https://images.unsplash.com/photo-1464822759023-fed622ff2c3b?auto=format&fit=crop&w=800&h=800',
    'gallery2.jpg': 'https://images.unsplash.com/photo-1506905925346-21bda4d32df4?auto=format&fit=crop&w=800&h=800',
    'gallery3.jpg': 'https://images.unsplash.com/photo-1501785888041-af3ef285b470?auto=format&fit=crop&w=800&h=800',
    'gallery4.jpg': 'https://images.unsplash.com/photo-1464822759023-fed622ff2c3b?auto=format&fit=crop&w=800&h=800',
    'gallery5.jpg': 'https://images.unsplash.com/photo-1506905925346-21bda4d32df4?auto=format&fit=crop&w=800&h=800',
    'gallery6.jpg': 'https://images.unsplash.com/photo-1501785888041-af3ef285b470?auto=format&fit=crop&w=800&h=800'
}

# Télécharger chaque image
for filename, url in image_urls.items():
    print(f'Téléchargement de {filename}...')
    response = requests.get(url)
    if response.status_code == 200:
        with open(f'images/{filename}', 'wb') as f:
            f.write(response.content)
        print(f'{filename} téléchargé avec succès!')
    else:
        print(f'Erreur lors du téléchargement de {filename}') 