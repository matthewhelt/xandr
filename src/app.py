#!/usr/bin/python3

# Xandr Code Sample
# A simple single file rest API example used to update a data structure
# MRH, 2021-06-03

# imports
from flask import Flask, jsonify, request, session

# defs and global needs
app = Flask(__name__)

employees = [{'id': 0, 'name': 'Anem Ployee', 'salary': 1000},
             {'id': 1, 'name': 'Anoth Eremployee', 'salary': 24000}]

# utility functions
def grant_raise_05(id, employees):
    # find the record then update, there are many other ways to do this, but this
    # is easy to read. note this change will not persist since it's modifying an
    # in-memory list of dicts

    new_employee_list = []

    # find & update dictionary
    for record in employees:
        if record['id'] == id:
            # hardcoded for brevity, needs a proper rounding function
            record['salary'] += int((record['salary'] * 0.05))

        new_employee_list.append(record)

    # rescope updated list
    employees = new_employee_list

# application

@app.route("/", methods=["GET", "PUT"], defaults={'id': None})
@app.route("/<id>", methods=["GET", "PUT"])
def get_employee(id):

    if request.method == "GET":
        # if no ID is passed in the url, presume query for all records
        # otherwise return specific query for the ID in the resource identifier
        if id is not None:
            id = int(id)
            return jsonify(employees[id])
        else:
            # should add handling for errors here
            return jsonify(employees)

    if request.method == "PUT":
        if id is not None:
            grant_raise_05(int(id), employees)

            # assuming success, return update resource
            return '', 204
        else:
            # no id, no resource - return unacceptable input
            return '', 406


# entry point
if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
