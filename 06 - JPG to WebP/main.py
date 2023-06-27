from PIL import Image
import os

#NÃO EDITAR ESSE BLOCO
def convert_to_webp(input_path, output_path, quality=80):
    img = Image.open(input_path)
    img.save(output_path, 'WebP', quality=quality)

#NÃO EDITAR ESSE BLOCO
def batch_convert_to_webp(input_folder, output_folder, quality=80):
    # Verifica se a pasta de destino existe, caso contrário, cria-a
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

#NÃO EDITAR ESSE BLOCO
    # Percorre todos os arquivos da pasta de entrada
    for filename in os.listdir(input_folder):
        if filename.endswith('.jpg') or filename.endswith('.jpeg'):
            input_path = os.path.join(input_folder, filename)
            output_filename = os.path.splitext(filename)[0] + '.webp'
            output_path = os.path.join(output_folder, output_filename)
            convert_to_webp(input_path, output_path, quality=quality)



# PREENCHA AQUI
input_folder = 'pasta/de/entrada'
output_folder = 'Output'
quality = 10  # Altere a qualidade conforme necessário
batch_convert_to_webp(input_folder, output_folder, quality=quality)