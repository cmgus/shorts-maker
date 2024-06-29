# ###################333
#!/bin/bash

# Verificar que se haya proporcionado la URL como argumento
if [ $# -eq 0 ]; then
    echo "Error: Debes proporcionar la URL de la canción o playlist de YouTube."
    exit 1
fi

# Carpeta de destino para las descargas
destination_folder="musics"  # Puedes cambiar esta ruta según tu preferencia

# Crear la carpeta de destino si no existe
mkdir -p "$destination_folder"

# Obtener la URL proporcionada como argumento
url=$1

# Determinar el formato de salida
formato_salida="mp3"  # Por defecto, se descarga en formato mp3

if [ $# -eq 2 ]; then
    if [ "$2" == "mp4" ]; then
        formato_salida="mp4"
    elif [ "$2" != "mp3" ]; then
        echo "Error: El formato de salida debe ser 'mp3' o 'mp4'."
        exit 1
    fi
fi

# Descargar la canción o la lista de reproducción en el formato especificado
if [ "$formato_salida" == "mp3" ]; then
    youtube-dl --extract-audio --audio-format mp3 --output "$destination_folder/%(title)s.%(ext)s" "$url"
else
    youtube-dl --format 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/bestvideo+bestaudio' --merge-output-format mp4 --output "$destination_folder/%(title)s.%(ext)s" "$url"
fi

# Si deseas descargar solo el audio de una lista de reproducción y combinarlos en un solo archivo MP3, puedes usar el siguiente comando:
# youtube-dl --extract-audio --audio-format mp3 --yes-playlist --output "$destination_folder/%(playlist_title)s/%(playlist_index)s - %(title)s.%(ext)s" "$url"

echo "Descarga completada. Los archivos se han guardado en: $destination_folder"
