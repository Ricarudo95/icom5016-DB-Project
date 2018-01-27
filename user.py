
from flask import jsonify
from userdao import UserDAO


class UserHandler:
    
    #------Building Dictionary for user query results

    def build_user_dict(self, row):
        result = {}
        result['User Id'] = row[0]
        result['First Name'] = row[1]
        result['SurName'] = row[2]
        result['Password'] = row[3]
        result['Location'] = row[4]
        result['Address'] = row[5]
       
        return result

    #------Building Dictionary for Resources query results

    def build_resource_dict(self, row):
        result = {}
        result['Resource ID'] = row[0]
        result['Supplier ID'] = row[1]
        result['Resource Name'] = row[2]
        result['Category'] = row[3]
        result['Quantity'] = row[4]
        result['Price'] = row[5]

        return result

     #------Building Dictionary for Resources query results    
    def build_creditcard_dict(self, row):
        result = {}
        result['Credit Card ID'] = row[0]
        result['User ID'] = row[1]
        result['Card Number'] = row[2]
        result['Expiration Date'] = row[3]
        result['CVC Code'] = row[4]
        result['Status'] = row[5]

        return result

    #------Returns all Users in the Database

    def getAllUser(self):
        dao = UserDAO()
        user_list = dao.getAllUsers()
        result_list = []
        for row in user_list:
            result = self.build_user_dict(row)
            result_list.append(result)
        return jsonify(Users=result_list)

    #------Recieves an User Id and the Retuns info of that User

    def getUserbyId(self, uid):
        dao = UserDAO()
        row = dao.getUserById(uid)
        if not row:
            return jsonify(Error = "User Not Found"), 404
        else:
            user = self.build_user_dict(row)
            return jsonify(User = user);

    #------Recieves an User Id an the Retuns Suppliers the user has bought from.

    def getUserResources(self, uid):
        dao = UserDAO()
        resource_list = dao.getUserResources(uid)
        result_list = []
        for row in resource_list:
            result = self.build_resource_dict(row)
            result_list.append(result)
        return jsonify(User_Resources = result_list)


    def updateUserCreditCard(self, form):
        if len(form) != 5:
            return jsonify(Error = "Malformed post request") , 400
        else:
            u_id= form.get("u_id")
            ccNumber=form.get("card_number")
            expDate=form.get("expiration_date")
            cvc_code=form.get("cvc_code")
            c_update=form.get("Update")

            if u_id and ccNumber and expDate and cvc_code and c_update:
                dao = UserDAO()
                c_id= dao.updateUserCreditCard(u_id, ccNumber, expDate, cvc_code, c_update)
                return True
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400

    def addUser(self, form):
        if len(form) != 5:
            return jsonify(Error = "Malformed post request") , 400
        else:
            fname = form.get("uFirstName")
            lname = form.get("uLastName")
            upass = form.get("pass")
            loc = form.get("loc")
            address = form.get("address")
            if fname and lname and upass and loc and address:
                dao = UserDAO()
                u_id = dao.addUser(fname, lname, upass, loc, address)
                return self.getUserbyId(u_id)
                
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400
