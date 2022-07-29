from app import app, db
from flask import render_template, request, redirect
from models.models import *


@app.route('/')
def first_page():
    return render_template('first-page.html')


@app.route('/head-employee')
def select_command_employee():
    return render_template('head-employee.html')


@app.route('/head-salon')
def select_command_salon():
    return render_template('head-salon.html')


@app.route('/head-plant')
def select_command_plant():
    return render_template('head-plant.html')

# Add new employee
@app.route('/add-employee', methods=['GET', 'POST'])
def add_data_about_employee():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        department_type = request.form['department_type']
        department_id = request.form['department_id']

        employee = Employee(name=name, email=email, department_type=department_type, department_id=department_id)

        try:
            db.session.add(employee)
            db.session.commit()
            db.session.flush()
            return redirect('/data-employee')
        except:
            return 'Error! No data was added'
    else:
        return render_template('add-employee.html')


@app.route('/data-employee', methods=['POST', 'GET'])
def show_data_employee():
    all_data_employee = Employee.query.all()
    return render_template('data-employee.html', all_data_employee=all_data_employee)

# Delete data by id
@app.route('/delete/<int:department_id>/del', methods=['POST', 'GET'])
def delete_data_about_employee(department_id):
    delete_data_employee = Employee.query.get_or_404(department_id)
    try:
        db.session.delete(delete_data_employee)
        db.session.commit()
        return redirect('/data-employee')
    except:
        return 'Error!No data was delete'


@app.route('/update-employee/<int:department_id>/up', methods=['POST', 'GET'])
def update_data_about_employee(department_id):
    update_employee = Employee.query.get(department_id)
    if request.method == 'POST':
        update_employee.name = request.form['name']
        update_employee.email = request.form['email']
        update_employee.department_type = request.form['department_type']

        try:
            db.session.add(update_employee)
            db.session.commit()
            return redirect('/data-employee')
        except:
            return 'Error! Data not update'
    else:
        return render_template('update-employee.html', update_employee=update_employee)
# ADD DATA PLANT
@app.route('/add-plant', methods=['GET', 'POST'])
def add_data_about_plant():
    if request.method == 'POST':
        location = request.form['location']
        name_plant = request.form['name_plant']
        director_id = request.form['director_id']

        plant = Plant(location=location, name_plant=name_plant, director_id=director_id)

        try:
            db.session.add(plant)
            db.session.flush()
            db.session.commit()
            return redirect('/data-plant')
        except:
            return 'Error!'
    else:
        return render_template('add-plant.html')

@app.route('/data-plant', methods=['POST', 'GET'])
def all_data_about_plant():
    all_data_plant = Plant.query.all()
    return render_template('data-plant.html', all_data_plant=all_data_plant)


@app.route('/delete-plant/<int:director_id>/del', methods=['POST', 'GET'])
def delete_data_about_plant(director_id):
    delete_data_plant = Plant.query.get(director_id)

    try:
        db.session.delete(delete_data_plant)
        db.session.commit()
        return redirect('/data-plant')
    except:
        return 'Error'


@app.route('/update-plant/<int:director_id>/up', methods=['POST', 'GET'])
def update_data_about_plant(director_id):
    update_plant = Plant.query.get(director_id)
    if request.method == 'POST':
        update_plant.location = request.form['location']
        update_plant.name_plant = request.form['name_plant']

        try:
            db.session.add(update_plant)
            db.session.commit()
            return redirect('/data-plant')
        except:
            return 'Error'
    else:
        return render_template('update-plant.html', update_plant=update_plant)

# ADD SALON
@app.route('/add-salon', methods=['POST', 'GET'])
def add_data_about_salon():
    if request.method == 'POST':
        name_salon = request.form['name_salon']
        adress_salon = request.form['adress_salon']
        id_salon = request.form['id_salon']

        salon = Salon(name_salon=name_salon, adress_salon=adress_salon, id_salon=id_salon)

        try:
            db.session.add(salon)
            db.session.flush()
            db.session.commit()
            return redirect('/data-salon')
        except:
            return 'Error'
    else:
        return render_template('add-salon.html')

