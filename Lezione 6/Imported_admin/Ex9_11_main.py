from Ex_9_11_Importedadmin_user import User, Priviliges,Admin

user:User = User("Antonio", "Rossi", "Nive35678", "antonio.@mail.com")
priv:Priviliges = Priviliges(["can add post", "can delete post", "can ban user"])

admin:Admin = Admin(user,priv)

admin.show_info()