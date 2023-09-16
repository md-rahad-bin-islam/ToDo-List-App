# Todo Application  

This is a complete Todo Application made using Django and Boostrap. It has all the features required by a Todo Application. 

## Demo 
![Demo 1](https://github.com/arkalsekar/todo-app/blob/main/demo/home.JPG?raw=true)

![Demo 2](https://github.com/arkalsekar/todo-app/blob/main/demo/update.JPG?raw=true)

## Characteristics

Here are the Features of the Application created.
</br>
1. User can Create a New Task.
2. See all the previous Task.
3. Update a Created Task.
4. Delete the Tasks Completed.


## Setting Up

Clone or Download the this repository and store it on your machine. 
```bash
git clone https://github.com/arkalsekar/todo-app.git
```

## Usage
Once Downloaded or Cloned the Repository, Run the following Commands

```bash
pip install -r requirements.txt
```
Once Installed all the requirements. Run the Following Commands.
```bash
python manage.py makemigrations
```
```bash
python manage.py migrate
```
This is isin't necessary but with this you would be able to login to the website.
```bash
python manage.py createsuperuser
```
This command will finally run the server on localhost://8000
```bash
python manage.py runserver
```
Now head on to [http://127.0.0.1:8000/](http://127.0.0.1:8000/) and access the site.


## License
[MIT](https://choosealicense.com/licenses/mit/)
