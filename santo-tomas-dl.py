import argparse, datetime, re, urllib.request

parser = argparse.ArgumentParser()

parser.add_argument('--f', help = 'formats the name of the output file',
                    choices = ['rut', 'rut+age', 'age+rut', 'age'],
                    default = 'rut')

parser.add_argument('rut', help = 'can be a RUT or a txt with RUTs')

args = parser.parse_args()

formats = {'rut':'@@@.jpg',
           'rut+age':'@@@(*** años).jpg',
           'age+rut':'*** años(@@@).jpg',
           'age':'*** años.jpg'}

def get_age(rut):
    age = int(datetime.datetime.now().year-(3.46*int(rut[:-8])+1930.3))
    return str(age)

def get_file(rut, name_format):
        file_name = name_format.replace('@@@', rut).replace('***', get_age(rut))
        urllib.request.urlretrieve(
            'https://misservicios.santotomas.cl/foto_usuario/generar_foto/imagen.ashx?qryRUT=%s'
            % rut, file_name)

def get_list(text):
    with open('%s.txt' % text) as file:
        return re.findall('\S+-\S+', file.read())

def get_string(string):
    if re.match('[0-9]{7,8}-[0-9kK]$', string):
        return [string]
    else:
        return get_list(string)

def loop_rut(rut_list):
    for rut in rut_list:
        get_file(rut, formats.get(args.f))
        print('%s saved' % rut)
    print('\nall saved')
    input()
    
loop_rut(get_string(args.rut))
