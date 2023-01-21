firstly make model of the data base then make migrations using `python manage.py makemigrations`
then after making migration migrate it using `python manage.py migrate`


# this added to get name as a object name 
    def __str__(self):
        return self.name
