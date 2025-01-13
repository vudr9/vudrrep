from flask import Flask, request, render_template_string
import requests

app = Flask(__name__)

@app.route('/')         # '/' (korijenska ruta) na pocetku
def home():
    return '''
        <form action="/send" method="get">
            <label for="par1" style=
            "height:60px; width:300px; font-size:40px; color:blue;" 
            >Unesite parametar:</label>
            <input type="text" id="par1"  style=
            "height:60px; width:300px; font-size:40px; color:blue; border-width: 2px; border-color: blue;
            margin-right: 30px;"
            name="par1" required>
            <button type="submit" style=
            "height:60px; width:150px; font-size:40px; color:blue; border-width: 2px; border-color: red;"
            >Pošalji</button>
            <br> <br>
            <button type="reset" style=
            "height:60px; width:150px; font-size:40px; color:green; border-width: 2px; border-color: green;
            margin-left: 350px;"
            >Počisti</button>
        </form>
    '''

@app.route('/send', methods=['GET'])
def send_to_php():
    par1 = request.args.get('par1')
    if not par1:
        return "Par1 parametar nije dostavljen!", 400
    
    # PHP skripta URL (localhost: Apache server)
    # php_url = f"http://localhost/D.php"
    php_url = "http://drvu.infinityfreeapp.com/D.php"   
    response = requests.get(php_url, params={'par1': par1}) # par1 = naziv parametra koji PHP skripta očekuje i
                                                            # vrijednost varijable par1 iz Flask aplikacije.
    
    if response.status_code == 200:
        #return f"Odgovor PHP skripte: {response.text}"
        #rez = "111" + response.text + " 222" + "333" + response.text + "444"      
        #return rez 
        return response.text        # prikazuje PHP stranicu  
    else:
        return f"Došlo je do greške pri pozivu PHP skripte: {response.status_code}"



if __name__ == '__main__':
    app.run(debug=True)	# True ili False

    #app.run()
