
var points = 4;
var bronzeButtonOn = false
var silverButtonOn = false
var goldButtonOn = false
var platinumButtonOn = false

function Currentpoints(){

    document.getElementById("current_points").innerHTML = "Your Current Points are " + points;
}

function TierSpec(){
  
    var tier = ["bronze", "silver", "gold", "platinum"];
    var currentTier;
    
  
        
        points++;

         if (points <= 5){
            var currentTier = tier[0];
            
            if (bronzeButtonOn == false){
                    // 1. Create the button
                    var button1 = document.createElement("input");
                    //button1.innerHTML = "Upgrade to Silver!";
                    button1.setAttribute("type", "button")
                    button1.setAttribute("value", "Claim Bronze prize")
                    button1.setAttribute("id", "button1")
                    button1.setAttribute("onclick","window.location='gold.html'");

                    // 2. Append somewhere
                    var body = document.getElementsByTagName("body")[0];
                    body.appendChild(button1);
                    bronzeButtonOn = true;
                    silverButtonOn = false
                    goldButtonOn = false
                    platinumButtonOn = false
            }
        }

            else if (points > 5 <= 10){
                currentTier = tier[1];
                
                if (silverButtonOn == false){
                // 1. Create the button
                var button2 = document.createElement("input");
                //button1.innerHTML = "Upgrade to Silver!";
                button2.setAttribute("type", "button")
                button2.setAttribute("value", "Claim Silver prize")
                button2.setAttribute("id", "button2")
                button2.setAttribute("onclick","/HACKATHON/templates/prize.html");
                
                // 2. Append somewhere
                var body = document.getElementsByTagName("body")[0];
                body.appendChild(button2);
                silverButtonOn = true;
                bronzeButtonOn = false
                goldButtonOn = false
                platinumButtonOn = false
                }
            }


                else if (points >10 <= 15){
                    currentTier = tier[2];
                    bronzeButtonOn=false;
                    document.getElementById("button1").remove();
                                    
                    if (goldButtonOn == false){
                                    // 1. Create the button
                        var button3 = document.createElement("input");
                        //button1.innerHTML = "Upgrade to Silver!";
                        button3.setAttribute("type", "button")
                        button3.setAttribute("value", "Claim Platinum prize")
                        button3.setAttribute("id", "button3")
                        button3.setAttribute("onclick","/HACKATHON/templates/prize.html");
                        
                        // 2. Append somewhere
                        var body = document.getElementsByTagName("body")[0];
                        body.appendChild(button3);
                        goldButtonOn = true;
                        bronzeButtonOn = false
                        silverButtonOn = false
                        platinumButtonOn = false
                    }
        
                    }


                    else if (points >15 <= 20){
                        currentTier = tier[3];

            if (platinumButtonOn == false){            
            // 1. Create the button
            var button4 = document.createElement("input");
            //button1.innerHTML = "Upgrade to Silver!";
            button4.setAttribute("type", "button")
            button4.setAttribute("value", "Claim prize")
            button4.setAttribute("id", "button4")
            button4.setAttribute("onclick","/HACKATHON/templates/prize.html");
            
            // 2. Append somewhere
            var body = document.getElementsByTagName("body")[0];
            body.appendChild(button4); 
            platinumButtonOn = true;
            bronzeButtonOn = false
            silverButtonOn = false
            goldButtonOn = false

                        }
                    }

            document.getElementById("after_submit").style.visibility = "visible";

            document.getElementById("tier_achieved").innerHTML = "Your Current Tier is " + currentTier;
            document.getElementById("points_you_have").innerHTML = "You got " + points + " on your account.";
        
/*
                if (points>= 5 < 10){
                    tier=silver
                    document.getElementById("Button2").value="Upgrade to Gold!";
                }
                    
            
                if (points>= 10 < 15){
                    tier=gold
                    document.getElementById("Button3").value="Upgrade to Platinum!";
                }

                 if (points>= 15 <20){
                     tier=platinum}

                if (points= 20){
                    tier=platinum}
*/


               /*( if points>=5:           
                   #claim bronze prize button
                    elif: 
                        #roll over to next tier button
            if points<= 10:
                tier=silver
                if points>=10:
                    #claim silver prize button
                    else: 
                        #roll over to next tier button
            if points<= 15:
                tier=gold
                if points>=15:
                    #claim gold prize button
                    else:
                        #roll over to next tier button
            if points<= 20:
                tier=platinum
                if points==20: */





}

