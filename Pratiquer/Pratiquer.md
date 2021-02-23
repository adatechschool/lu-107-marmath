# Pratiquer

Mettez dans ce dossier tout le code source produit dans les exercices proposés pour la partie "Pratiquer" de la fiche Level up

# Exo Kata boolean to string in ruby:

def boolean_to_string(b)
  <br>if b == true
    <br> return "true"
  <br>else 
    <br>return "false" 
  <br>end
<br>end

# Exo Kata filter odd numbers in js:

<br>function odds(values){
  // arrow it
  <br>return values.filter( (number)=> number % 2 );
<br>}

# Exo Kata birthday:
<br>def get_villain_name(birthdate): 
    <br>first = [ "The Evil","The Vile","The Cruel", "The Trashy","The Despicable", "The Embarrassing", "The Disreputable","The Atrocious", "The Twirling",  "The   <br>  Orange","The Terrifying", "The Awkward"]
    <br>last = ["Mustache", "Pickle", "Hood Ornament", "Raisin", "Recycling Bin", "Potato", "Tomato", "House Cat", "Teaspoon", "Laundry Basket"]
   <br> birthmonth = birthdate.month
   <br>birthDay = int(str(birthdate.day)[-1:])
   <br>x = f"'{first[birthmonth-1]+' '+ last[birthDay]}'"
   <br> pass
   <br> return x
