# English Indonesian Language Identifier
Simple English-Indonesian Language Identifier Web Application

**Developed by:**
- [Barik](https://github.com/rizkyebarik)
- [Roland](https://github.com/rolandhartanto)

## Requirements
- [Flask](http://flask.pocoo.org/docs/1.0/installation/)
- [ScikitLearn](https://scikit-learn.org/stable/install.html)
- [python-dotenv](https://github.com/theskumar/python-dotenv)
- [Joblib](https://joblib.readthedocs.io/en/latest/installing.html)

## Usage
Insert only **ONE WORD** to the text area and click the **"CLASSIFY"** button. The result will appear immediately. Click **"RESET"** button if you want to reset the text area and the result. 

## How to Run
1. Copy `example.env` and rename it as `.env`. Change the `DICTIONARY_PATH` variable according to your dictionary location. Dictionary usage is optional, so you can ignore the value of the variable.  
If you want to add the dictionary, you have to follow this dictionary CSV file format.
   ```
   kata,bahasa
   word1,label1
   ...
   wordn,labeln
   ```
   The first line is the header (copy it). Other lines contain pairs of word and its label. The label is either `indonesia` or `inggris`.

2. Set the environment variable value by executing this command in terminal.   
**Linux**
   ```
   export FLASK_APP=<insert file name here>
   ```
   **Windows**
   ```
   SET FLASK_APP=<insert file name here>
   ```

3. Run flask by executing this command.
   ```
   flask run
   ```
   Notes: You can also execute `run.bat` file if you use Windows to skip step 2 and 3. 
4. You can access the page by visiting `http://localhost:5000`.
