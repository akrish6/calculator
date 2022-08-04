from flask import Flask, render_template, request
#from chatterbot import ChatBot
#from chatterbot.trainers import ChatterBotCorpusTrainer


#Flask initialization
app = Flask(__name__)

#chatbot=ChatBot('VA')
# Create a new trainer for the chatbot
#trainer = ChatterBotCorpusTrainer(chatbot)

# Now let us train our bot with multiple corpus
#trainer.train("chatterbot.corpus.english.greetings", "chatterbot.corpus.english.conversations" )

@app.route("/")
def home():
    return render_template("home.html")   

@app.route("/salvador")
def salvador():
    return "Hello, Salvador"

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/chatbot")
def chatbot():
    return render_template("chatbot.html")

#@app.route("/get", methods=["GET","POST"])
#def chatbot_response():
    #msg = request.form["msg"]
    #response = chatbot.get_response(msg)
    #return str(response)
    
if __name__ == "__main__":
    app.run(debug=True)
