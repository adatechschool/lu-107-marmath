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

# Exo Kata Find Intersection

exemple d'input input=['1, 3, 5, 8, 11, 13','1, 2, 5, 4, 10, 13'];

function FindIntersection(strArr) { 
let s1 = strArr[0].toString();
let s2 = strArr[1].toString();
//console.log(s1.split(","));
  // code goes here  
  //return strArr; 
s1 = s1.split(", ");
s2 = s2.split(", ");
// console.log(s1, s2);
  let tabVide = [];
  for (i=0; i<s1.length;i++){
    for (j=0;j<s2.length;j++){
      //console.log(s1[i], "haha", s2[j]);
      if(s1[i] === s2[j]){
        // console.log(s1[i]);
        strArr = tabVide.push(s1[i]);
        strArr = tabVide.join(',');
      }
    }
  }
return strArr
}
   
// keep this function call here 
console.log(FindIntersection(readline()));
