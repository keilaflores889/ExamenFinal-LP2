from flask import Flask, render_template, request, redirect, url_for,flash
from dao.MateriaDao import MateriaDao

app = Flask(__name__)

# flash requiere esta sentencia
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

# INICIO-MATERIAS

@app.route('/materias-index')
def materias_index():
    #creacion de la instancia de materiadao
    materiasDao = MateriaDao()
    lista_materias = materiasDao.getMaterias()
    return render_template('materias/materias-index.html', lista_materias=lista_materias)

@app.route('/materias')
def materias():
    return render_template('materias/materias.html')

@app.route('/guardar-materia', methods=['POST'])
def guardarMateria():
    materia = request.form.get('txtDescripcion').strip()
    if materia == None or len(materia) < 1:
       # mostrar un mensaje al usuario
       flash('Debe escribir algo en la descripcion', 'warning')
    
       # redireccionar a la vista materias
       return redirect(url_for('materias'))
    
    materiadao = MateriaDao()
    materiadao.guardarMateria(materia.upper())

    # mostrar un mensaje al usuario
    flash('Guardado exitoso', 'success')

    # redireccionar a la vista materias
    return redirect(url_for('materias_index'))

@app.route('/materias-editar/<id>')
def materiasEditar(id):
    materiadao = MateriaDao()
    return render_template('materias/materias editar.html', materia=materiadao.getMateriaById(id))

@app.route('/actualizar-materia', methods=['POST'])
def actualizarMateria():
    id = request.form.get('txtIdMateria')
    descripcion = request.form.get('txtDescripcion').strip()

    if descripcion == None or len(descripcion) == 0:
        flash('No debe estar vacia la descripcion')
        return redirect(url_for('materiasEditar', id=id))

    # actualizar
    materiadao = MateriaDao()
    materiadao.updateMateria(id, descripcion.upper())

    return redirect(url_for('materias_index'))

@app.route('/materias-eliminar/<id>')
def materiasEliminar(id):
    materiadao = MateriaDao()
    materiadao.deleteMateria(id)
    return redirect(url_for('materias_index'))
# FIN-MATERIAS

# se pregunta por el proceso principal
if __name__=='__main__':
    app.run(debug=True)