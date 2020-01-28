1. PULL THE IMAGE FROM DOCKER HUB
   docker pull chamika55/flaskapp:compare_strings

2. BUILD THE IMAGE
   docker build . -t chamika55/flaskapp 


3. RUN THE FOLLOWING COMMANDS
   docker run -it -d -p 5000:5000 chamika55/flaskapp
   docker run chamika55/flaskapp 

4. USE THE FOLLOWING URI TO ACCESS API ENDPOINT
   http://127.0.0.1:5000/comapre_strings


5. SAMPLE JSON PAYLOAD
    
    {
    "string1": "The easiest way to earn points with Fetch Rewards is to just shop for the products you already love. If you have any participating brands on your receipt, you'll get points based on the cost of the products. You don't need to clip any coupons or scan individual barcodes. Just scan each grocery receipt after you shop and we'll find the savings for you",
    "string2": "The easiest way to earn points with Fetch Rewards is to just shop for the items you already buy. If you have any eligible brands on your receipt, you will get points based on the total cost of the products. You do not need to cut out any coupons or scan individual UPCs. Just scan your receipt after you check out and we will find the savings for you",
    "order_of_words": "False"
    }


    

