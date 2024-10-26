from fastapi import FastAPI

app = FastAPI() #fastapi instance - app created

#we can also change the name of the file to anything instead of main .. just the declaration will change.. 
# syntax - uvicorn <filename.py>:<instance_name> --reload

# ex - joy.py & instance is myhouse
#uvicorn joy:myhouse --reload


#app name is conventional... it can be anything
#uvicorn main:app --reload 

@app.get("/") #the path is set to root or just "/" which means base url
#this decorator tells FastAPI that the function below corresponds to the path / with an operation get


def index():
    return {"welcome note":'welcome to the world of sammisam'}
@app.get("/blog")
#here a path /blog was set up
def blog(): 
    #here blog doesnt need to be blog, it can be xyz or any other function name
    return {"data":"blog-list"}
#both the function names can also be completely same, but what matters is the decorator
#for dynamic routing we use f strings type
#@app.get('/path/{id_variable}')

#query-parameters
@app.get('/blog?limit=10&published=true')
#here we take the query parameter as per our need
#but to make it accessible via path parameter



@app.get('/blog/unpublished')
def unpublished():
    #thios section must be present before the dynamic routing within the same extension 
    return {"data":"unpublished blog list"}

@app.get('/blog/{id}')
#always mention this dynbamic routing at the end - because it will overtake all the other 
#id is the path parameter 
def show(id):
    return {"data":id}
# def showint(id:int):
#     #here the type conversion of id occurs from integer to string
#     return {"data int":id}

@app.get('/blog/{id}/comment')
#here we are getting a comment path for the customised id as per user input

def comment(id):
    return {"comment":f"Hey user id {id}"}

