# PyPass-Generator

PyPass Generator is a Password Generator Program, which is created using Tkinter GUI.

The feather of these programs are that we created Tkinter window on that a Canvas, defined some padding and on the canvas we've putted lock img on it,
than there is some labels, entries, buttons of different sizes we've created them and positioned them properly on a window.

Defining Functions

1. find_password: this function is associated with search button, when we enter website name in web entry, and press search, it will read the data.json file and try to find the 
email and pass attached to that website, saved in json file, if file is not created or data of website is not found it will give error prompt on the screen.

2. generate_password: this function is associated with generate button, all we have to do is write website and email in their respective entries, click on generate password
button, it will create a password which will have randomize combination of nums, symbols, and letters small or caps, and will copy it on clipboard.

3. write_json: this func is used in other functions wherever we want to dummp data in json file, if file is there than dump it, if not than use this func to create a file
and write the data in it.

4. save: this is attached to add button, simply gets whatever written in all enteries pyut them in a dict form or json form and then save it in data.json file,also checks 
whether any field is left empty befire ppressing the add button if yes will show error prompt, after saving will delete everything from all fields.

5. put_default: it will display the last typed email in the email entry, it's not a very imp func but adds a functionality, all other fields will be empty.
