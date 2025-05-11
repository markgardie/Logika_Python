from models import User

# create
test_user = User.objects.create(
    name = "Test user", 
    email = "test@gmail.com"
    )

# read
all_users = User.objects.all()

test_user2 = User.objects.get(name = "Test user")

admins = User.objects.filter(role = "admin")

#update
test_user.email = "test2@gmail.com"
test_user.save()

#delete
test_user.delete()