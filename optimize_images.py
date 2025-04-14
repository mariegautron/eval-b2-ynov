import os
from PIL import Image
import glob

def optimize_image(input_path, output_path, max_size=(1200, 1200), quality=85):
    """Optimise une image en la redimensionnant et en la compressant."""
    with Image.open(input_path) as img:
        # Redimensionner si nécessaire
        if img.size[0] > max_size[0] or img.size[1] > max_size[1]:
            img.thumbnail(max_size, Image.Resampling.LANCZOS)
        
        # Sauvegarder en WebP
        img.save(output_path, 'WEBP', quality=quality)

def main():
    # Créer le dossier pour les images optimisées
    output_dir = 'images/optimized'
    os.makedirs(output_dir, exist_ok=True)
    
    # Liste des formats d'images à optimiser
    image_extensions = ['*.jpg', '*.jpeg', '*.png']
    
    # Optimiser toutes les images
    for ext in image_extensions:
        for img_path in glob.glob(f'images/{ext}'):
            filename = os.path.basename(img_path)
            name, _ = os.path.splitext(filename)
            output_path = os.path.join(output_dir, f'{name}.webp')
            
            print(f'Optimisation de {img_path}...')
            optimize_image(img_path, output_path)

if __name__ == '__main__':
    main() 