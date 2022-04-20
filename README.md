# fotos-perfil-santo-tomas-dl
Un script en python para descargar fotos de perfil de alumnos de Santo Tomás

# Uso

Ejecuta el script pasando el rut del alumno o un txt con ruts separados por linea, las fotos de perfil se descargarán en el mismo directorio en que se ejecute el script

    python santo-tomas-dl.py XXXXXXXX-X
    python santo-tomas-dl.py RUTs.txt

# OPCIONES
    --f                                  Formatea el nombre de la imagen descargada,
                                         puede ser 'rut', 'rut+age', 'age+rut', 'age',
                                         la edad es sólo un aproximado basado en el rut.
