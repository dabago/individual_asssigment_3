#%%
from flask import Flask, jsonify


server = Flask("Phonebook")


phonebook = {"anastasia": "1113333444",
           "agata": "222333444",
           "octavio":"3334445555",
           "david":"444555666"}


@server.route("/home")
def home_page():
    return "Welcome to the best phonebook ever"


@server.route("/myphonebook")
def myphonebook():

    return jsonify(phonebook)


@server.route("/add-contact/<name>/<phone>", methods = ["PUT"])
def add_contact(name, phone):

    if phone.isdigit() == True:
        phonebook.update({name:phone})

        return jsonify("Contact has been sucessfully added")

    else:

        return "Please check the phone you have introduced only contains numbers"


@server.route("/get-phone/<name>")
def get_phone(name):

    for i in phonebook:

        if i == name.lower():

            return jsonify("Here you go! " + name + "'s phone is " + phonebook[i])

    else:

        return jsonify("Sorry, your search was not successful. Please try again")


@server.route("/delete-phone/<name>", methods = ["DELETE"])
def del_phone(name):

    for i in phonebook:

        if i == name.lower():

            del phonebook[i]

            return jsonify("The data from {} has been removed from the phonebook".format(i))

    else:

        return jsonify("Sorry, your search was not successful")


@server.route("/update-phone/<name>/<phone>", methods = ["POST"])
def update_phone(name,phone):


    for i in phonebook:
        if phone.isdigit() == True :

            if i==name.lower():

                phonebook[i] = phone

                return jsonify("The phonebook has been updated. The new {}'s number is {}".format(name,phone))
        else:

            return jsonify("Please check the phone you have introduced only contains numbers")
    else:

        return jsonify("Sorry, {} does not exist in your phonebook. The update was not successful".format(name))





server.run()
