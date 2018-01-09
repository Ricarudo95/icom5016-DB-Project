from flask import jsonify


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
        result['r_id'] = row[0]
        result['s_id'] = row[1]
        result['rname'] = row[2]
        result['category'] = row[3]
        result['quantity'] = row[4]
        result['price'] = row[5]
     

        return result
    #------Returns all Users in the Database

    def getAllUser(self):
        dao = UserDao()
        user_list = dao.getAllUser() 
        result_list = []
        for row in user_list:
            result = self.build_user_dict(row)
            result_list.append(result)
        return jsonify(Users=result_list)

    #------Recieves an User Id and the Retuns info of that User

    def getUserbyId(self, uid):
        dao = UserDao()
        row = dao.getUserbyId(uid)
        if not row:
            return jsonify(Error = "User Not Found"), 404
        else:
            user = self.build_user_dict(row)
            return jsonify(User = user);

    #------Recieves an User Id an the Retuns Suppliers the user has bought from.

    def getUserResources(self, uid):
        dao = UserDao()
        resource_list = dao.getUserResources(uid)
        result_list = []
        for row in resource_list:
            result = self.build_resource_dict(row)
            result_list.append(result)
        return jsonify(User_Resources = result_list)

