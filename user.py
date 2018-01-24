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


    def searchUser(self, args):
        fname = args.get("uFirstName")
        lname = args.get("uLastName")
        upass = args.get("pass")
        loc = args.get("loc")
        dao = UserDAO()
        userlist = []
        result_list = []
        if (len(args) == 1) and fname
            userlist = dao.getUserbyName(fname)
        for row in userlist:
            result = self.build_user_dict(row)
            result_list.append(result)
        return jasonify(User = result_list)
