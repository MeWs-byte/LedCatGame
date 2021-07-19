from flask import Flask, render_template, request, redirect, url_for, flash
import lights
import servoCat

status = 'static'
app = Flask(__name__)
app.secret_key = b'_1#y2l"F4Q8z\n\xec]/'
up = 0
@app.route('/', methods=['GET', 'POST'])
@app.route('/index/', methods=['GET', 'POST'])      # get a mini dash going here to control all the states and see incoming alarm
def index():
    
    
    global up
    global status
    
    if request.method == "POST":
        try:
            
            return redirect(url_for('index'))
            
        except:
            flash("Invalid type ")
        return redirect(url_for('index'))
    
  
    if request.method == "GET" and request.args.get("up", ""):   # fast sweep up
        status = 'fastSweepUp'
        print(status)
        upMe = request.args.get("up", "")
        print('this is upMe')
        print(upMe) 
        upNr = up + 1
        lights.sweepRightSingleRed()
        print(upNr)

    if request.method == "GET" and request.args.get("down", ""):  # fast sweep down
        status = 'fastSweepDown'
        print(status)
        downMe = request.args.get("down", "")
        print('this is downMe')
        print(downMe) 
        downNr = up + 1
        lights.sweepLeftSingleRed()
        print(downNr)  

    if request.method == "GET" and request.args.get("BlinkUp", ""):
        status = 'blinkUp'
        print(status)

        while status == 'blinkUp':

            BlinkUpMe = request.args.get("BlinkUp", "")

            #lights.goRightSingleRed()
            lights.loopLeftSingleRed() 

    if request.method == "GET" and request.args.get("BlinkDown", ""):
        status = 'blinkDown'
        print(status)  
        while status == 'blinkDown':

            BlinkDownMe = request.args.get("BlinkDown", "")
            
            #lights.goLeftSingleRed()  
            
            lights.loopRightSingleRed()

    if request.method == "GET" and request.args.get("servo", ""):
        servoMe = request.args.get("servo", "")
        servoCat.servoRun()    







    if request.method == "GET" and request.args.get("rainbow", ""): # rainbow
        rainbowMe = request.args.get("rainbow", "") 
        lights.rainbow_cycle(0.00000009)
        #lights.rainbow_cycle(0.009)    
                 
                
   

    return render_template('index.html')
    




app.run(host="0.0.0.0",threaded=True)