@app.route('/data-salon', methods=['POST', 'GET'])
def show_data_salon():
    all_data_salon = Salon.query.all()
    return render_template('data-salon.html', all_data_salon=all_data_salon)


@app.route('/delete-salon/<int:id_salon>/del')
def delete_data_about_salon(id_salon):
    delete_data_salon = Salon.query.get_or_404(id_salon)

    try:
        db.session.delete(delete_data_salon)
        db.session.commit()
        return redirect('/data-salon')
    except:
        return 'Error!No data was delete'

@app.route('/update-salon/<int:id_salon>/up', methods=['GET', 'POST'])
def update_data_about_salon(id_salon):
    update_salon = Salon.query.get(id_salon)
    if request.method == 'POST':
        update_salon.name_salon = request.form['name_salon']
        update_salon.adress_salon = request.form['adress_salon']

        try:
            db.session.add(update_salon)
            db.session.commit()
            return redirect('/data-salon')
        except:
            return 'Error'
    else:
        return render_template('update-salon.html', update_salon=update_salon)

# SEARCH BY NAME
@app.route('/find-employee', methods=['GET'])
def employee_name_by_search():
    return render_template('find-employee.html')


@app.route('/found-employee', methods=['GET'])
def find_employee_by_name():
    if request.args.get('name', False):
        try:
            found_employee_name = Employee.query.filter(Employee.name == request.args.get('name')).first()
            return render_template('found-employee.html', found_employee_name=found_employee_name)
        except:
            return 'Error!'
    if request.args.get('email', False):
        found_employee_name = Employee.query.filter(Employee.email == request.args.get('email')).first()
        return render_template('found-employee.html', found_employee_name=found_employee_name)
    if request.args.get('department_type', False):
        found_employee_name = Employee.query.filter(Employee.department_type == request.args.get('department_type')).first()
        return render_template('found-employee.html', found_employee_name=found_employee_name)
    if request.args.get('department_id', False):
        found_employee_name = Employee.query.filter(Employee.department_id == request.args.get('department_id')).first()
        return render_template('found-employee.html', found_employee_name=found_employee_name)
    else:
        return 'Error!'

@app.route('/find-plant', methods=['GET'])
def plant_name_by_search():
    return render_template('find-plant.html')


@app.route('/found-plant', methods=['GET'])
def find_plant_by_name():
    if request.args.get('name_plant', False):
        found_name_plant = Plant.query.filter(Plant.name_plant == request.args.get('name_plant')).first()
        return render_template('found-plant.html', found_name_plant=found_name_plant)
    if request.args.get('location', False):
        found_name_plant = Plant.query.filter(Plant.location == request.args.get('location')).first()
        return render_template('found-plant.html', found_name_plant=found_name_plant)
    if request.args.get('director_id', False):
        found_name_plant = Plant.query.filter(Plant.director_id == request.args.get('director_id')).first()
        return render_template('found-plant.html', found_name_plant=found_name_plant)
    else:
        return 'Error'

@app.route('/find-salon', methods=['GET'])
def salon_name_by_search():
    return render_template('find-salon.html')

@app.route('/found-salon', methods=['GET'])
def find_salon_name():
    if request.args.get('name_salon', False):
        try:
            found_name_salon = Salon.query.filter(Salon.name_salon == request.args.get('name_salon')).first()
            return render_template('found-salon.html', found_name_salon=found_name_salon)
        except:
            return 'Error '

    if request.args.get('adress_salon', False):
        found_name_salon = Salon.query.filter(Salon.adress_salon == request.args.get('adress_salon')).first()
        return render_template('found-salon.html', found_name_salon=found_name_salon)
    if request.args.get('id_salon', False):
        found_name_salon = Salon.query.filter(Salon.id_salon == request.args.get('id_salon')).first()
        return render_template('found-salon.html', found_name_salon=found_name_salon)
    else:
        return 'Error Find-Store'
